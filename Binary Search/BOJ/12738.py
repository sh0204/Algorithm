#12738 가장 긴 증가하는 부분 수열3

from bisect import bisect_left

a= int(input())
arr = list(map(int, input().split()))

ans =[]

for num in arr:
  k = bisect_left(ans, num)
  if len(ans) == k:
    ans+=[num]
  else:
    ans[k] = num

print(len(ans))