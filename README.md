# 🤖 AI-Powered Personal Assistant - VoiceMate 🗣️

## Overview
Welcome to VoiceMate, your smart and intuitive personal assistant! 🌟 This Python project harnesses the power of AI to assist you with code, answer questions, translate languages, and more.

## Features 🚀
- **Code Assistance:** Get instant help with your code by just asking.
- **Knowledge Queries:** Ask anything, and VoiceMate will fetch informative answers!
- **Language Translation:** Seamlessly translate text into different languages.
- **Note-Taking:** Keep your thoughts organized with VoiceMate's note-taking feature.
- **Calendar Integration:** Schedule events and set reminders effortlessly.

## Project Structure 📁
- **features.py:** Main script with the implementation of exciting features.
- **codeassistance.py:** Code assistance logic powered by the OpenAI API.
- **knowledgequeries.py:** Fetching knowledge using the OpenAI API.
- **languagetranslation.py:** Language translation using the Google Translate API.
- **notetaking.py:** Organize your thoughts with VoiceMate's note-taking functionality.
- **calendarintegration.py:** Seamlessly integrate with your calendar for scheduling.

## Usage 🛠️
1. Create a virtual environment: `python -m venv venv`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure your OpenAI API key and password in `keys.txt`.
4. Run the assistant: `python features.py`

## Configuration ⚙️
- Set your OpenAI API key and password in the `keys.txt` file.
- Customize the wake-up word and authentication mechanism in the `features.py` script.

## Dependencies 🌐
- `openai==0.27.0`
- `googletrans==4.0.0-rc1`
- `SpeechRecognition==3.8.1`

## Author 👩‍💻
Adithian.ps

## License 📜
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
