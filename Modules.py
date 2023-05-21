import sounddevice as sd
from scipy.io.wavfile import write
import winsound

def record_audio(freq, duration, file_name):
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()

    write(f"{file_name}.wav", freq, recording)

def play_audio(file_name):
    winsound.PlaySound(file_name, winsound.SND_FILENAME)