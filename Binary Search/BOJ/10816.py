#10816 숫자카드

      
n = int(input())
have = list(map(int, input().split()))
have.sort()
m = int(input())
want = list(map(int, input().split()))

dic = dict()

for i in have:
  if i in dic:
    dic[i]+=1
  else:
    dic[i] =1

for i in want:
  if i in dic:
    print(dic[i], end= ' ')
  else:
    print(0, end=' ')