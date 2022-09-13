#7568 덩치
#몸무게 x 키 y (x,y)

n = int(input())
student =[]

for i in range(n):
  x,y = map(int,input().split())
  student.append((x,y))

for i in student:
  cnt = 1
  for j in student:
    if i[0] < j[0] and i[1] < j[1]:
      cnt += 1

  print(cnt, end =' ')