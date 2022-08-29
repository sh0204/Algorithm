#볼링공 고르기

#볼링공 무게 1~M
#볼링공 총 N개

#무게마다 몇개의 볼링공 있는지 체크

n,m = map(int,input().split())
data = list(map(int, input().split()))

#무게 담을 수 있을 리스트
arr  = [0] * 11

for x in data:
  #무게에 해당하는 볼링볼 카운트
  arr[x] += 1

result = 0
#1부터 M까지의 무게 처리
for i in range(1, m+1):
  n -= arr[i] #A가 선택할 수 있는 갯수 제거
  result += arr[i] * n #B가 선택할 수 있는 갯수와 곱

print(result)
