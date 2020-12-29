import machine
import sys
import utime
from pca9685.pca9685 import PCA9685
from pca9685.motor import DCMotors

def main():
    i2c1 = ''

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
    moto1 = DCMotors(i2c=i2c1, address=0x40)
    moto1.__DC_MOTORS = [(14, 15)]

    if(1==2):
        moto1.speed(index=0, value=0)
        print("motor afremmen")
        utime.sleep_ms(1200)
        
        spoed1 = 1
        print("start motor, spoed=",spoed1)
        moto1.speed(index=0, value=spoed1)
        utime.sleep_ms(1200)
        
        moto1.speed(index=0, value=0)
        utime.sleep_ms(1200)
        print("motor afremmen")

        print("start motor, achteruit spoed=",spoed1 * -1)
        moto1.speed(index=0, value=spoed1 * -1)
        utime.sleep_ms(1200)

        moto1.speed(index=0, value=0)
        print("motor afremmen")
        utime.sleep_ms(1200)

    if(2==3):
        spoed1 = 4094
        print("start motor, spoed=",spoed1)
        moto1.speed(index=0, value=spoed1)
        utime.sleep_ms(2200)

        moto1.speed(index=0, value=0)
        print("motor stop")
        utime.sleep_ms(1200)

    if(3==3):
        moto1.speed(index=0, value=0)
        print("3, motor afremmen")
        utime.sleep_ms(1900)      
        
        print("Snelheid van 0 tot 4096")
        for snel1 in range(600, 4096, 20):
            print("Snelheid vooruit", snel1)
            moto1.speed(index=0, value=snel1)
            utime.sleep_ms(400)

        utime.sleep_ms(1200)
        print("motor stop")
        moto1.speed(index=0, value=0)
        
        pca1.reset()

print("app START op ", sys.platform)
main()
print("app EIND op ", sys.platform)
