class col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    B = '\033[40m'
    W = '\033[7m'
    R = '\033[41m'
    O = '\033[43m'

ln=256
l=[1 for i in range(ln)]
for j in range(ln):
    l2=[]
    curr=0
    print(' '*j, end='')
    for i in l:
        if i==1:
            print(f'{col.W}  {col.ENDC}', end='')
            curr=1-curr
        else:
            print(f'{col.B}  {col.ENDC}', end='')
        if len(l2)<ln-1-j:
            l2.append(curr)
#    print(l2)
    l=l2
#    print(l)
    print(col.ENDC)

