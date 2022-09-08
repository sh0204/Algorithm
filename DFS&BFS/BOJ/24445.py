#24445 알고리즘 수업 - 너비 우선 탐색 2

#bfs 정점 1부터 시작해서 너비 우선 탐색으로 방문하여 노드의 방문순서 출력

from collections import deque
import sys

def bfs(node):
  global cnt
  queue = deque()
  queue.append(node)
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      #해당 원소와 연결된 아직 방문하지 않은 원소를 큐에 삽입
      if not visited[i]:
        cnt += 1
        visited[i] = cnt
        queue.append(i)

  return 0
      
#n: 정점 수 , m = 간선 수, r: 시작정점
n,m,r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
visited[r] = 1
cnt = 1

#맵정보 입력
for _ in range(m):
  x, y = map(int, sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)

#내림차순 정렬
for i in range(1, n+1):
  graph[i].sort(reverse = True)

bfs(r)
for i in visited[1:]:
  print(i)