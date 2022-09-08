#24444 알고리즘 수업 - 너비 우선 탐색 1

#bfs 정점 1부터 시작해서 너비 우선 탐색으로 방문하여 노드의 방문순서 출력
#n: 정점 수 , m = 간선 수, r: 시작정점

from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited =[0]*(n+1)
visited[r] = 1
cnt = 1

#노드 정보 입력
for _ in range(m):
  x,y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs(node):
  global cnt
  queue = deque()
  queue.append(node)

  while queue:
    v = queue.popleft()
    graph[v].sort() #오름차순 정렬
    #해당 원소와 연결된 정점 중 아직 방문하지 않았다면
    for i in graph[v]:
      if not visited[i]:
        cnt +=1
        queue.append(i)
        visited[i] = cnt
  

bfs(r)
for i in visited[1:]:
  print(i)