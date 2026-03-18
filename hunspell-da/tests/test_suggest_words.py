#!/usr/bin/python3

import enchant

wdlst = [ "hej", "te", "morgen"]
dic = enchant.Dict("da_DK")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
