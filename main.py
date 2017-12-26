import config, temperature
import time
import machine


def main():
    machine.freq(160000000)
    try:
        conf_class = config.Config()
        conf_data = conf_class.load_config()
        #counter_class = counter.Counter(9, 10, conf_data)
        temperature_class = temperature.Temperature(4, 13, conf_data)
        #screen_class = screen.Screen(conf_data)
        while True:
            temperature_class.temperature()
            print(conf_data)
            #screen_class.write_display()
            time.sleep_ms(1000)
    except SyntaxError:
        print('main error')
    except TypeError:
        print('type error main')


if __name__ == '__main__':
    main()
