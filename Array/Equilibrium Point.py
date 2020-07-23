# User function Template for python3

# Complete this function


def equilibriumPoint(arr, n):
    # Your code here
    total_sum = sum(arr) 
    leftsum = 0
    for i, num in enumerate(arr): 
          
        # total_sum is now right sum 
        # for index i 
        total_sum -= num 
          
        if leftsum == total_sum: 
            return i+1 
        leftsum += num 
       
      # If no equilibrium index found,  
      # then return -1 
    return -1
            



#{ 
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]

        print(equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends