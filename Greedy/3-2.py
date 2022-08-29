#큰 수의 법칙
#입력 값 중에서 가장 큰 두 수만 저장해서 연속해서 더하기

#N,M,K 공백 구분하여 한줄로 입력 받기
n,m,k = map(int, input().split())
data = list(map(int,input().split()))

data.sort()
f = data[n-1]
s = data[n-2]

result = 0

while True:
  for i in range(k):
    if m == 0: # 가장 큰 수 k번 더하기
      break
    result += f
    m -= 1
  if m == 0:
    break
  result += s
  m-=1

print(result)