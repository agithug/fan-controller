import os 

# Return CPU temperature as a character string                                      
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))


while True:
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