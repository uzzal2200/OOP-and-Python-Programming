s=input()
cur = ""
l=0
r=0
ans=[]
for char in s:
    cur=cur+char
    l=cur.count("L")
    r=cur.count("R")
    if l == r:
        ans.append(cur)
        cur=""
        l=0
        r=0
print(len(ans))
for char in ans:
    print(char)
