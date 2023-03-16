# get json data from a url, and speak it every 5 sec.
# tested with mac 11.4,  python 2.7

import urllib2
from os import system
import time, json


def get_and_read():
  link = ""
  f = urllib2.urlopen(link)
  info = json.loads(f.read())
  f.close()
  print(info)
  return info["es"] % 100


last = 0
while 1:
 num = get_and_read()
 if last != num:
     system("say -v Ting-Ting " + str("{:.1f}".format(num)))
     last = num
 time.sleep(5)
