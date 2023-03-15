# get json data from a url, and speak it every 5 sec.
# tested with mac 11.4,  python 2.7

import urllib2
from os import system
import time, json, decimal


def get_and_read():
  link = ""
  f = urllib2.urlopen(link)
  info = json.loads(f.read())
  f.close()
  print(info)
  num = "{:.2f}".format(info["es"] % 100)
  system("say " + str(decimal.Decimal(num).normalize()))


while 1:
 get_and_read()
 time.sleep(5)
