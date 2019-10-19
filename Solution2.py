n = int(input())
tr = list(map(int, input().split()))
i,j = tuple(map(int, input().split()))
s = 0
for k in range(i,j+1):
    s += tr[k]
print(s)    
