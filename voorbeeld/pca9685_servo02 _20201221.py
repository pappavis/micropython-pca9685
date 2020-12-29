import machine
from pca9685.pca9685 import PCA9685
from pca9685.servo import Servos
import utime
import sys

def main():
    wemosPinsDict8266 = {"TX":1, "RX":3,"D4":2, "D3":0, "D2":4, "D1":5, "RX":3, "TX":1, "D8":15, "D7":13, "D6":12, "D5":14, "D0":16, "SCL":5, "SDA":4}
    wemosSPI8266 = {"MISO":wemosPinsDict8266["D6"], "MOSI":wemosPinsDict8266["D7"], "SCK":wemosPinsDict8266["D5"], "CSN":wemosPinsDict8266["D4"], "CE":wemosPinsDict8266["D3"]}

    wemosPinsESP32 = {"TX":1, "RX":3,"D4":2, "D3":0, "D2":4, "D1":5, "RX":3, "TX":1, "SCL":22, "SDA":21, "MISO":19, "MOSI":23, "SCK":18, "A0VP":36, "A3VN":39, "A4":32, "A5":33, "A6":34, "DAC1":25, "DAC2":26, "A17":14, "A15":12, "A14":13}


    if(sys.platform == 'esp8266'):
        i2c1 = machine.I2C(scl=machine.Pin(wemosPinsDict8266["SDA"]), sda=machine.Pin(wemosPinsDict8266["SCL"]), freq=100000)
        #i2c1 = machine.I2C(scl=machine.Pin(wemosPinsDict8266["SCL"]),sda=machine.Pin(wemosPinsDict8266["SDA"]),freq=100000)
    else:
        #i2c1 = machine.SoftI2C(scl=machine.Pin(19),sda=machine.Pin(22),freq=100000)
        i2c1 = machine.SoftI2C(scl=machine.Pin(wemosPinsESP32["SCL"]),sda=machine.Pin(wemosPinsESP32["SDA"]),freq=100000)


    pca1 = PCA9685(i2c=i2c1, address=0x40)
    pcaServo = Servos(i2c=i2c1, address=0x40)
    pinServ1 = 13

    if(1==1):        
        #pca1.freq(freq=50)
        #pca1.pwm(index=pinServ1, on=True, off=False)
        pcaServo.position(index=pinServ1, degrees=0)
        print("Servo naar 0 graden.")
        utime.sleep_ms(300)
        
        for tel1 in range(1, 4):
            for deg1 in range(0, 200, 1):
                print(tel1, "\t", deg1, "\t pin=", pinServ1, "\t graden=", deg1)
                pcaServo.position(index=pinServ1, degrees=deg1)
                utime.sleep_ms(10)

            utime.sleep_ms(200)
            pcaServo.position(index=pinServ1, degrees=0)


    utime.sleep_ms(1500)
    print("")
    print("Servo naar 0 graden.")
    pcaServo.position(index=pinServ1, degrees=-10)
    utime.sleep_ms(300)
    
    pca1.reset()
    pcaServo.release(index=pinServ1)


print("Start app", sys.platform)
main()
print("Eind app", sys.platform)
