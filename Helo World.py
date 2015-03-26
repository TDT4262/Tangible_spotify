import serial

port = serial.Serial("portnavn",9600)

def read():
    if (port.inWaiting() > 0):
        line = port.readline()
        return line
    else: return ""
    
data = read()
print(data)