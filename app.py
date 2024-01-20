import openai
from googletrans import Translator
from notetaking import NoteManager
from calendarintegration import CalendarManager
from auth import authenticate_user

note_manager = NoteManager()
calendar_manager = CalendarManager()

WAKE_UP_WORD = "assistant"

def read_keys():
    try:
        with open("keys.txt", "r") as file:
            api_key = file.readline().strip()
            password = file.readline().strip()
            return api_key, password
    except FileNotFoundError:
        print("Error: keys.txt not found.")
        exit()

API_KEY, PASSWORD = read_keys()

def provide_code_assistance(query):
    openai.api_key = API_KEY

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Assist me with the following code:\n{query}",
        temperature=0.7,
        max_tokens=150
    )

    return response.choices[0].text.strip()

def answer_knowledge_query(query):
    openai.api_key = API_KEY

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Answer the following question:\n{query}",
        temperature=0.7,
        max_tokens=150
    )

    return response.choices[0].text.strip()

def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def generate_response(prompt):
    openai.api_key = API_KEY

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )

    return response.choices[0].text.strip()

def set_reminder(task, date):
    calendar_manager.schedule_event(task, date)
    return f"Reminder set for: {task} on {date}."

def authenticate_and_process(command):
    if not command.startswith(WAKE_UP_WORD):
        return "Wake up word not detected."

    authenticated = authenticate_user(PASSWORD)
    if not authenticated:
        return "Authentication failed. Access denied."

    actual_command = command[len(WAKE_UP_WORD):].strip()
    return process_feature_request(actual_command)

def process_feature_request(command):
    if "code assistance" in command:
        return provide_code_assistance(command)
    elif "knowledge query" in command:
        return answer_knowledge_query(command)
    elif "translate" in command:
        # Assuming the command is in the format "Translate <text> to <language>"
        text_to_translate = command.split("Translate ")[1].split(" to ")[0]
        target_language = command.split(" to ")[1]
        return translate_text(text_to_translate, target_language)
    elif "generate response" in command:
        prompt = command.split("Generate response for: ")[1]
        return generate_response(prompt)
    elif "take a note" in command:
        category = command.split("in ")[1].split(":")[0]
        note = command.split(": ")[1]
        note_manager.add_note(category, note)
        return f"Note added to {category}: {note}"
    elif "schedule event" in command:
        task = command.split("for ")[1].split(" on ")[0]
        date = command.split(" on ")[1]
        return set_reminder(task, date)
    else:
        return "Sorry, I couldn't understand that request."

# Example usage:
user_command = "assistant Generate response for: Tell me a joke."
response = authenticate_and_process(user_command)
print(response)
