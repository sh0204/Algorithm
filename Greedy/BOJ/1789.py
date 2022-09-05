#1789 수들의 합
#서로 다른 n개의 자연수의 합 s 
#s를 알때 n의 최댓값은?

s = int(input())
cnt = 0
result = 0

while True:
  cnt += 1
  result += cnt
  if result > s:
    break

print(cnt-1)