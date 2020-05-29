import serial
import struct

class ArduinoController:

    def __init__(self, dev_file, baud: int=9600):
        # Open serial port for communication with Arduino, at device file "dev_file"
        self.arduino = serial.Serial(port=dev_file, baudrate=baud, timeout=5)

    def write_freq(self, freq: float) -> int:
        # Arduino's Serial.read returns an integer, so we need to turn the floating point frequency into an integer.
        # We multiply the frequency by 10 and truncate the decimal points.
        freq = str(int(freq * 10)) + '\n'

        return self.arduino.write(freq.encode('utf-8'))

    def read(self):
        return self.arduino.read()

    def close(self):
        # Simply closes the Serial port connection, probably to used in a SIGINT handler.
        self.arduino.close()
        return