# ref: https://stackoverflow.com/questions/31167967/python-3-4-text-to-speech-with-sapi
# get json data from a url, and speak it every 5 sec.
# tested with windows 11, python 3.9

import urllib.request,win32com.client
import time, json, decimal

def get_and_read(speaker):
  link = ""
  with urllib.request.urlopen(link) as f:
    info = json.loads(f.read())
    print(info)
    num = "{:.2f}".format(info["es"] % 100)
    speaker.Speak(decimal.Decimal(num).normalize())

speaker = win32com.client.Dispatch("SAPI.SpVoice")


while 1:
 get_and_read(speaker)
 time.sleep(5)
