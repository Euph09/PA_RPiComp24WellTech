import serial, time

#Access input from PM sensor, which is USB
ser = serial.Serial('/dev/ttyUSB0')

#Read binary stream from sensor
data = []
for index in range(0,10):
    datum = ser.read()
    data.append(datum)

#Read values of the two pollutants and output it
pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder = 'little')/10
pmten = int.from_bytes(b''.join(data[4:6]), byteorder = 'little')/10
print('('+str(pmtwofive)+','+str(pmten)+')')
