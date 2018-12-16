import os 

# Return CPU temperature as a character string                                      
def getCPUtemp():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))


while True:
    temp = getCPUtemp()
    if temp > 45:
        try:
            fan.on()
        except:
            pass
    else:
        try:
            fan.on()
        except:
            pass