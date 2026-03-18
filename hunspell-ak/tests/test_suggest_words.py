#!/usr/bin/python3

import enchant

wdlst = [ "Hɛlo", "tii", "anɔpa"]
dic = enchant.Dict("ak_GH")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
