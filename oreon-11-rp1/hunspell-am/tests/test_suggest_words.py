#!/usr/bin/python3

import enchant

wdlst = [ "ሀሎ", "ሻይ", "ጠዋት"]
dic = enchant.Dict("am_ET")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
