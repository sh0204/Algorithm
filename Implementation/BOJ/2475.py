#2475 검증수
#컴퓨터마다 6자리의 고유번호
#6번째 자리에 검증수
#검증수는 5개의 숫ㅅ자를 각각 제곱한 수의 합을 10으로 나눈 나머지

num = list(map(int, input().split()))

result = 0
for i in range(len(num)):
  result += pow(num[i], 2)
  result %= 10

print(result)