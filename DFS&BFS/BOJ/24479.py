#24479  알고리즘 수업 - 깊이 우선 탐색 1

#인접 정점 오름차순으로 방문
# n:정점 수 m:간선 수 r: 시작정점

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(node):
  global cnt
  #현재 노드 방문 처리
  visited[node] = cnt
  graph[node].sort() #오름차순 정렬
  #현재 노드와 연결된 다른 노드 방문
  for i in graph[node]:
    if not visited[i]:
      cnt += 1
      dfs(i)

n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited =[0] * (n+1)
cnt = 1

#2차원 배열리스트로 노드 연결 정보
for _ in range(m):
  x,y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

dfs(r)
for i in visited[1:]:
  print(i)





