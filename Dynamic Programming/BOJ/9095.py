# 9095 1,2,3 더하기

t = int(input())

def dp(n):
  if n ==1:
    return 1
  elif n == 2:
    return 2
  elif n ==3 :
    return 4
  else:
    return dp(n-1)+dp(n-2)+dp(n-3)

for _ in range(t):
  n = int(input())
  print(dp(n))