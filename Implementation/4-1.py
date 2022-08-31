#공간 크기 입력
n = int(input())
#시작 위치
x,y =1,1
#계획
plan =input().split()

#LRUD 에 따른 위치 변화
dx = [0,0, -1,1]
dy = [-1,1,0, 0]
move = ['L','R','U','D']

for i in plan:
  for j in range(len(move)):
    if i == move[j]:
      nx = x+dx[j]
      ny = y+dy[j]
  #공간 벗어나는 경우 무시
  if nx <1 or ny <1 or nx > n or ny > n:
    continue

  x = nx
  y = ny

print(x, y)