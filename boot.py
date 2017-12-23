def do_connect():
    import network
    import webrepl
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('dsl', '0x323633EAECF2F2ECEEE2E3F3F0EAE3F0E2F8E3383737343338ED363837')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    webrepl.start()

do_connect()
