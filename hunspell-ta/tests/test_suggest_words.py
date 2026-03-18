#!/usr/bin/python3

import enchant

wdlst = [ "வணகம்", "நம்டைய", "தமழ்"]
dic = enchant.Dict("ta_IN")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
