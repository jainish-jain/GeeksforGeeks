#{ 
#Driver Code Starts
#Initial Template for Python 3

import math


 # } Driver Code Ends

#User function Template for python3
import math
##Complete this function
def digitsInFactorial(n):
    #Your code here
    if (n < 0): pass

    if (n <= 1): 
        return 1; 
  
    digits = 0; 
    for i in range(2, n + 1): 
        digits += math.log10(i); 
  
    return math.floor(digits) + 1;


#{ 
#Driver Code Starts.

def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input())
        
        print(digitsInFactorial(N))
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends