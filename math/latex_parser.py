import re

def parse(s):
    units=['m','g','s','C','J','N','W','V','A','T','Wb','mol','M']
    pre={'n':'0.000000001','\\\\mu':'0.000001','m':'0.001','d':'0.01','c':'0.1','k':'1000','M':'1000000','G':'1000000000'}
    const={'u':'1.660539*10**(-27)','e':'1.6021766*10**(-19)','g':'9.80665'}
    s=s.replace('\\cdot','*')
    print(s)
#    fr=r'\\frac({})({})'
#    print(fr,s,fr in s)
    s=re.sub(r'\\frac{([\d\D^}]*)}{([\d\D^}]*)}',r'(\1)/(\2)',s)
    for i in units:
        l=re.findall(r'([A-Za-z]*)'+i[0],s)#,'('+pre['\\1']+')',s))
        for j in l:
#            print(l,i,pre[l[0]])
            try:
                s=re.sub(r'[A-Za-z]*'+i[0],'('+pre[j]+')',s)
            except:
                s=re.sub(r'([A-Za-z]*)'+i[0],'',s)
    for i in const.keys():
        l=re.findall(i,s)
        for j in l:
            s=re.sub(i,'('+const[i]+')',s)
    s=re.sub(r'\^', r'**', s)
    s=re.sub(r'(\d)\(',r'\1*(',s)
    s=s.replace('{','(')
    s=s.replace('}',')')
#    for i in units:
#        s=re.sub(r'([A-Za-z]*)'+i[0],pre['\\1']+'*',s)
    s=re.sub(r'[A-Za-z]','',s)
    return s

#s='5\\frac{123}{1}\cdot4^2'
while 1:
    s2=input()
#print(parse(s), eval(parse(s)))
    print(parse(s2), eval(parse(s2)))
