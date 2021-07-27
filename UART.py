
from jetcam.csi_camera import CSICamera
import cv2
import numpy as np
import time
import serial
print("OPENCV")
print(cv2.__version__)

cam0 = CSICamera(width=1080, height=720, capture_width=1080, capture_height=720, capture_fps=30) 

def STM(ID, reg, data):
    print("#APB"+ID+reg+data)
    fc_com1.write(b"change\n")

fc_com1 = serial.Serial(
    port="/dev/ttyTHS0",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)
time.sleep(1)
nowTime=time.time()
if(time.time()-nowTime>1):
        #print('waiting')
        nowTime=time.time()
data='wait'
ID='255'
reg='0xqCF'
nowTime=time.time()
clockTime=time.time()

while(True):
    while(data!='start'):#wait until start
        data=input("Please enter a string:\n")
        if(data=='start'):
            STM(ID,reg,data)
            nowTime=time.time()

    if fc_com1.inWaiting() > 0 :#receiver
        messege = fc_com1.readline() 
        print(messege)

    if(time.time()-clockTime>1):#transmitter
        fc_com1.write(b"change\n")
        clockTime=time.time()

    if cv2.waitKey(1)==ord('q'):#q or 10sec end the process
        break
    if(time.time()-nowTime>10):
        break
        nowTime=time.time()

    image0 = cam0.read()
    cv2.imshow("Dialation Image",image0)
fc_com1.close()
cv2.destoryAllWindows()