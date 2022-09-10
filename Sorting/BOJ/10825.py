#10825 국영수
#국어점수 감소 순서 -> 영어 점수 증가 순서 -> 수학점수 감소 순서 -> 이름 사전 순

n = int(input())

arr = []
for _ in range(n):
  name,k,e,m = list(map(str, input().split()))
  arr.append([name,int(k),int(e),int(m)])

arr.sort(key=lambda x :(-x[1], x[2],-x[3],x[0]))

for i in arr:
  print(i[0])