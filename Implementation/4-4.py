#게임개발

#n,m 공백 구분하여 입력
n,m = map(int, input().split())

#현재 방향
x,y,dir = map(int, input().split())

#기본 좌표 설정
d =[[0] *m for _ in range(n)]

#현재 좌표
d[x][y]=1

#맵 정보
arr =[]
for i in range(n):
  arr.append(list(map(int,input().split())))
  
#북동남서 위치
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#왼쪽으로 회전
def left():
  global dir
  dir -= 1
  if dir == -1:
    dir = 3

#방문 칸 수
cnt = 1
#회전 횟수
turn = 1
while True:
  #왼쪽으로 회전
  left()
  nx = x+dx[dir]
  ny = y+dy[dir]

 #회전 후 정면에 가보지 않는 칸 
  if d[nx][ny] == 0 and arr[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    cnt += 1
    turn = 0 #회전횟수 초기화
    continue
  #회전 후 전부 바다이거나 가본 칸
  else:
    turn += 1
  #네 면 모두 갈 수 없을 때
  if turn == 4:  
    nx = x - dx[dir]
    ny = y - dy[dir]
  
    #뒤로 갈 수 있으면
    if arr[nx][ny] == 0:
      x = nx
      y = ny
    
    #뒤가 바다이면
    else:
      break
    turn = 0

print(cnt)
  