import config, counter, temperature
import time
import machine


def main():
    machine.freq(160000000)
    try:
        conf_class = config.Config()
        conf_data = conf_class.load_config()
        counter_class = counter.Counter(16, 5, conf_data)
        temperature_class = temperature.Temperature(12, 4, conf_data)
        while True:
            temperature_class.temperature()
            time.sleep_ms(1000)
            print('write ok')
    except SyntaxError:
        print('main error')
    except TypeError:
        print('type error main')


if __name__ == '__main__':
    main()
