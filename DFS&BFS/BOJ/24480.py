#24480 알고리즘 수업 - 깊이 우선 탐색 2
# 내림차순 방문
# n:정점 수 m:간선 수 r: 시작정점
import sys
sys.setrecursionlimit(10 ** 8)

n,m,r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = [0] * (n+1)
cnt = 1

#노드 연결 정보
for _ in range(m):
  x, y = map(int, sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(node):
  global cnt
  #현재 노드 방문 처리
  visited[node] = True
  ans[node] = cnt
  graph[node].sort(reverse = True)
  for i in graph[node]:
    if visited[i] == False:
      cnt +=1
      dfs(i)

dfs(r)
for i in ans[1:]:
  print(i)