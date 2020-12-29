import pca9685.pca9685

class DCMotors:    
    def __init__(self, i2c, address=0x60, freq=1600):
        self.__DC_MOTORS = ((9, 10), (12, 11), (3, 4), (6, 5))    
        self.pca9685 = pca9685.pca9685.PCA9685(i2c, address)
        self.pca9685.freq(freq)

    def _pin(self, pin, value=None):
        if value is None:
            return bool(self.pca9685.pwm(pin)[0])
        if value:
            self.pca9685.pwm(pin, 4096, 0)
        else:
            self.pca9685.pwm(pin, 0, 0)

    def speed(self, index, value=None):
        in2, in1 = self.__DC_MOTORS[index]
        inToUse1 = -1
        if value is None:
            value = self.pca9685.duty(pwm)
            if self._pin(in2) and not self._pin(in1):
                value = -value
            return value
        if value > 0:
            # Forward
            self._pin(in2, False)
            self._pin(in1, True)
            inToUse1 = in1
        elif value < 0:
            # Backward
            self._pin(in1, False)
            self._pin(in2, True)
            inToUse1 = in2
        else:
            # Release
            self._pin(in1, False)
            self._pin(in2, False)
        self.pca9685.duty(inToUse1, abs(value))

    def brake(self, index):
        in2, in1 = self.__DC_MOTORS[index]
        self._pin(in1, True)
        self._pin(in2, True)
        self.pca9685.duty(in1, 0)
        self.pca9685.duty(in2, 0)


