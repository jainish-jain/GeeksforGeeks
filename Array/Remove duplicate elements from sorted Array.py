#Your function should return an integer denoting the size of the new list
def remove_duplicate(n, arr):
    #Code here

    arr.sort()
    ls=[]
    for i in range(n):
        if arr[i] not in ls:
            ls.append(arr[i])
            print(arr[i],end=" ")
        # else:
        #     remove_duplicate(n,arr)
            
    return 0    

    






#{ 
#  Driver Code Starts
#Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        n = remove_duplicate(n, arr)
        for i in range(n):
            print (arr[i], end=" ")
        print()


# } Driver Code Ends