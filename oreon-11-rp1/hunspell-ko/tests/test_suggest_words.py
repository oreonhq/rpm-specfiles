#!/usr/bin/python3

import enchant

wdlst = [ "안녕", "차", "아침"]
dic = enchant.Dict("ko_KR")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
