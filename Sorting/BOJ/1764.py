# 1764 듣보잡

n,m = map(int, input().split())
cl = set()
cs = set()

for _ in range(n):
  cl.add(input())
for _ in range(m):
  cs.add(input())

arr = list(cl&cs)
arr.sort()
print(len(arr))
print(*arr,sep='\n')