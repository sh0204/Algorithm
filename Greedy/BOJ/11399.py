#ATM

#사람이 인출하는데 필요한 시간의 합의 최솟값
# 인출하는데 걸리는 시간이 가장 짧은 사람 순서대로 정렬해서 더해줌

#첫째줄 : N명
#둘째줄 : 걸리는 시간 p


n= int(input())
p = list(map(int, input().split()))
p.sort()

result = 0
for i in range(n):
  for j in range(i+1):
    result += p[j]

print(result)