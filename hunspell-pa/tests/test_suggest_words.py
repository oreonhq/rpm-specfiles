#!/usr/bin/python3

import enchant

wdlst = [ "ਸਡ", "ਸਤ ਸ੍ਰੀ", "ਪੰਜਬ"]
dic = enchant.Dict("pa_IN")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
