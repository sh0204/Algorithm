#7562 나이트의 이동

from collections import deque
import sys
input = sys.stdin.readline

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

def bfs(sx, sy, ex, ey):
  queue = deque()
  queue.append([sx,sy])
  #현재 노드 방문 처리
  visited[sx][sy] = 1

  while queue:
    x,y = queue.popleft()
    #최종적인 결과값과 같을 경우
    if x == ex and y == ey:
      print(visited[ex][ey]-1)
      return
    for i in range(8):
      nx = x+dx[i]
      ny = y+dy[i]

      if 0<=nx<n and 0<=ny<n and visited[nx][ny] ==0:
        queue.append([nx,ny])
        visited[nx][ny] = visited[x][y]+1

  
#테스트케이스 갯수
t = int(input())
for i in range(t):
  #체스판 크기
  n = int(input())
  #현재 위치
  sx, sy = map(int, input().split())
  #이동 위치
  ex, ey = map(int, input().split())
  visited = [[0]*n for i in range(n)]
  bfs(sx, sy, ex, ey)


