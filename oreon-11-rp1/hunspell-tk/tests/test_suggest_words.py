#!/usr/bin/python3

import enchant

wdlst = [ "salam", "çaý", "irden"]
dic = enchant.Dict("tk_TM")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
