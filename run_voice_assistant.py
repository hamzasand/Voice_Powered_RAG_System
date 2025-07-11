# voice_assistant/main.py
# Chatbot reply voice to text 
import logging
import time
from colorama import Fore, init
from voice_assistant.audio import record_audio, play_audio
from voice_assistant.transcription import transcribe_audio
from voice_assistant.response_generation import generate_response
from voice_assistant.text_to_speech import text_to_speech
from voice_assistant.utils import delete_file
from voice_assistant.config import Config
from voice_assistant.api_key_manager import get_transcription_api_key, get_response_api_key, get_tts_api_key

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize colorama
init(autoreset=True)

import threading
def main():
    """
    Main function to run the voice assistant.
    """
    chat_history = [
        {"role": "system", "content": """
You are Verbi, a smart and friendly AI voice assistant designed for a Point of Sale (POS) system.

Your main role is to help the user build a purchase list by listening to product names and quantities during a sessionand total bill at the end.

Instructions:
- When the user says "make list", you will enter list-creation mode.
- In list mode, listen for product names and quantities like: "3 Pepsi":"price", "2 chicken burgers":"price", "1 large fries":"price", etc.
- Keep adding items to the list as the user speaks.
- When the user says "stop list", you will finalize the list.

At the end of the session:
- Generate a clean summary of the items and quantities.
- Include a total price using estimated or preset prices for each item.
- Present it like a receipt.

Keep your responses short and clear. Do not explain or ask for confirmation unless something is unclear.
"""
           }
    ]

    while True:
        try:
            # Record audio from the microphone and save it as 'test.wav'
            record_audio(Config.INPUT_AUDIO)

            # Get the API key for transcription
            transcription_api_key = get_transcription_api_key()
            
            # Transcribe the audio file
            user_input = transcribe_audio(Config.TRANSCRIPTION_MODEL, transcription_api_key, Config.INPUT_AUDIO, Config.LOCAL_MODEL_PATH)

            # Check if the transcription is empty and restart the recording if it is. This check will avoid empty requests if vad_filter is used in the fastwhisperapi.
            if not user_input:
                logging.info("No transcription was returned. Starting recording again.")
                continue
            logging.info(Fore.GREEN + "You said: " + user_input + Fore.RESET)

            # Check if the user wants to exit the program
            if "goodbye" in user_input.lower() or "arrivederci" in user_input.lower():
                break

            # Append the user's input to the chat history
            chat_history.append({"role": "user", "content": user_input})

            # Get the API key for response generation
            response_api_key = get_response_api_key()

            # Generate a response
            response_text = generate_response(Config.RESPONSE_MODEL, response_api_key, chat_history, Config.LOCAL_MODEL_PATH)
            logging.info(Fore.CYAN + "Response: " + response_text + Fore.RESET)

            # Append the assistant's response to the chat history
            chat_history.append({"role": "assistant", "content": response_text})

            # Determine the output file format based on the TTS model
            if Config.TTS_MODEL == 'openai' or Config.TTS_MODEL == 'elevenlabs' or Config.TTS_MODEL == 'melotts' or Config.TTS_MODEL == 'cartesia':
                output_file = 'output.mp3'
            else:
                output_file = 'output.wav'

            # Get the API key for TTS
            tts_api_key = get_tts_api_key()

            # Convert the response text to speech and save it to the appropriate file
            text_to_speech(Config.TTS_MODEL, tts_api_key, response_text, output_file, Config.LOCAL_MODEL_PATH)

            # Play the generated speech audio
            if Config.TTS_MODEL=="cartesia":
                pass
            else:
                play_audio(output_file)


        except Exception as e:
            logging.error(Fore.RED + f"An error occurred: {e}" + Fore.RESET)
            delete_file(Config.INPUT_AUDIO)
            if 'output_file' in locals():
                delete_file(output_file)
            time.sleep(1)

if __name__ == "__main__":
    main()
