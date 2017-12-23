# import valve
import time

import machine
import neopixel


def main():
    #machine.freq(160000000)
    try:
        np = neopixel.NeoPixel(machine.Pin(4), 32)
        # vl = valve.Valve(2, 3, 4, 5, 12)
        while True:
            demo(np)
        #    adc, status = vl.get_status()
        #    print(adc, status)
            time.sleep_ms(1000)
            print('write ok')
    except SyntaxError:
        print('main error')
    except TypeError:
        print('type error main')


def demo(np):
    n = np.n
    print(np.n)
    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()


if __name__ == '__main__':
    main()
