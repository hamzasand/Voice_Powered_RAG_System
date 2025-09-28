# Voice_Assistant/audio.py
import sounddevice as sd
import soundfile as sf
from pydub import AudioSegment
import pygame
import time
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Here set the duuration of listining of model via mic as duration=15 seconds which can be increse and decrease
def record_audio(file_path_mp3, duration=15, samplerate=22050, channels=1):
    """
    Record audio from the microphone using sounddevice and save it as an MP3 file.
    
    Args:
    file_path_mp3 (str): Path to save the MP3 audio file.
    duration (int): Duration to record in seconds.
    samplerate (int): Sample rate of the audio.
    channels (int): Number of input channels (1 = mono, 2 = stereo).
    """
    try:
        logging.info("Recording started...")
        recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
        sd.wait()
        logging.info("Recording complete.")
        # Save as temporary WAV first
        wav_path = "temp_recording.wav"
        sf.write(wav_path, recording, samplerate)
        # Convert to MP3 using pydub
        audio = AudioSegment.from_wav(wav_path)
        audio.export(file_path_mp3, format="mp3", bitrate="128k", parameters=["-ar", str(samplerate), "-ac", str(channels)])
        os.remove(wav_path)
        logging.info(f"Audio saved as {file_path_mp3}")
    except Exception as e:
        logging.error(f"Recording failed: {e}")

def play_audio(file_path):
    """
    Play an audio file using pygame.
    
    Args:
    file_path (str): The path to the audio file to play.
    """
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)
    except pygame.error as e:
        logging.error(f"Failed to play audio: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred while playing audio: {e}")
    finally:
        pygame.mixer.quit()
