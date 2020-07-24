#User function Template for python3


#Complete this function
def convertToWave(A,N):
    #Your code here
    for i in range(1,N,2):
        if A[i-1]<A[i]:
            A[i-1],A[i]=A[i],A[i-1]
    A[:]=A


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().split()]
        convertToWave(A,N)
        for i in A:
            print(i,end=" ")
        
        
        print()
        
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends