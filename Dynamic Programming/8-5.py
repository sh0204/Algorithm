#1로 만들기

#x가 5로 나눠떨어지면 5로 나눔
#3으로 나눠떨어지면 3으로 나눔
#2로 나눠떨어지면 2로 나눔
#1을 뺌

#앞에서 구한 결과값을 저장한 후에 사용

n = int(input())
dp = [0] * (n+1)

for i in range(2, n+1):
  if i % 5 == 0:
    dp[i] = min(dp[i], dp[i//5]+1 )
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i//3]+1 ) 
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i//2]+1 ) 
  dp[i] = dp[i-1]+1

print(dp[n])