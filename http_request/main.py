from m5stack import lcd
import json
import wifi
import urequests

class Config:
  def __init__(self, filename="settings.json"):
    f = open(filename)
    self.__json = json.loads(f.read())
    f.close()

  def __getattr__(self, name):
    return self.__json[name]

config = Config()
wifi.do_connect(config.wifi)

header = {
    "X-Api-Key": config.mackerel["apikey"]
}

r = urequests.get("https://api.mackerelio.com/api/v0/services", headers=header)
lcd.println(r.text) 
