n=int(input())
arr=list(map(int,input().split()))
# find minimum numver
num_min=min(arr)
num_max=max(arr)
# find index
mn_index=arr.index(num_min)
mx_index=arr.index(num_max)
# swap maximum and minimum index
arr[mn_index],arr[mx_index]=arr[mx_index],arr[mn_index]
# print the modified array
print(*arr)
