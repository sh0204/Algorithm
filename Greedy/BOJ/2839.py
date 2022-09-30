#2839 설탕 배달

#3킬로 5킬로
#n킬로 정확하게 못하면 -1 출력
#봉지 최소 개수 출력

n = int(input())
bag = 0

while True:
  if n%5 == 0:
    bag+= n/5
    print(int(bag))
    break
  n-=3
  bag+=1

  if n<0:
    print(-1)
    break
    