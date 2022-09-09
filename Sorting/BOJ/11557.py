#11557 Yangjojang of The Year

t = int(input())

for _ in range(t):
  n = int(input())
  arr=[]
  for _ in range(n):
    data = input().split()
    arr.append((data[0], int(data[1]))) #술의 양은 정수형으로 변환

  #술의 양을 기준으로 정렬
  arr = sorted(arr, key= lambda info : info[1])
  print(arr[-1][0])