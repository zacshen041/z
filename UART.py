
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

fc_com1 = serial.Serial(
    port="/dev/ttyTHS0",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)
time.sleep(1)
ID='255'
reg='0xqCF'
nowTime=time.time()
while(True):
    
    if(time.time()-nowTime>1):
        #print('waiting')
        nowTime=time.time()
    if cv2.waitKey(1)==ord('i'):
        data=input("Please enter a string:\n")
        STM(ID,reg,data)
    if cv2.waitKey(1)==ord('q'):
        break

fc_com1.close()