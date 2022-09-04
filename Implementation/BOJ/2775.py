#2775번 부녀회장이 될테야

#a층 b호에 살려면 (a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들 데리고 살아야함

#비어있는 집X 0층부터 있고, 0층의 i호에는 i 명이 삼

t = int(input())

for i in range(t):
  k =int(input()) #층
  n =int(input()) #호
  people = [i for i in range(1,n+1)] #0층

  for i in range(k):
    for j in range(1,n):
      people[j] += people[j-1]
  print(people[-1])