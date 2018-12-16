import os 
from gpiozero import Motor
from time import sleep
from config import *


motor = Motor(forward = fan.pin)

# Return CPU temperature as a character string                                      
def getCPUtemp():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))


while True:
    temp = getCPUtemp()
    if temp > 45:
        try:
            motor.forward()
        except:
            pass
    else:
        try:
            motor.off()
        except:
            pass