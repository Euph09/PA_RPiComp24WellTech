import time
import board
import adafruit_dht

#Set up DHT11 sensor
sensor = adafruit_dht.DHT11(board.D17, use_pulseio=False)

def Measure():
    try:
        # Print the values to the serial port
        temperature = sensor.temperature
        humidity = sensor.humidity
        print("({0:0.1f},{1:0.1f})".format(temperature,humidity))

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
    except Exception as error:
        sensor.exit()
        raise error
    
Measure()
