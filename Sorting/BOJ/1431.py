#1431 시리얼 번호
# 짧은 순서 -> 숫자들 더해서 작은 순서 -> 사전순

n = int(input())
arr=[]
for _ in range(n):
  arr.append(input())

def sum_num(num):
  result = 0
  for i in num:
    if i.isdigit():
      result += int(i)
  return result

  
arr.sort(key=lambda x : (len(x),sum_num(x),x))
for i in arr:
  print(i)