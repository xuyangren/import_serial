import serial
import time
 
ser = serial.Serial("COM5", baudrate=9600, timeout=1)
 
while True:
    # 连续读取串口数据
    data = ser.readline()
    print(data)
 
    # 定时发送指定数据
    time.sleep(10) # 每隔 10 秒发送一次
    ser.write(b"send data")
