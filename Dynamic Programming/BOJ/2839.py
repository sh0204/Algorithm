#2839 설탕 배달

#3킬로 5킬로
#n킬로 정확하게 못하면 -1 출력
#봉지 최소 개수 출력

n = int(input())

d = [-1] * 5001
d[3]=d[5] =1
for i in range(6, n+1):
  if i % 5 == 0:
    d[i] = d[i-5]+1
  elif i%3 == 0:
    d[i] = d[i-3]+1
  elif d[i-3] > 0 and d[i-5]>0:
    d[i] = min(d[i-3],d[i-5])+1

print(d[n])
