#User function Template for python3

#Complete this function
def leaders(arr,size):
    #Your code here
    
    '''
    Just return the list with leaders in it
    '''
    
    ls=[arr[size-1]]
    if size==1:
        pass
    else:   
        max_from_right = arr[size-1]    
        for i in range( size-2, -1, -1):         
            if max_from_right <= arr[i]:             
                ls.append(arr[i]) 
                max_from_right = arr[i]
    
    return ls[::-1] 


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        
        A=leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends