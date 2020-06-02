import pyaudio
import numpy as np
from arduinoctl import ArduinoController as ac
from scipy.signal import find_peaks

class Detector:

    def __init__(self, dev_file, baud=9600, chunk_size=4096*4,
                 rate=44100, max_guitar_freq=500):
        self.arduino = ac(dev_file, baud=baud)
        self.chunk = chunk_size
        self.rate = rate
        self.max_guitar_freq = max_guitar_freq
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,channels=1,rate=self.rate,input=True,
              frames_per_buffer=self.chunk)

    # Reads audio from the computer, then extracts the most prevalent frequency
    # and writes it to the arduino. Returns that frequency.
    def sample(self) -> float:
        data = np.fromstring(self.stream.read(self.chunk), dtype=np.int16)
        fourier = np.fft.fft(data)

        # max_ind = np.argmax(np.abs(fourier[:int(self.max_guitar_freq * self.chunk / self.rate)]))
        graph = np.abs(fourier[:int(self.max_guitar_freq * self.chunk / self.rate)])
        peaks, _ = find_peaks(graph, prominence=.5 * (np.max(graph) - np.min(graph)))
        # print(peaks)
        max_ind = peaks[0]
        max_freq = max_ind * self.rate / self.chunk

        self.arduino.write_freq(max_freq)

        return max_freq

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.arduino.close()


### Original code from here down ###
"""

CHUNK = 4096* 4 # # data points
RATE = 44100 # (Hz)

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) #uses default input device

# SIGINT handler to cleanly close on ctrl-C
def close_stream(sig_num, frame):
    stream.stop_stream()
    stream.close()
    p.terminate()
    exit(0)

signal.signal(signal.SIGINT, close_stream)

max_guitar_freq = 500 # 500 is higher than all guitar strings so ignore anything above it
# peaks = []

print("Recording ...")

while True:
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    fourier = np.fft.fft(data)
    
    max_ind = np.argmax(np.abs(fourier[:int(max_guitar_freq * CHUNK / RATE)]))
    max_freq = max_ind * RATE / CHUNK
    print("peak: " + str(max_freq))
#     peaks.append(max_freq)

# plt.plot(np.arange(100), peaks)

# plt.plot(np.arange(100), peaks)

# plt.plot(np.arange(CHUNK), data)
# frequencies = np.arange(CHUNK) * RATE / CHUNK
# fourier = np.fft.fft(data)
# plt.figure()
# plt.plot(frequencies, np.abs(fourier))
# plt.xlim(0, 500)
"""
