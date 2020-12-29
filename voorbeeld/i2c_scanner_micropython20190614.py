# Scanner i2c en MicroPython | MicroPython i2c scanner
# Renvoi l'adresse en decimal et hexa de chaque device connecte sur le bus i2c
# Return decimal and hexa adress of each i2c device
# https://projetsdiy.fr - https://diyprojects.io (dec. 2017)
 
import machine
import sys
i2c = ''


wemosPinsDict8266 = {"TX":1, "RX":3,"D4":2, "D3":0, "D2":4, "D1":5, "RX":3, "TX":1, "D8":15, "D7":13, "D6":12, "D5":14, "D0":16, "SCL":5, "SDA":4}
wemosSPI8266 = {"MISO":wemosPinsDict8266["D6"], "MOSI":wemosPinsDict8266["D7"], "SCK":wemosPinsDict8266["D5"], "CSN":wemosPinsDict8266["D4"], "CE":wemosPinsDict8266["D3"]}

wemosPinsESP32 = {"TX":1, "RX":3,"D4":2, "D3":0, "D2":4, "D1":5, "RX":3, "TX":1, "SCL":22, "SDA":21, "MISO":19, "MOSI":23, "SCK":18, "A0VP":36, "A3VN":39, "A4":32, "A5":33, "A6":34, "DAC1":25, "DAC2":26, "A17":14, "A15":12, "A14":13}


if(sys.platform == 'esp8266'):
    i2c1 = machine.I2C(scl=machine.Pin(wemosPinsDict8266["SDA"]), sda=machine.Pin(wemosPinsDict8266["SCL"]), freq=100000)
    #i2c1 = machine.I2C(scl=machine.Pin(wemosPinsDict8266["SCL"]),sda=machine.Pin(wemosPinsDict8266["SDA"]),freq=100000)
else:
    #i2c1 = machine.SoftI2C(scl=machine.Pin(19),sda=machine.Pin(22),freq=100000)
    i2c1 = machine.SoftI2C(scl=machine.Pin(wemosPinsESP32["SCL"]),sda=machine.Pin(wemosPinsESP32["SDA"]),freq=100000)

print(sys.platform, 'Scan i2c bus...')
devices = i2c1.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

print("Lijst I2C addressen:", [hex(device_address)
for device_address in i2c1.scan()])


print("Eind app")
