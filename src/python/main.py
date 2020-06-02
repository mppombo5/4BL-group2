import os
import argparse as ap
import time
from arduinoctl import ArduinoController as ac
from detect import Detector

def main():
    parser = ap.ArgumentParser(description="Arguments to use in data collection and Arduino communication.")
    parser.add_argument("port", help="The serial port file to use.")
    args = parser.parse_args()

    serial_port = args.port
    if not os.path.exists(serial_port):
        print("Error: file '{}' does not exist or is not a file.".format(serial_port))
        exit(1)

    # William's test driver code, but with the serial port as a command line arg.
    # ctl = ac(serial_port)

    # need this delay for arduino initialization
    time.sleep(3)

    print('Starting detection...')
    detector = Detector(serial_port)
    while True:
        try:
            print('writing: ' + str(detector.sample()))
        except Exception as e:
            print(e)
            print('Breaking')
            detector.close()
            break

    # for num in [2.5, 1.5, 1.6, 3.7]:
    #     print(ctl.write_freq(num))
    #     time.sleep(1)

    # ctl.close()


if __name__ == "__main__":
    main()
