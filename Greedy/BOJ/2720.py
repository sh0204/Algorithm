#2720 세탁소 사장 동혁
#쿼터 0.25 다임 0.1 니켈 0.05 페니 0.01
#손님이 받는 동전의 개수 최소

t = int(input())
money = [25,10,5,1]


for _ in range(t):
  c=int(input())
  left =[]
  for i in money:
    left.append(c//i) #몫
    c = c%i
  print(*left)