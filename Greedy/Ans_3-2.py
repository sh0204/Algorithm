#큰 수의 법칙
#입력 값 중에서 가장 큰 두 수만 저장해서 연속해서 더하기

#N,M,K 공백 구분하여 한줄로 입력 받기
n,m,k = map(int, input().split())
data = list(map(int,input().split()))

data.sort()
f = data[n-1]
s = data[n-2]

# 가장 큰 수가 더해지는 횟수 구하기
cnt = int (m/(k+1)) * k
cnt += m %(k+1)

result = 0
result += cnt*f
result += (m-cnt)*s

print(result)