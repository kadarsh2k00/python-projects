r=['+','+','+','+','+','+','+','+','+']
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
    if ((r[0]=='X'and r[1]=='X' and r[2]=='X') or (r[3]=='X' and r[4]=='X'and r[5]=='X') or (r[6]=='X'and r[7]=='X'and r[8]=='X') or (r[0]=='X'and r[3]=='X'and r[6]=='X') or (r[1]=='X'and r[4]=='X'and r[7]=='X') or (r[2]=='X'and r[5]=='X'and r[8]=='X') or (r[0]=='X'and r[4]=='X'and r[8]=='X') or (r[2]=='X'and r[4]=='X'and r[6]=='X')):
        print('player 1 wins')
        w=1
        return(w)
    elif ((r[0]=='0'and r[1]=='0'and r[2]=='0') or (r[3]=='0'and r[4]=='0'and r[5]=='0') or (r[6]=='0'and r[7]=='0'and r[8]=='0') or (r[0]=='0'and r[3]=='0'and r[6]=='0') or (r[1]=='0'and r[4]=='0'and r[7]=='0') or (r[2]=='0'and r[5]=='0'and r[8]=='0') or (r[0]=='0'and r[4]=='0'and r[8]=='0') or (r[2]=='0'and r[4]=='0'and r[6]=='0')):
        print('player 2 wins')
        w=1
        return(w)
print('WELCOME TO TIC TAC TOE\n')
for i in range(1,10):
    f=0
    display()
    if(i%2!=0):
            while(f==0):
                print('player 1 chance:')
                t1=int(input())
                if r[t1-1]=='+':
                    r[t1-1]='X'
                    f=1
                else:
                    print('invalid entry\n Try again')
    else:
        while(f==0):
            print('player 2 chance:')
            t1=int(input())
            if r[t1-1]=='+':
                r[t1-1]='0'
                f=1
            else:
                print('invalid entry\n Try again')
    d=win()
    if d==1:
        break
    
