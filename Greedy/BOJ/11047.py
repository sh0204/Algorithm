#동전 0

#n종류의 동전 이용해서 가치의 합을 k로 
#동전 개수의 최솟값은?


#첫째줄 n,k
#2~n개줄 가치 오름차순으로 

n,k = map(int, input().split())
cost =[]


for i in range(n):
  cost.append(int(input()))
cost.sort(reverse=True) #내림차순 정렬

cnt = 0

for i in cost:
  if k >= i :
    cnt = cnt + k // i #몫만큼 더해줌    
    k = k%i #나머지 할당
    if k <= 0:
      break

print(cnt)