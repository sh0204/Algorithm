#만들 수 없는 금액
#N개의 동전을 가지고 있음 -> 만들 수 없는 양의 정수 금액 중 최솟값

n = int(input())
data = list(map(int,input().split()))

#오름차순 정령
data.sort()

result = 1

for x in data:
  if result < x:
    break
  result += x

print(result)