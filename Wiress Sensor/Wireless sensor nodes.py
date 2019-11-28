import numpy as np
import matplotlib.pyplot as plt
A=50
num_node=10
#part 1
data=0+(A-0)*np.random.random([2,num_node])
plt.figure(1)
plt.plot(data[0,:],data[1,:],'r*')
for i in range(0,num_node):
    plt.text(data[0,i],data[1,i],str(i+1))
data=np.round(data)
print(data)

#part 2
dist=np.zeros([num_node,num_node])
for i  in range(0,num_node):
     for j in range(0,num_node):
         d=np.sqrt((data[0,j]-data[0,i])**2+(data[1,j]-data[1,i])**2)
         dist[i,j]=np.round(d)
print('Distance matrix:')
print(dist)
gm=dist

#part 3
sensible_range=20
for i in range(0,num_node):
    for j in range(0,num_node):
        if dist[i,j]<sensible_range and i!=j:
            gm[i,j]=1
        else:
            gm[i,j]=0
print('Graph matrix:')
print(gm)

#part 4
n=input('Enter node no.:')
n=int(n)
print('Neighbours are:')
x1=data[0,n-1]
y1=data[1,n-1]
for j in range(0,num_node):   
    if gm[n-1,j]==1:
        print(j+1)
        x2=data[0,j]
        y2=data[1,j]
        p1=[x1,x2]
        p2=[y1,y2]
        plt.plot(p1,p2)
plt.plot(x1,y1,'k*')
plt.show()

#part 5
enr=np.ones([num_node])*1000
for i in range(1,1000):
    r=1+(num_node-1)*np.random.random()
    r=np.round(r)
    r=int(r)
    etx=40+(60-40)*np.random.random()
    etx=np.round(etx)
    erx=20+(40-20)*np.random.random()
    erx=np.round(erx)
    if enr[r-1]>=etx:
        enr[r-1]=enr[r-1]-etx
    print(enr)
    for j in range(0,num_node):
        x3=data[0,j]
        y3=data[1,j]
        plt.text(x3,y3,str(j+1))
        if gm[n-1,j]==1:
            if enr[j]>=erx:
                enr[j]=enr[j]-erx
        if enr[j]>750:
            plt.plot(x3,y3,'g*')
        if enr[j]>500 and enr[j]<750:
            plt.plot(x3,y3,'c*')
        if enr[j]>250 and enr[j]<500:
            plt.plot(x3,y3,'y*')
        if enr[j]<250 and enr[j]>120:
            plt.plot(x3,y3,'m*')
        if enr[j]<120 and enr[j]>0:
            plt.plot(x3,y3,'r*')
        if enr[j]<40:
            plt.plot(x3,y3,'k*')
    plt.title(['itration no.',str(i)])
    plt.pause(0.1)
    
        
    



