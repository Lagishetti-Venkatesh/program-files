arr_size, test =map(int, input().split())
arr = [0]*(arr_size+1)
for i in range(test):
    s, e, v = map(int, input().split())
    arr[s-1] += v
    if(e <= len(arr)): arr[e] -= v
x = max = 0
for i in arr:
   x=x+i;
   if(max<x): max=x;
print(max)
