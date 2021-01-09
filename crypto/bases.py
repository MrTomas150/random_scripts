import codecs
from math import log
dec=14311663942709674867122208214901970650496788151239520971623411712977120586163535880168563325

hexify={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
rehex={hexify[i]:i for i in hexify}

def maxPwr(base, num):
    return int(log(num, base))

def dec2hex(dec):
    mLast = maxPwr(16, dec)+1
    s=''
    while dec!=0:
        m = maxPwr(16, dec)
        s+='0'*(mLast-m-1)
        mLast=m
        s += hexify[dec//pow(16, m)]
        dec-=rehex[s[-1]]*pow(16,m)
    s+='0'*m
    return s
#m=14311663942709674867122208214901970650496788151239520971623411712977120586163535880168563325
print(dec2hex(m))
