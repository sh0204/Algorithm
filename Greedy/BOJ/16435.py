#16435 스네이크버드
#과일 수 n, 초기 길이 l
#자신의 길이보다 작거나 같은 높이에 있는 과일 먹
#먹으면 1씩 길이 증가

n, l = map(int, input().split())
fru = list(map(int, input().split()))
fru.sort()


for i in range(n):
  if l >= fru[i]:
    l += 1
    
print(l)