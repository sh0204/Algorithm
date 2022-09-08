#4963 섬의 개수

# 가로 세로 또는 대각선으로 연결되어 있으면 걸어갈 수 있음

from collections import deque
import sys
input = sys.stdin.readline

dx =[-1,-1,-1,0,0,1,1,1]
dy =[-1,1,0,-1,1,-1,1,0]
def bfs(x,y):
  queue = deque()
  queue.append([x,y])

  while queue:
    a,b = queue.popleft()
    #해당 원소와 연결되었는데 1이면서 방문하지 않은 원소 큐에 삽입
    for i in range(8):
      nx = a+dx[i]
      ny = b+dy[i]
      if 0<= nx < h and 0<= ny < w and graph[nx][ny] == 1:
        graph[nx][ny]= 0
        queue.append([nx, ny])


  
while True:
  #w:너비 h:높이
  w,h = map(int, input().split())
  if w == 0 and h == 0:
    break
  # 지도 입력
  graph = [list(map(int, input().split())) for _ in range(h)]
  cnt = 0

  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1:
        bfs(i, j)
        cnt +=1
  print(cnt)