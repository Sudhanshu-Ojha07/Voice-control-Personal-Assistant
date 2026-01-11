from voice_io import take_commands, speak
from llm.gemini_client import ask_gemini

EXIT_WORDS = ["exit", "stop", "sleep"]

def start_llm_mode():
    speak("LLM mode activated.")

    while True:
        user_input, _ = take_commands()

        if user_input == "None":
            continue

        if any(word in user_input.lower() for word in EXIT_WORDS):
            speak("Exiting LLM mode.")
            break

        response = ask_gemini(f"Answer in plain spoken English, no markdown:\n{user_input}")
        print("Gemini:", response)
        speak(response)
