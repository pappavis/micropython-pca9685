### PCA9685 12-bit I2C PWM motor aansturing biblioteek.
Oorspronklike deur <a href="https://github.com/adafruit/micropython-adafruit-pca9685" target="_blank">Adafruit</a>

<img src="https://github.com/pappavis/micropython-pca9685/blob/main/plaatjes/pca9685_breakout.gif?raw=true" width="30%" height="30%">

# Hoe om te gebruik:

1. Download die micropython lib
```bash
macBook$ git pull github.com/pappavis/micropython-pca9685/
```

2. Verbind jouw Micropython apparaat aan jouw computer.
3. Open <a href="https://thonny.org/">Thonny</a> en selecteer die juiste COM-poort (Windows) of /dev/ op Mac & Linux.
4. Maak een root map "lib"
 <img src="https://github.com/pappavis/micropython-pca9685/blob/main/plaatjes/thonny_pad.jpg?raw=true">
5. Upload die lib naar /lib/pca9685 met 'n tool soos <a href="https://github.com/wendlers/mpfshell" target="_blank">mpfshell</a>
6. Test jouw installasie .

```bash
MicroPython v1.13-178-g21c293fbc on 2020-11-16; ESP32 module with ESP32

Type "help()" for more information.
>>> from pca9685.pca9685 import PCA9685
>>> i2c1 = machine.SoftI2C(scl=machine.Pin(22),sda=machine.Pin(21),freq=100000)
>>> pca1 = PCA9685(i2c=i2c1, address=0x40)
>>> 
```
Sien ook die examples/ map vir meer voorbeelde.

# voorbeeld DCMotors

```python
import machine
import sys
import utime
from pca9685.pca9685 import PCA9685
from pca9685.motor import DCMotors

def main():
    i2c1 = ''
    
    if(sys.platform == 'esp8266'):
        i2c1 = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)
    else:
        i2c1 = machine.SoftI2C(scl=machine.Pin(22),sda=machine.Pin(21),freq=100000)

    pca1 = PCA9685(i2c=i2c1, address=0x40)
    moto1 = DCMotors(i2c=i2c1, address=0x40)
    moto1.__DC_MOTORS = [(14, 15)]
    
    moto1.speed(index=0, value=0)
    print("motor afremmen")
    utime.sleep_ms(1200)
    
    spoed1 = 1000    # speed from 0 to 4096
    print("start motor, spoed=",spoed1)
    moto1.speed(index=0, value=spoed1)
    utime.sleep_ms(1200)

print("app START op ", sys.platform)
main()
print("app EIND op ", sys.platform)

```
