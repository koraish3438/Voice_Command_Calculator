# 🧮 Voice_Command_Calculator
A Python-based Voice Calculator with CustomTkinter UI, supporting both manual input and Bangla/English voice commands.


=========================== 📌 Description (English) =============================

A Voice Calculator built with Python and CustomTkinter.
This calculator supports both manual input and voice commands (Bangla & English).

Features include:

Basic arithmetic operations (+, -, ×, ÷)

Power and square root (x², √)

Voice recognition using Google Speech Recognition

Smooth UI with CustomTkinter

======================📌 Description (Bangla)======================

এটি একটি ভয়েস ক্যালকুলেটর যা Python এবং CustomTkinter ব্যবহার করে তৈরি করা হয়েছে।
এতে আপনি কীবোর্ডে সংখ্যা লিখে বা ভয়েস কমান্ড (বাংলা ও ইংরেজি) দিয়ে হিসাব করতে পারবেন।

ফিচারসমূহ:

যোগ, বিয়োগ, গুণ, ভাগ

ঘাত (x²) ও বর্গমূল (√)

গুগল Speech Recognition দিয়ে ভয়েস কমান্ড

সুন্দর UI (CustomTkinter)

=================⚙️ Project Requirements=================

এই প্রজেক্ট রান করার জন্য প্রয়োজন হবে:

Python (3.10 or above recommended)

customtkinter library

speechrecognition library

pyaudio (for microphone input)

googletrans (if you want translation support)

Install dependencies
pip install customtkinter speechrecognition pyaudio googletrans==4.0.0-rc1

================🧑‍💻 Code Explanation==================

UI Part (CustomTkinter):

A modern styled calculator window তৈরি করা হয়েছে।

Number buttons, operators, এবং display box যুক্ত আছে।

Voice Recognition:

speech_recognition ব্যবহার করে মাইক্রোফোন থেকে ইনপুট নেয়।

Google Speech Recognition API ব্যবহার করে ইনপুটকে Bangla/English text এ রূপান্তর করে।

Calculation Logic:

User input (manual/voice) → expression parse করে → result দেখায়।

Error হলে “Invalid Input” মেসেজ দেখায়।

Special Functions:

x² (power) এবং √ (square root) এর জন্য আলাদা ফাংশন তৈরি আছে।

=================🔄 How It Works====================

Run the program → Calculator UI open হবে।

আপনি চাইলে কীবোর্ড দিয়ে manual input দিতে পারবেন।

অথবা “🎤 Voice Command” বাটন প্রেস করলে মাইক্রোফোন চালু হবে →

বাংলায় বললে (যেমন: "দুই যোগ দুই") → Result: 4

ইংরেজিতে বললে (যেমন: "five multiply three") → Result: 15

=================📖 Usage Instructions (Manual)==================

Manual Input:

Number এবং Operator বোতাম ব্যবহার করে হিসাব দিন।

Example: 12 + 8 = 20

Voice Input:

Voice বাটনে ক্লিক করুন।

পরিষ্কারভাবে বাংলায় বা ইংরেজিতে সংখ্যাগুলো বলুন।

Result display তে দেখাবে।

Special Functions:

x² → Number squared করবে।

√ → Square root বের করবে।

=====================🎤 Presentation Info==============================

Project Title & My Credit

Instructor’s Name

Project Explanation (Bangla)

Code & Features Overview

Demo Screenshots

Conclusion & Future Scope


✍️ Developed by: Koraish