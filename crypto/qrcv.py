#import cv2 as cv
#import numpy as np
tmp=0
'''
s=['00000001100110100    10000000',
   '011111011001011010   10111110',
   '0100010110111110100  10100010',
   '01000101100111100101 10100010',
   '01000101101010110001110100010',
   '01111101011101000100010111110',
   '00000001010101010101010000000',
   '11111111110111110011111111111',
   '0110100100100011011010101    ',
   '00000010111110000011010110   ',
   '101111011001101111101110100  ',
   '1111011001010010110100000101 ',
   '01101000110100011011010110100',
   '00011110110001001110001110101',
   '11010100110110010111110011100',
   '01101110010110101010101111101',
   '01110001010110011010001110110',
   '11100010110111011111010011100',
   '01100101011010111011100100100',
   '11111011000100110000100010100',
   '01110000101011011111000001000',
   '11111111001110110011011100011',
   '00000001100100010111010101101',
   '01111101000100101101011101001',
   '01000101111011000011000001111',
   '01000101010111011000110000101',
   '01000101100000110101011000110',
   '01111101101110001000000001101',
   '00000001000000111001011010101']
'''

s=['00000001100110100010010000000',
   '01111101100101101010110111110',
   '01000101101111101001010100010',
   '01000101100111100101010100010',
   '01000101101010110001110100010',
   '01111101011101000100010111110',
   '00000001010101010101010000000',
   '11111111110111110011111111111',
   '01101001001000110110101010000',
   '00000010111110000011010110001',
   '10111101100110111110111010000',
   '11110110010100101101000001010',
   '01101000110100011011010110100',
   '00011110110001001110001110101',
   '11010100110110010111110011100',
   '01101110010110101010101111101',
   '01110001010110011010001110110',
   '11100010110111011111010011100',
   '01100101011010111011100100100',
   '11111011000100110000100010100',
   '01110000101011011111000001000',
   '11111111001110110011011100011',
   '00000001100100010111010101101',
   '01111101000100101101011101001',
   '01000101111011000011000001111',
   '01000101010111011000110000101',
   '01000101100000110101011000110',
   '01111101101110001000000001101',
   '00000001000000111001011010101']

def qr_show(img, mask=-1):
    print('---------------------BEGINNING OF QR---------------------')
    for i in range(len(img)):
        for j in range(len(img[i])):
     #       if (((ic+j)%3+ic+j)%2==0) and not (((i<9 or i>20) and j<9) or (i<9 and j>20) or i==6 or j==6):
            if (mask==0 and (j%3==0) and not (((i<9 or i>20) and j<9) or (i<9 and j>20) or i==6 or j==6 or ((i>19 and i<25) and (j>19 and j<25)))):
                print(f"{bcolors.O}  {bcolors.ENDC}",end='')
            elif (mask==1 and ((i+j)%3==0) and not (((i<9 or i>20) and j<9) or (i<9 and j>20) or i==6 or j==6 or ((i>19 and i<25) and (j>19 and j<25)))):
                print(f"{bcolors.O}  {bcolors.ENDC}",end='')
            elif (mask==2 and ((i+j)%2==0) and not (((i<9 or i>20) and j<9) or (i<9 and j>20) or i==6 or j==6 or ((i>19 and i<25) and (j>19 and j<25)))):
                print(f"{bcolors.O}  {bcolors.ENDC}",end='')
            elif (mask==3 and (i%2==0) and not (((i<9 or i>20) and j<9) or (i<9 and j>20) or i==6 or j==6 or ((i>19 and i<25) and (j>19 and j<25)))):
                print(f"{bcolors.O}  {bcolors.ENDC}",end='')
            elif (mask==4 and (((i*j)%3+i*j)%2==0) and not (((i<9 or i>20) and j<9) or (i<9 and j>20) or i==6 or j==6 or ((i>19 and i<25) and (j>19 and j<25)))):
                print(f"{bcolors.O}  {bcolors.ENDC}",end='')
            elif (mask==5 and (((i*j)%3+i+j)%2==0) and not (((i<9 or i>20) and j<9) or (i<9 and j>20) or i==6 or j==6 or ((i>19 and i<25) and (j>19 and j<25)))):
                print(f"{bcolors.O}  {bcolors.ENDC}",end='')
            elif (mask==6 and ((i//2+j//3)%2==0) and not (((i<9 or i>20) and j<9) or (i<9 and j>20) or i==6 or j==6 or ((i>19 and i<25) and (j>19 and j<25)))):
                print(f"{bcolors.O}  {bcolors.ENDC}",end='')
            elif (mask==7 and ((i*j)%2+(i*j)%3==0) and not (((i<9 or i>20) and j<9) or (i<9 and j>20) or i==6 or j==6 or ((i>19 and i<25) and (j>19 and j<25)))):
                print(f"{bcolors.O}  {bcolors.ENDC}",end='')
            elif img[i][j] == 1 or img[i][j] == '1':
                print(f"{bcolors.W}  {bcolors.ENDC}",end='')
            elif img[i][j] == 0 or img[i][j] == '0':
                print(f"{bcolors.B}  {bcolors.ENDC}",end='')
            else:
                print(f"{bcolors.R}  {bcolors.ENDC}",end='')
        print()
    print('------------------------END OF QR------------------------')
def mask(img):
    b=str(img[8][2])+str(img[8][3])+str(img[8][4])
    return int(b,2)
class bcolors:
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
img=[['' for i in range(29)] for i in range(29)]
for i in range(len(s)):
    for j in range(len(s[i])):
        img[i][j]=s[i][j]
#print('123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890')
#print(img)
qr_show(img,0)
qr_show(img,1)
qr_show(img,2)
qr_show(img,3)
qr_show(img,4)
qr_show(img,5)
qr_show(img,6)
qr_show(img,7)

for i in range(len(img)):
    for j in range(len(img[i])):
        if (((i*j)%3+i+j)%2==0) and not (((i<9 or i>20) and j<9) or (i<9 and j>20) or i==6 or j==6 or ((i>19 and i<25) and (j>19 and j<25))):
            img[i][j]= '0' if img[i][j]=='1' else '1' if img[i][j]=='0' else ' '

qr_show(img)
print(mask(img))
s=''
for k in range(len(img)//2):
    for l in range(len(img)):
        i,j=len(img)-l-1 if k%2==0 else l,len(img)-2*k-1
        if not (((i<9 or i>20) and j<9) or (i<9 and j>20) or i==6 or j==6 or ((i>19 and i<25) and (j>19 and j<25))):
            s+=img[i][j]
        j=len(img)-2*k-2
        if not (((i<9 or i>20) and j<9) or (i<9 and j>20) or i==6 or j==6 or ((i>19 and i<25) and (j>19 and j<25))):
            s+=img[i][j]
#print(s)
l=[1 if i=='0' else 0 if i=='1' else 2 for i in s]
#print(l)
enc=l[:4]
lb=[l[4+i*8:4+(i+1)*8] for i in range(len(l)//8)]
#print(lb)
lbb=[]
for i in range(len(lb)):
    tmp=''
    for j in lb[i]:
        tmp+=str(j)
    lbb.append(tmp)
#for i in lbb:
#    print(i)
#cv.imshow(img)
#print(img)
#print(s)
