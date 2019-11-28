import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
from itertools import permutations
from itertools import combinations 
import random

color_num=[0,1,2,3,4,5,6,7,8]

####c=int(input('Enter the no. of colors'))
##d=int(input('Enter the no. of digits'))

def check_matches(n1,n2):
    p=0
    for i in range(0,d):
        if n1[i]==n2[i]:
            p=p+1
    return p
        
def gen_vector(c,d):
        
    ##choices = list(range(c))
    ##random.shuffle(choices)
    ##
    ##selected_color=[]
    ##for m in range(0,d):
    ##    a=(choices.pop())
    ##    print(a)
    ##    selected_color.append((a))
    ##    
    ##arrange=[]
    ##perm=permutations(selected_color)
    ##for i in list(perm):
    ##    arrange.append((i))
    ##    print(i)
    ##code=random.choice(arrange)
    ##print('CODE:',code)
   
    guess_vector=[]
##    comb = permutations(avail_color,d)
    B=combinations(avail_color,d)
    for i in list(B):
        C=permutations(i)
        e=0
        for j in list(C):
            e=e+1
##            print (j)
            guess_vector.append(j)
    print(e)
    answer=random.choice(guess_vector)
    print('Answer code:',answer)

    guess=random.choice(guess_vector)
    print('Guess:',guess)

 
    TF=np.ones((len(guess_vector)))
    R=1
    print(TF)

    while(R!=9 and guess!=answer):
        R=R+1

        N_matches=check_matches(answer,guess)
        print('N_Matches:',N_matches)
    
        for m in range(0,len(guess_vector)):
            g=guess_vector[m]
            f=0
            for k in range(0,d):
                if g[k]==guess[k]:
                     f=f+1
            if f!=N_matches:
                TF[m]=0
        print('TF')    
        print(TF)

        for t in range(len(guess_vector)-1,-1,-1):
            if TF[t]==0:
                del guess_vector[t]
        
        TF=np.ones((len(guess_vector)))
        guess=random.choice(guess_vector)
        print('Guess:',guess)
    print('TF')    
    print(TF)
    print('guess_vector')
    print(guess_vector)
    if guess==answer:
        print('PLAYER 2 WINS') 
                  
    return R

##N=int(input('Enter the number of matches: '))
N=20
M=np.array([[6,4],[8,5],[9,6]])
print(M)

R_all=np.zeros((3,N))


for s in range(0,3):
    NR=[]
    avail_color=[]
    c=M[s][0]
    d=M[s][1]

    for i in range(0,c):
        avail_color.append(color_num[i])
    print('Available colors: ',avail_color)
    for g in range(0,N):
            
        S=gen_vector(c,d)
        print('Rounds :',S)    
        NR.append((S))
    R_all[s]=np.asarray(NR)
   
print('R_all:',R_all)

plt.figure(1)

win_perc=np.zeros((3,1))
R_avg=np.zeros((3,1))
for s in range(0,3):
        #ploting
        plt.subplot(1,3,s+1)
        plt.hist(R_all[s,:])
        plt.xlabel('ROUNDS')
        plt.ylabel('FREQUENCY')
        plt.title('COMBINATION'+str(s+1))
        #win_perc and #Avg_Rounds       
        n=0
        p=0
        for v in range(0,N):
                p=p+R_all[s,v]
                if R_all[s,v]<9:
                        n=n+1
        win_perc[s]=(n/N)*100
        R_avg[s]=(p/N)
print('Win percentage:',win_perc)
print('R_avg:',R_avg)
plt.show()


        





        
        
        


    


   
    
