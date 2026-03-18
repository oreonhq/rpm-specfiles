#!/usr/bin/python3

import enchant

wdlst = [ "হ্যাল", "ডিনা", "বাঙল", "অসময়"]
dic = enchant.Dict("as_IN")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
