import pyaudio
import matplotlib.pyplot as plt
import numpy as np
import serial
import time
from arduinoctl import ArduinoController as ac

ctl = ac('/dev/tty.usbmodem1461201') # change this port to be your own

# need this delay for arduino initialization
time.sleep(3)

for num in [2.5, 1.5, 1.6, 3.7]:
    print(ctl.write_freq(num))
    time.sleep(1)

ctl.close()