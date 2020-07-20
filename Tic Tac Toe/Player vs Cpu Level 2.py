# In this mode Cpu stops another player from winning.
import numpy as np
r=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
def display():
    c=-1
    for i in range(0,3):
        for j in range(0,3):
            c=c+1
            print('\t%c\t|'%(r[c]),end=' ')
        print('')
        print('_________________________________________________\n')
def win():
    w=0
    if ((r[0]=='X' and r[1]=='X' and r[2]=='X') or (r[3]=='X' and r[4]=='X'and r[5]=='X') or (r[6]=='X'and r[7]=='X'and r[8]=='X') or (r[0]=='X'and r[3]=='X'and r[6]=='X') or (r[1]=='X'and r[4]=='X'and r[7]=='X') or (r[2]=='X'and r[5]=='X'and r[8]=='X') or (r[0]=='X'and r[4]=='X'and r[8]=='X') or (r[2]=='X'and r[4]=='X'and r[6]=='X')):
        print('player 1 wins')
        w=1
        return(w)
    elif ((r[0]=='0'and r[1]=='0'and r[2]=='0') or (r[3]=='0'and r[4]=='0'and r[5]=='0') or (r[6]=='0'and r[7]=='0'and r[8]=='0') or (r[0]=='0'and r[3]=='0'and r[6]=='0') or (r[1]=='0'and r[4]=='0'and r[7]=='0') or (r[2]=='0'and r[5]=='0'and r[8]=='0') or (r[0]=='0'and r[4]=='0'and r[8]=='0') or (r[2]=='0'and r[4]=='0'and r[6]=='0')):
        print('CPU wins')
        w=1
        return(w)


def cin(x,y,z):
    if r[x]=='X' and r[y]=='X' and  r[z]==' ':
        r[z]='0'
        v=1
        return v
    if r[x]=='X' and  r[y]==' ' and  r[z]=='X':
        r[y]='0'
        v=1
        return v
    if r[x]==' ' and  r[y]=='X' and  r[z]=='X':
        r[x]='0'
        v=1
        return v

def cwin(x,y,z):
    if r[x]=='0' and r[y]=='0' and  r[z]==' ':
        r[z]='0'
        v=1
        return v
    if r[x]=='0' and  r[y]==' ' and  r[z]=='0':
        r[y]='0'
        v=1
        return v
    if r[x]==' ' and  r[y]=='0' and  r[z]=='0':
        r[x]='0'
        v=1
        return v

print('WELCOME TO TIC TAC TOE\n')
md=0
display()
for i in range(1,10):
    md=md+1
    f=0
    if(i%2!=0):
            while(f==0):
                print('player chance:')
                t1=int(input())
                if r[t1-1]==' ':
                    r[t1-1]='X'
                    f=1
                else:
                    print('Invalid Chance\n Try again')
    else:
        print('CPU chance:')
        x=[0,3,6,0,1,2,0,2]
        y=[1,4,7,3,4,5,4,4]
        z=[2,5,8,6,7,8,8,6]
        v=0 
        for i in range(0,8):
            d=cwin(x[i],y[i],z[i])
            if d==1:
                break
        for i in range(0,8):
            d=cin(x[i],y[i],z[i])
            if d==1:
                break
        if d!=1:
            while(f==0):
                t1=int(1+(9-1)*np.random.random(1))
                t1=np.round(t1)
                if r[t1-1]==' ':
                    r[t1-1]='0'
                    f=1
        else:
            print('Invalid Chance\n Try Again')
    display()
    w=win()
    if w==1:
        break
    if md==9:
        print('match draw')





    
