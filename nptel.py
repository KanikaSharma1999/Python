'''2) In a list of integers l, the neighbours of l[i] are l[i-1] and l[i+1]. l[i] is a hill if it is strictly greater than its neighbours and a valley if it is strictly less than its neighbours.

Write a function counthv(l) that takes as input a list of integers l and returns a list [hc,vc] where hc is the number of hills in l and vc is the number of valleys in l. 
'''



def countv(l):
    if len(l)>=3:
        hc=0
        vc=0
        for i in range(1,len(l)-1):
            if (l[i-1]<=l[i] and l[i]>=l[i+1]):
                hc=hc+1
                print(l[i])
            elif (l[i-1]>=l[i] and l[i]<=l[i+1]):   
                vc=vc+1
                print(l[i])
            else:
                None
        return(hc,vc)       
list=[3,1,2,3] 
countv(list)
