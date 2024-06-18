n=int(input())
ar=list(map(int,input().split()))
flag = True
count=0;
while flag is True:
    for i,num in enumerate(ar):
        if(num % 2 == 1):
            flag = False
            break
        else:
            ar[i]/=2
    if(flag):
        count += 1
print(count)
