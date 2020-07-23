#User function Template for python3
from collections import Counter
#Complete this function
def majorityWins(arr, n,  x,y):
    # code here
    c=Counter(arr)
    if c[x]==c[y]:
        return min(x,y)
    else:
        if c[x]>c[y]:
            return x
        else:
            return y
   
    



#{ 
#  Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while(T>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        x,y=map(int,input().strip().split())
        
        print(majorityWins(arr,n,x,y))
        T-=1

# } Driver Code Ends