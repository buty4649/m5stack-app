from m5stack import lcd
import time
import network

def do_connect(config={}):

  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)

  while not wlan.isconnected():
    lcd.print("WiFi connecting ... ")

    for net in wlan.scan():
      ssid = net[0].decode()

      if ssid in config.keys():
        wlan.connect(ssid, config[ssid])

        while not wlan.isconnected():
          time.sleep_ms(100)

        ifconfig = wlan.ifconfig()
        lcd.println("success")
        lcd.println("IP: %s" % ifconfig[0])
        return

    lcd.print("error.")
    time.sleep(1)

  return
