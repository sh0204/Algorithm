#11725 트리의 부모 찾기
#BFS 사용
#루트 없는 트리가 주어졌을 때 이때 트리의 루트가 1
#각 노드의 부모를 구하는 프로그램

from collections import deque

#노드의 개수
n = int(input())

#parent 배열 만들어서 부모노드 표시

graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

def bfs(node):
  queue = deque()
  queue.append(node)

  while queue:
    #큐에서 하나 원소 뽑아서 출력
    v = queue.popleft()
    for i in graph[v]:
      #해당 원소와 연결된 아직 방문하지 않은 원소를 큐에 삽입
      #해당 원소는 부모 노드
      if parent[i] == 0:
        parent[i] = v
        queue.append(i)

for _ in range(n-1):
  a, b= map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

#시작노드 = 1
bfs(1)

for i in parent[2:]:
  print(i)