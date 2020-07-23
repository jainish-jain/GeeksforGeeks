#User function Template for python3

#Complete this function
def reverseInGroups(a,n,k):
    #Your code here
    ls=[]
    for i in range(0,n,k):
        ls.extend(list(a[i:i+k])[::-1])
    return ls


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        nk=[int(x) for x in input().strip().split()]
        
        N=nk[0]
        K=nk[1]
        
        A=[int(x) for x in input().strip().split()]
        
        A=reverseInGroups(A,N,K)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends