import machine
import time
from machine import Timer
from machine import Pin

# 0 - close
# 1 - open
# 2 - closing
# 3 - opened
# 4 - error

PWM_CLOSE = 40
PWM_OPEN = 115
ADC_ALARM = 700
TIME_END = 500


class Valve:
    def __init__(self, p_close, p_open, p_button, p_control, p_out):
        self.pwm = None
        self.tmr = None
        self.p_close = machine.Pin(p_close, machine.Pin.IN, machine.Pin.PULL_UP)
        self.p_open = machine.Pin(p_open, machine.Pin.IN, machine.Pin.PULL_UP)
        self.p_button = machine.Pin(p_button, machine.Pin.IN, machine.Pin.PULL_UP)
        self.p_control = machine.Pin(p_control, machine.Pin.OUT)
        self.p_out = p_out
        self.p_adc = machine.ADC(0)
        self.status = 0
        if self.p_close.value():
            self.status = 0
        if self.p_open.value():
            self.status = 1
        if self.p_open.value() ^ self.p_close.value():
            self.status = 4
        self.p_button.irq(trigger=Pin.IRQ_FALLING, handler=self._button)
        self.p_close.irq(trigger=Pin.IRQ_FALLING, handler=self._endswitch())
        self.p_open.irq(trigger=Pin.IRQ_FALLING, handler=self._endswitch())

    def close(self):
        if self.status == 1:
            self.pwm = machine.PWM(machine.Pin(self.p_out), freq=50)
            self.pwm.duty(PWM_CLOSE)
            time.sleep_ms(100)
            self.p_control.on()
            self.status = 2
            self.tmr = Timer(-1)
            self.tmr.init(period=1500, mode=Timer.ONE_SHOT, callback=self._timer_valve_control())

    def open(self):
        if self.status == 0:
            self.pwm = machine.PWM(machine.Pin(self.p_out), freq=50)
            self.pwm.duty(PWM_OPEN)
            time.sleep_ms(100)
            self.p_control.on()
            self.status = 3
            self.tmr = Timer(-1)
            self.tmr.init(period=1500, mode=Timer.ONE_SHOT, callback=self._timer_valve_control())

    def get_status(self):
        if self.status == 2 or self.status == 3:
            if self.p_adc.read() > ADC_ALARM:
                self._reset_out()
                self.status = 4
        if self.status == 2 and not self.p_close.value() and self.p_open.value():
            self.status = 0
        if self.status == 3 and self.p_close.value() and not self.p_open.value():
            self.status = 1
        return self.p_adc.read(), self.status

    def reset_error(self):
        self.status = 1
        self.close()

    def _timer_valve_control(self):
        if (self.status == 2 or self.status == 3) and (self.p_open.value() ^ self.p_close.value()):
            self._reset_out()
            self.status = 4

    def _reset_out(self):
        self.p_control.off()
        if self.pwm is not None:
            self.pwm.deinit()
        if self.tmr is not None:
            self.tmr.deinit()

    def _button(self):
        if self.status == 4:
            self.reset_error()
        if self.status == 0:
            self.open()
        if self.status == 1:
            self.close()
        time.sleep_us(100)

    def _endswitch(self):
        time.sleep_ms(TIME_END)
        self._reset_out()
        if self.status == 2 and not self.p_close.value():
            self.status = 0
            return
        if self.status == 3 and not self.p_open.value():
            self.status = 1
            return
        self.status = 4
