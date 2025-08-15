import customtkinter as ctk
import re
import speech_recognition as sr
import threading
import time

# ======================================================
# --------------- Safe Evaluation --------------------
# ======================================================
def safe_eval(expr):
    """
    Safely evaluate mathematical expressions.
    Supports +, -, *, /, **, √ (square root), and ² (square)
    """
    try:
        # Replace special symbols with Python equivalents
        expr = expr.replace("√", "math.sqrt")
        expr = expr.replace("²", "**2")

        # Only allow numbers, operators, parentheses, and math functions
        allowed = re.compile(r'^[0-9\.\+\-\*\/\(\) mathsqrt]+$')
        if not allowed.match(expr):
            return "ERROR"

        # Evaluate expression safely
        result = eval(expr)

        # Round float results for readability
        if isinstance(result, float):
            result = round(result, 10)

        return result
    except:
        return "ERROR"


# ======================================================
# --------------- Button Click Handler ----------------
# ======================================================
def on_button_click(value):
    current_text = entry_field.get()

    if value == "C":  # Clear entry field
        entry_field.delete(0, ctk.END)

    elif value == "DEL":  # Delete last character
        if current_text == "ERROR":
            entry_field.delete(0, ctk.END)
        elif len(current_text) > 0:
            entry_field.delete(len(current_text)-1, ctk.END)

    elif value == "=":  # Evaluate expression
        if current_text.strip() == "":
            return
        result = safe_eval(current_text)
        entry_field.delete(0, ctk.END)
        entry_field.insert(ctk.END, str(result))

    elif value == "x²":  # Square
        entry_field.insert(ctk.END, "²")

    elif value == "√":  # Square root
        entry_field.insert(ctk.END, "√")

    else:  # Append number/operator
        entry_field.insert(ctk.END, value)

    # Ensure cursor stays at the end
    entry_field.xview_moveto(1)


# ======================================================
# --------------- Voice Button Animation --------------
# ======================================================
def animate_voice_button(stop_event):
    """
    Animate the voice button while listening
    """
    colors = ["#1f6aa5", "#2f82c5", "#4da3e0"]
    i = 0
    while not stop_event.is_set():
        voice_btn.configure(fg_color=colors[i % len(colors)])
        i += 1
        time.sleep(0.3)
    # Reset to default color
    voice_btn.configure(fg_color="#2c506b")


# ======================================================
# --------------- Voice Command Handler ---------------
# ======================================================
def voice_command_thread():
    """
    Handles voice input and updates entry field.
    Appends voice commands to existing text instead of replacing it.
    """
    stop_event = threading.Event()
    animation_thread = threading.Thread(target=animate_voice_button, args=(stop_event,), daemon=True)
    animation_thread.start()

    voice_btn.configure(text="Listening...", font=("Consolas", 16, "bold"))

    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            command_text = recognizer.recognize_google(audio_data, language="bn-BD")

            # Replace Bengali & English math words with symbols
            replacements = {
                "যোগ": "+", "বিয়োগ": "-", "বিয়োগ": "-", "গুণ": "*", "ভাগ": "/",
                "plus": "+", "minus": "-", "multiply": "*", "times": "*", "divide": "/",
                "square": "²", "√": "√", "root": "√"
            }

            cmd = command_text.lower()
            for word, symbol in replacements.items():
                cmd = cmd.replace(word, symbol)

            # Keep only valid characters
            cmd = re.sub(r"[^0-9\+\-\*\/\(\)√²\.]", "", cmd)

            # Append to existing entry field
            for char in cmd:
                entry_field.insert(ctk.END, char)
                entry_field.update()
                time.sleep(0.03)

    except sr.UnknownValueError:
        entry_field.insert(ctk.END, " [Didn't catch that]")
    except sr.RequestError:
        entry_field.insert(ctk.END, " [Speech error]")
    except Exception as e:
        entry_field.insert(ctk.END, " [Error]")

    stop_event.set()
    voice_btn.configure(text="🎤 Voice", font=("Consolas", 20, "bold"))


def voice_command():
    """
    Start voice command in a separate thread
    """
    threading.Thread(target=voice_command_thread, daemon=True).start()


# ======================================================
# --------------- GUI Setup --------------------------
# ======================================================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Voice Calculator")

# ---------- Entry Field ----------
entry_field = ctk.CTkEntry(
    root, width=280, height=50,
    font=("Consolas", 28, "bold"),
    justify="right", fg_color="#BBB", text_color="#000"
)
entry_field.grid(row=0, column=0, columnspan=4, pady=10, padx=5)

# ---------- Top Row Buttons: C, Voice, DEL ----------
c_btn = ctk.CTkButton(
    root, text="C", width=60, height=50, font=("Consolas", 20, "bold"),
    fg_color="#db701f", text_color="white", command=lambda: on_button_click("C")
)
c_btn.grid(row=1, column=0, padx=3, pady=3)

voice_btn = ctk.CTkButton(
    root, text="🎤 Voice", width=125, height=50, font=("Consolas", 20, "bold"),
    fg_color="#2c506b", text_color="white", command=voice_command
)
voice_btn.grid(row=1, column=1, columnspan=2, padx=3, pady=3)

del_btn = ctk.CTkButton(
    root, text="DEL", width=60, height=50, font=("Consolas", 20, "bold"),
    fg_color="#db701f", text_color="white", command=lambda: on_button_click("DEL")
)
del_btn.grid(row=1, column=3, padx=3, pady=3)

# ---------- Other Calculator Buttons ----------
buttons = [
    ('x²', 2, 0, "#3C3636"), ('√', 2, 1, "#3C3636"), ('(', 2, 2, "#3C3636"), (')', 2, 3, "#3C3636"),
    ('7', 3, 0, "#3C3636"), ('8', 3, 1, "#3C3636"), ('9', 3, 2, "#3C3636"), ('/', 3, 3, "#000"),
    ('4', 4, 0, "#3C3636"), ('5', 4, 1, "#3C3636"), ('6', 4, 2, "#3C3636"), ('*', 4, 3, "#000"),
    ('1', 5, 0, "#3C3636"), ('2', 5, 1, "#3C3636"), ('3', 5, 2, "#3C3636"), ('-', 5, 3, "#000"),
    ('0', 6, 0, "#3C3636"), ('.', 6, 1, "#3C3636"), ('=', 6, 2, "#000"), ('+', 6, 3, "#000"),
]

for (text, row, col, color) in buttons:
    btn = ctk.CTkButton(
        root, text=text, width=60, height=50, font=("Consolas", 20, "bold"),
        fg_color=color, text_color="white", command=lambda t=text: on_button_click(t)
    )
    btn.grid(row=row, column=col, padx=3, pady=3)

# ---------- Run the App ----------
root.mainloop()
