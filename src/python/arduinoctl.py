import serial
import struct

class ArduinoController:

    def __init__(self, dev_file, baud: int=9600):
        # Open serial port for communication with Arduino, at device file "dev_file"
        self.arduino = serial.Serial(port=dev_file, baudrate=baud, timeout=5)

    def write_freq(self, freq: float) -> int:
        # Python floats are represented as 64-bit double-precision floats, so pack it into 'd' for a C++ double.
        freq_data = struct.pack('d', freq)
        return self.arduino.write(freq_data)
