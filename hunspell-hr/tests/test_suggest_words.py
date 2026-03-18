#!/usr/bin/python3

import enchant

wdlst = [ "Zdravo", "čaj", "jutro"]
dic = enchant.Dict("hr_HR")
for wd in wdlst:
    dic.check(wd)
    print("input word = {0}, Suggestions => {1}".format(wd, dic.suggest(wd)))
