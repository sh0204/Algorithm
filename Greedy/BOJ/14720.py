#14720 우유축제

# 딸 -> 초 -> 바 -> 딸

# 0 : 딸, 1 : 초, 2: 바

#마실 수 있는 우유 최대 개수

n = int(input())
milk = list(map(int, input().split()))

cnt = 0
for i in range(n):
  if milk[i] == cnt %3:
    cnt +=1

print(cnt)