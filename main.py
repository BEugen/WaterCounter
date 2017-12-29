import time
import machine
import config
import temperature
import screen

_SCREEN_REFRESH = 5

def main():
    machine.freq(160000000)
    count = _SCREEN_REFRESH
    try:
        conf_class = config.Config()
        conf_data = conf_class.load_config()
        #counter_class = counter.Counter(9, 10, conf_data)
        temperature_class = temperature.Temperature(4, 5, conf_data)
        screen_class = screen.Screen(conf_data)
        screen_class.write_display()
        screen_class.write_data()
        while True:
            temperature_class.temperature()
            conf_data['p']['l'] = temperature_class.temp_level()
            time.sleep_ms(1000)
            count -= 1
            if count <= 0:
                screen_class.clear_reg()
                screen_class.write_data()
                count = _SCREEN_REFRESH

    except SyntaxError:
        print('main error')
    except TypeError:
        print('type error main')


if __name__ == '__main__':
    main()
