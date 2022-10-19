#10797 10부제

day = int(input())
car = list(map(int, input().split()))

cnt =0
for i in range(len(car)):
  if car[i] == day:
    cnt+=1
  else:
    continue

print(cnt)


day = int(input())
car = list(map(int, input().split()))
print(car.count(day))