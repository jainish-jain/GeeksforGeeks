# your task is to complete this function
# finvtion should return an integer
def transitionPoint(arr, n):
    #Code here
    if sum(arr)==len(arr):
        return 0
    elif sum(arr)==0:
        return -1
    else:
        for i in range(len(arr)):
            if arr[i]==1:
                return i


#{ 
#  Driver Code Starts


#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))
# Contirbuted By: Harshit Sidhwa
# } Driver Code Ends