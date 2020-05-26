import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import os

CHUNK = 4096* 4 # # data points
RATE = 44100 # (Hz)

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) #uses default input device

max_guitar_freq = 500 # 500 is higher than all guitar strings so ignore anything above it
# peaks = []
while True:
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    fourier = np.fft.fft(data)
    
    max_ind = np.argmax(np.abs(fourier[:int(max_guitar_freq * CHUNK / RATE)]))
    max_freq = max_ind * RATE / CHUNK
    print("peak: " + str(max_freq))
#     peaks.append(max_freq)


stream.stop_stream()
stream.close()
p.terminate()

# plt.plot(np.arange(100), peaks)

# plt.plot(np.arange(100), peaks)

# plt.plot(np.arange(CHUNK), data)
# frequencies = np.arange(CHUNK) * RATE / CHUNK
# fourier = np.fft.fft(data)
# plt.figure()
# plt.plot(frequencies, np.abs(fourier))
# plt.xlim(0, 500)
