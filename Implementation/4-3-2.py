#왕실의 나이트

#8X8 좌표평면
#수직 2, 수평 1
#수평 2, 수직 1

data = list(input())
x = ord(data[0]) - ord('a')+1
y = int(data[1])

cnt = 0
dx = [-2,-2,-1,-1,1,1,2,2] #열
dy = [1,-1,2,-2,2,-2,1,-1] #행

for i in range(8):
  nx = x+dx[i]
  ny = y+dy[i]

  if 1 <= nx <= 8 and 1 <= ny <=8:
    cnt +=1

print(cnt)