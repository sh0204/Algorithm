# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
  #특정 노드가 위치를 벗어나면 종료
  if x == -1 or x == n or y == -1 or y == m :
      return False
  #방문하지 않았던 노드이면 방문
  if graph[x][y] == 0:
      #해당 노드는 방문 처리
      graph[x][y] == 1
      #상하좌우 dfs 호출
      dfs(x-1, y)
      dfs(x,y-1)
      dfs(x+1, y)
      dfs(x,y+1)
      return True
  return False

result =0

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print(result)