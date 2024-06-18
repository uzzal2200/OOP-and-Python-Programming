n=int(input())
arr=list(map(int,input().split()))
nums={}
for num in arr:
    if( num not in nums):
        nums[num]=0
    nums[num] += 1

#print(nums)
t=0
for key,val in nums.items():
    if(val > key):
        t=t+val-key
    elif(val < key):
        t=t+val
print(t)