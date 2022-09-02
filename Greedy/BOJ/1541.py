#1541 잃어버린 괄호

# - 기준으로 괄호치기

expr = input().split('-') #- 기준으로 나눔
result = []


for i in expr:
  num = 0
  i = i.split('+') #+ 기준으로 나눔
  for j in i:
    num += int(j) #숫자형으로 바꿔서 계산
  result.append(num)

n = result[0]
for i in range(1, len(result)):
  n -= result[i]

print(n)