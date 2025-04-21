JARVIS - Virtual AI Desktop Assistant 🧠🎙️
Jarvis is your personal voice-activated AI desktop assistant built with Python. It can perform a wide range of tasks — from playing music and browsing the web to opening apps, taking dictation, solving math problems, and more — all using simple voice commands.

🚀 Features
🔊 Wake word activation ("Jarvis")

🎵 Play songs on YouTube and YouTube Music

🧮 Voice-powered calculator (using system calculator)

📝 Dictation in Notepad with voice input

🌐 Google Search

📖 Wikipedia Q&A

🖥️ Open/Close desktop apps:

Notepad

Paint

Command Prompt

Control Panel

File Explorer

Microsoft Word/Excel

Calculator

Visual Studio Code

Burnout Paradise (example game)

🔔 Beep indicator before recording

🧠 Natural voice responses

📦 Dependencies
Make sure the following Python packages are installed:

bash
Copy
Edit
pip install speechrecognition
pip install pyttsx3
pip install pywhatkit
pip install wikipedia
pip install pyautogui
pip install pygame
pip install pygetwindow
Also ensure you have:

beep.wav file in your working directory

Python installed on your system (Python 3.7+ recommended)

Windows OS (as it uses os.system for Windows apps)

🛠️ How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/rishishankar-03/JARVIS_Virtual_AI_Desktop_Assisstant.git
cd JARVIS_Virtual_AI_Desktop_Assisstant
Run the script:

bash
Copy
Edit
python jarvis.py
Say "Jarvis" to activate, then speak your command after the prompt.

🧠 Example Commands
"Jarvis, play faded on YouTube"

"Jarvis, play happier on YouTube Music"

"Jarvis, what is the capital of France?"

"Jarvis, open notepad"

"Jarvis, write in notepad"

"Jarvis, calculate 45 multiplied by 9"

"Jarvis, close calculator"

"Jarvis, open burnout paradise"

"Jarvis, close code app"

"Jarvis, what is machine learning?"

📝 Notes
Some features are tightly coupled with Windows OS (e.g., taskkill, start, app names).

You can customize the path for specific software (e.g., games) in the script.

You can improve accuracy by training on custom keywords or integrating more advanced NLP.

🙌 Author
Rishi Shankar
GitHub: rishishankar-03

