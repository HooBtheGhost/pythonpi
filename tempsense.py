import RPi.GPIO as GPIO
import time 
import requests
import Freenove_DHT as DHT
DHTPin = 11  # define the pin of DHT11

def loop():
    dht = DHT.DHT(DHTPin)  # create a DHT class object
    counts = 0  # Measurement counts
    while(True):
        # Get temperature reading...
        for i in range(0, 15):
            chk = dht.readDHT11()  # read DHT11 and get a return value...
            if (chk is dht.DHTLIB_OK):  # ... then determine whether data read is normal according to the return value.
                # print("DHT11,OK!")
                break
            time.sleep(0.1)
        
        # ...and increment the counter if it's over 25°C
        if (dht.temperature >= 25):
            counts += 1
        elif (counts > 0):
            counts += -1

        #print(dht.temperature)
        #print(counts)

        # Check if the temperature measurement has been above 25°C for at least 15 times
        if (counts >= 15):
            requests.post('https://maker.ifttt.com/trigger/temphook/with/key/dQrwW7T1NE_i0aiJDVYqTJ')
            counts = 0

        # Sleep 2 seconds before getting next reading
        time.sleep(2)

if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()


