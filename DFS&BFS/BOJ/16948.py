#16948 데스 나이트

#최소 이동 횟수

from collections import deque

#bfs
def bfs(x,y):
  queue = deque()
  queue.append([x,y])
  while queue:
    x,y = queue.popleft()
    for i in range(6):
      nx = x+dx[i]
      ny = y+dy[i]
      #방문하지 않았다면
      if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
        #노드 1추가
        visited[nx][ny] = visited[x][y] + 1
        if nx == r2 and ny == c2:
          return visited[nx][ny]
        queue.append((nx,ny))
  return -1

#방향
dx= [-2,-2,0,0,2,2]
dy= [-1,1,-2,2,-1,1]

n = int(input())
r1,c1,r2,c2 = map(int, input().split())

#이동횟수 체크
visited =[[0]*n for _ in range(n)]
print(bfs(r1,c1))


