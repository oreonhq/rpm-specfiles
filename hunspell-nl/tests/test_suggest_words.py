#!/usr/bin/python3

import enchant

wdlst = [ "Hal", "the", "ochte"]
dic = enchant.Dict("nl_NL")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
