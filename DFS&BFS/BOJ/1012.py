#1012 유기농 배추

#상하좌우 -> 인접
#m 가로 n 세로 배추 위치개수 k
#bfs

from collections import deque
import sys
input = sys.stdin.readline

dx  =[0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x, y):
  queue = deque()
  queue.append((x,y))
  graph[x][y] = 0
  
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx< n and 0<=ny<m and graph[nx][ny] == 1: 
          queue.append((nx,ny))
          graph[nx][ny] = 0

t= int(input())
for _ in range(t):
  m,n,k = map(int,input().split())
  graph = [[0]*m for _ in range(n)]
  cnt = 0
  
  for i in range(k):
    x,y = map(int,input().split())
    graph[y][x] = 1

  for a in range(n):
    for b in range(m):
      if graph[a][b] == 1:
        bfs(a,b)
        cnt +=1

  print(cnt)