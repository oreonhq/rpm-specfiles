#!/usr/bin/python3

import enchant

wdlst = [ "прывітанне", "чай", "раніца"]
dic = enchant.Dict("be_BY")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
