money = 1260
cnt = 0

coin =[500,100,50,10]

for i in coin:
  cnt +=  money//i
  money %= i

print(cnt)