import cgi
form = cgi.FieldStorage()              # 解析表单数据
print('Content-type: text/html')      # 加上空行

html = """
<TITLE>Register OK!.py</TITLE>
<H1>Greetings</H1>
<HR>
<P>%(name)s</P>
<P>%(nick-name)s</P>
<P>%(e-mail)s</P>

<HR>"""
def htmlize(adict):
    new = {}
    new['name'] = ('Hello, %s.' % adict['name'].value)
    new['nick-name'] = ('您的昵称：%s' % adict['nick-name'].value)
    new['e-mail'] = ('您的邮箱地址：%s' % adict['e-mail'].value)
    return new

if not 'name' in form:
    print(html % {'name':'注册失败，大侠请重新来过!', 'nick-name':'', 'e-mail':''})
else:
    print(html % htmlize(form))
