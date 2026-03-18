#!/usr/bin/python3

import enchant

wdlst = [ "salam", "çay", "sabah"]
dic = enchant.Dict("az_AZ")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
