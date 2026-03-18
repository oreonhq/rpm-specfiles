#!/usr/bin/python3

import enchant

wdlst = [ "Xin chào", "trà", "buổi sáng"]
dic = enchant.Dict("vi_VN")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
