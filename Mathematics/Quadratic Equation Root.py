#{ 
#Driver Code Starts
#Initial Template for Python 3

import math



 # } Driver Code Ends

#User function Template for python3


##Complete this function
from math import floor
def quadraticRoots(a,b,c):
    #Your code here
    s=(b*b)-(4*a*c)
    r=abs(s)**0.5
    if s>0:
        h=floor((-b+r)/(2*a))
        l=floor((-b-r)/(2*a))
        if h>l:
            print(h,l)
        else:
            print(l,h)
        
    elif s==0:
        j=floor(-b/(2*a))
        print(j,j)
    else:
        print("Imaginary")


#{ 
#Driver Code Starts.

def main():
    
    T=int(input())
    
    while(T>0):
        abc=[int(x) for x in input().strip().split()]
        a=abc[0]
        b=abc[1]
        c=abc[2]
        
        quadraticRoots(a,b,c)
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends