'''
Input:
2
3 
6
Output:
6
60
'''

import math
def getSmallestDivNum(n):
    #RETURN ans
    ip = 1
    for i in range(1,n+1): 
	    ip = int((ip * i)/math.gcd(ip, i))		 
    return ip


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        print(getSmallestDivNum(n))
# } Driver Code Ends