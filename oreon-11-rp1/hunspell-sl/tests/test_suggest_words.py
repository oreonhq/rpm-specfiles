#!/usr/bin/python3

import enchant

wdlst = [ "zdravo", "čaj", "jutro"]
dic = enchant.Dict("sl_SI")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
