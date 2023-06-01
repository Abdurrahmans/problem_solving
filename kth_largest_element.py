def ktn_larget(arr,k):
    n = len(arr)
    arr.sort()
    return arr[n-k]
k = 2
arr =[1,2,3,4,5,6,7,7,9]
print(ktn_larget(arr,k))
