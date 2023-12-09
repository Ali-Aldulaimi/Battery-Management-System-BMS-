import serial
import time
from datetime import datetime

def initialize_serial():
    ser = serial.Serial('/dev/ttyACM0', 115200)
    ser.flushInput()
    time.sleep(0.1)
    return ser

def extract_and_convert(frame):
    bytes_to_convert = frame[3:5]
    decimal_value = int.from_bytes(bytes_to_convert, byteorder='big')
    return decimal_value / 10

def send_request_frame(ser, request_frame):
    ser.write(request_frame)
    response_frame = ser.read(7)
    decimal_value = extract_and_convert(response_frame)
    return decimal_value
