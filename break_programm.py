import serial

with serial.Serial('/dev/ttyUSB0', 115200, timeout=1) as ser:
    ser.write(0x03)
    print(ser.read())
    ser.close()
