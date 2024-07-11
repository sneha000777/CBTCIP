import sounddevice as sd
import wavio
import numpy as np
import time

duration = 30
sampling_rate = 44100
amplification_factor = 2.5

print("You have 30 seconds to record your audio.")
print("Recording...")
audio = sd.rec(int(duration * sampling_rate), samplerate=sampling_rate, channels=2, dtype='int16')
sd.wait()
print("Recording completed successfully.")

amplified = audio * amplification_factor
amplified = np.clip(amplified, -32768, 32767).astype('int16')

print("Playing back the amplified audio...")
sd.play(amplified, sampling_rate)
sd.wait()
print("Audio Playback completed successfully.")

output_filename = "result.wav"
wavio.write(output_filename, amplified, sampling_rate, sampwidth=2)
print(f"Audio saved as file named : {output_filename}")
