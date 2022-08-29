#1이 될때 까지
# N에서 1빼기
# N을 K로 나눈다

#N이 K의 배수가 될때까지 1빼고, K로 나누기

#N,K 공백으로 구분하여 입력
n,k = map(int, input().split())
result = 0

while n >= k:
  while n % k !=0:
    n -= 1
    result += 1

  n //=k
  result +=1

while n >1 :
  n-=1
  result +=1

print(result)