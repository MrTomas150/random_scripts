import matplotlib.pyplot as plt
from numpy import arange
e=2.718281828459045
'testas'
rang=[0,1,0.01]
fun='pow(e,x)'
while 1:
    temp=input(f'your functions(seperated by ;)[default={fun}]: ')
    if temp.lower() in ["quit",'q']:
        break
    fun=temp if temp else fun
    temp=input(f'range of you plot{rang}: '.replace(', ', ':'))
    if temp.lower() in ["quit",'q']:
        break
    temp=temp.split(':') if temp else rang
    for i in range(min(len(temp),3)):
            rang[i]=float(temp[i])

    for f in fun.split(';'):
        y=[]
        for x in arange(rang[0],rang[1],rang[2]):
            try:
                exec('y.append('+f+')')
            except:
                print("check your syntax:"+f)
                break
        else:
            plt.plot(arange(rang[0],rang[1],rang[2]),y)
    else:
        plt.grid(1)
        plt.show()
print('thank you for using')
print(
'''
       _       _
 _ __ | | ___ | |_ __ _ ___
| '_ \| |/ _ \| __/ _` / __|
| |_) | | (_) | || (_| \__ \\
| .__/|_|\___/ \__\__,_|___/
|_|
'''
)
