#  Voice Powered RAG System 🎙️
## Motivation ✨✨✨

Welcome to the Voice Powered RAG system! 🎙️ Our goal is to create a modular voice assistant application that allows you to experiment with state-of-the-art (SOTA) models for various components. The modular structure provides flexibility, enabling you to pick and choose between different SOTA models for transcription, response generation, and text-to-speech (TTS). This approach facilitates easy testing and comparison of different models, making it an ideal platform for research and development in voice assistant technologies. Whether you're a developer, researcher, or enthusiast, this project is for you!

## Features 🧰

- **Modular Design**: Easily switch between different models for transcription, response generation, and TTS.
- **Support for Multiple APIs**: Integrates with OpenAI, Groq, and Deepgram APIs, along with placeholders for local models.
- **Audio Recording and Playback**: Record audio from the microphone and play generated speech.
- **Configuration Management**: Centralized configuration in `config.py` for easy setup and management.

## Project Structure 📂

```plaintext
voice_assistant/
├── voice_assistant/
│   ├── __init__.py
│   ├── audio.py
│   ├── api_key_manager.py
│   ├── config.py
│   ├── transcription.py
│   ├── response_generation.py
│   ├── text_to_speech.py
│   ├── utils.py
│   ├── local_tts_api.py
│   ├── local_tts_generation.py
├── .env
├── run_voice_assistant.py
├── piper_server.py
├── setup.py
├── requirements.txt
└── README.md
```

## Setup Instructions  📋

#### Prerequisites ✅

- Python 3.10 or higher
- Virtual environment (recommended)

#### Step-by-Step Instructions 🔢

1. 📥 **Clone the repository**

```shell
   git clone https://github.com/PromtEngineer/Verbi.git
   cd Verbi
```
2. 🐍 **Set up a virtual environment**

  Using `venv`:

```shell
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
  Using `conda`:

```shell
    conda create --name verbi python=3.10
    conda activate verbi
```
3.  📦 **Install the required packages**

```shell
   pip install -r requirements.txt
```
4. 🛠️ **Set up the environment variables**

Create a  `.env` file in the root directory and add your API keys:
```shell
    OPENAI_API_KEY=your_openai_api_key
    GROQ_API_KEY=your_groq_api_key
    DEEPGRAM_API_KEY=your_deepgram_api_key
    LOCAL_MODEL_PATH=path/to/local/model
    PIPER_SERVER_URL=server_url
```
5. 🧩 **Configure the models**

Edit config.py to select the models you want to use:

```shell
    class Config:
        # Model selection
        TRANSCRIPTION_MODEL = 'groq'  # Options: 'openai', 'groq', 'deepgram', 'fastwhisperapi' 'local'
        RESPONSE_MODEL = 'groq'       # Options: 'openai', 'groq', 'ollama', 'local'
        TTS_MODEL = 'deepgram'        # Options: 'openai', 'deepgram', 'elevenlabs', 'local', 'melotts', 'piper'

        # API keys and paths
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
        LOCAL_MODEL_PATH = os.getenv("LOCAL_MODEL_PATH")
```
7. 🏃 **Run the voice assistant**

```shell
   python run_voice_assistant.py
```


