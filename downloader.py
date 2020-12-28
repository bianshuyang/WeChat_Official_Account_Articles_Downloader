a = input('使用说明：输入.tmp.txt前的文本')
with open(a+'.tmp.txt','r',encoding='utf-8') as f:
    a = f.readlines()
a = ''.join(a)
a = a.split('hrefs="')
a.remove(a[0])
i = 0
g = []
while i<=len(a)-1:
    try:
        g.append(a[i][0:a[i].index(';scene=')])
    except:
        pass
    i = i+1
for i in g:
    if len(i) > 220:
        g.remove(i)
g = list(set(g))
with open('out.txt','w',encoding='utf-8') as f:
    f.write('\n'.join(g))

import pdfkit
with open('out.txt','r',encoding='utf-8') as f:
    a = f.readlines()
i = 0
while i<=len(a)-1:
    try:
        link = a[i].replace('\n','')
        pdfkit.from_url(link,str(i)+'.pdf')
    except:
        with open('log.txt','a',encoding='utf-8') as f:
            f.write(i)
    i = i+1
