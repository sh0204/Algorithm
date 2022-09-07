#14716 현수막
# 글자 -> 1 글자 아닌 부분 0
# 1이 상하좌우 대각선 연결되어 있으면 하나의 글자
# bfs로 탐색하다가 방문하지 않은 1이 있으면 글자 수 하나 증가 거기서 또 bfs 실시

from collections import deque
m, n = map(int, input().split()) #행 열
graph = [list(map(int, input().split())) for _ in range(m)]

#방향
dx = [-1,-1,-1,1,1,1,0,0]
dy = [-1,0,1,-1,0,1,-1,1]

def bfs(x,y):
  queue = deque()
  queue.append([x,y])
  graph[x][y] = 0
  while queue:
    x,y = queue.popleft()
    for i in range(8):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx <m and 0<=ny<n and graph[nx][ny] == 1:
        queue.append([nx,ny])
        graph[nx][ny] = 0
        
cnt = 0
for i in range(m):
  for j in range(n):
    if graph[i][j] == 1:
      bfs(i,j)
      cnt+=1
      
print(cnt)