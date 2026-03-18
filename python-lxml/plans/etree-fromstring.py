import lxml.etree as et
s = '<foo><bar baz="xyzzy">a<![CDATA[b]]>c</bar></foo>'
x = et.fromstring(s)
t = x.find('bar').text
print(t)
if t != 'abc':
    raise Exception()
