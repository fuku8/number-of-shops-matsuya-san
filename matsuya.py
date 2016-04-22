# encoding: utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

html =urlopen("http://pkg.navitime.co.jp/matsuyafoods/area/list")
bsObj = bs(html,"lxml")
span_list = bsObj.findAll("span")
sum = 0;
for s in span_list:
  ss = re.sub("\D","",str(s))
  if ss != "":
    sum +=int(ss)
print(sum)
