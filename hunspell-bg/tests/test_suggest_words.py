#!/usr/bin/python3

import enchant

wdlst = [ "здравей", "чай", "сутрин"]
dic = enchant.Dict("bg_BG")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
