from m5stack import lcd
import json
import time
import network
import machine
import _thread

def load_config(filename="wifi.json"):
  f = open(filename, 'r')
  config = json.loads(f.read())
  f.close()
  return config

def do_connect():

  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)

  config = load_config()

  while not wlan.isconnected():
    lcd.print("WiFi connecting ... ", 0, 0)

    for net in wlan.scan():
      ssid = net[0].decode()

      if ssid in config:
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

lcd.clear()
do_connect()

lcd.println("NTP sync ... ")
rtc = machine.RTC()
rtc.ntp_sync(server="ntp.jst.mfeed.ad.jp", tz="JST-9")
rtc.synced()
lcd.println("success")
time.sleep_ms(100)

def clock():
  lcd.clear()
  lcd.font(lcd.FONT_7seg, fixedwidth=True, dist=16, width=2)
  while True:
    d = time.strftime("%Y-%m-%d", time.localtime())
    t = time.strftime("%H:%M:%S", time.localtime())
    lcd.print(d, lcd.CENTER, 50, lcd.ORANGE)
    lcd.print(t, lcd.CENTER, 130, lcd.ORANGE)
    time.sleep_ms(500)

_thread.start_new_thread('Clock', clock, ())
