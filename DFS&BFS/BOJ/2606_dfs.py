#2606 바이러스

#dfs

n = int(input())
con = int(input())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(con):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

result =[]
def dfs(start):
  global cnt
  visited[start] = 1
  for i in graph[start]:
    if visited[i] == 0:
      result.append(i)
      dfs(i)
  return len(result)

print(dfs(1))