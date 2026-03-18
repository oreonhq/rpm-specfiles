#!/usr/bin/python3

import enchant

wdlst = [ "สวัสดี", "ชา", "เช้า"]
dic = enchant.Dict("th_TH")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
