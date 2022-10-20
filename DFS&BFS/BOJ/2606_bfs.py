#2606 바이러스

#bfs

from collections import deque

n = int(input())
con = int(input())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 0
for _ in range(con):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(graph, v):
  global cnt
  q = deque([v])
  
  while q:
    virus = q.popleft()
    visited[virus] = 1
    for i in graph[virus]:
      if visited[i] == 0:
        visited[i] = 1
        q.append(i)
        cnt += 1

  print(cnt)

bfs(graph, 1)