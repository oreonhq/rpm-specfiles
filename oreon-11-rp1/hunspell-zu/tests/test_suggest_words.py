#!/usr/bin/python3

import enchant

wdlst = [ "Sawubona", "itiye", "ekuseni"]
dic = enchant.Dict("zu_ZA")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
