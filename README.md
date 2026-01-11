🎙️ Voice-Controlled Personal Assistant with LLM Mode 🤖✨

A Python-based voice-controlled personal assistant that listens continuously, understands spoken commands, performs system-level tasks, and can switch into an AI-powered LLM Mode for intelligent conversations using Google Gemini (Flash).

This project is designed to help understand real-world voice assistant architecture, including speech recognition, NLP, system automation, and LLM integration.

🚀 Features
🗣️ Voice Command Mode

Continuous microphone listening

Speech-to-text using Google Speech Recognition

Tokenization and keyword extraction using NLTK

Executes system and utility commands like:

⏰ Time & 📅 Date

🔋 Battery status

🌐 Internet connectivity check

🖥️ Open terminal

🌍 Open websites (YouTube, etc.)

🧠 NEW: LLM Mode (Intelligent Mode)

Activated using the wake word:

"wake"

Once activated:

The assistant enters LLM Mode

Listens to your voice continuously

Sends your spoken query to Gemini Flash (free-tier LLM)

Reads back the AI-generated response

Automatically returns to listening for the next command

✨ This mode enables natural language conversations, explanations, and general Q&A.

🧩 Project Architecture
voice assistant/
│
├── Assemble.py              # Main controller (entry point)
│
├── voice_io.py              # Speech input (STT) and output (TTS)
│
├── llm/
│   ├── llm_mode.py          # Handles LLM interaction loop
│   └── gemini_client.py     # Gemini Flash API integration
│
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation

🧠 How LLM Mode Works

Assistant continuously listens for voice commands

When the user says "wake":

Control switches to LLM Mode

User speaks naturally

Voice input → Text → Gemini Flash API

AI-generated response:

Printed in terminal

Spoken aloud via TTS

Assistant returns to command listening mode

🔄 This creates a seamless hybrid voice assistant + AI chatbot experience.

🛠️ Technologies Used

Python

SpeechRecognition

gTTS / mpg321 (fast voice playback)

NLTK (tokenization & NLP)

Google Gemini Flash (LLM)

Subprocess & OS modules

Linux (Ubuntu)

⚡ Performance Optimizations

Fast audio playback using ffmpeg + mpg321

Sentence-based speech output for long LLM responses

Reduced microphone latency for quicker recognition

Cleaned LLM responses before TTS

Installation Guide:
    1.git clone https://github.com/your-username/Voice-control-Personal-Assistant.git
    2.cd Voice-control-Personal-Assistant
    3.pip install -r requirements.txt

    4.set your Gemini API key in config.py
    5.Run the assistant: python3 Assemble.py
