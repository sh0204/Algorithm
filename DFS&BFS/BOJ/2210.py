# 2210 숫자판 점프
# DFS

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x,y,num):
  if len(num) == 6:
    if num not in result:
      result.append(num)
    return 
  
  dx = [0,0,-1,1]
  dy = [-1,1,0,0]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx<0 or nx>=5 or ny<0 or ny>=5:
      continue
    else:
      dfs(nx,ny,num+board[nx][ny])
  
board = []
for i in range(5):
  board.append(list(map(str, input().split())))

result = []
for i in range(5):
  for j in range(5):
    dfs(i, j, board[i][j])
print(len(result))