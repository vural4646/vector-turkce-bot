import sounddevice as sd
import vosk
import json
import os

model = vosk.Model("model/vosk-model-small-tr-0.3")
recognizer = vosk.KaldiRecognizer(model, 16000)

def listen_trigger():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Vector tetikleyici dinliyor...")
        while True:
            sd.sleep(1000)

def callback(indata, frames, time, status):
    if recognizer.AcceptWaveform(indata.tobytes()):
        result = recognizer.Result()
        if "vector" in result.lower():
            print("Vector tetiklendi!")
            os.system("python3 pretrained_bot.py")


listen_trigger()
