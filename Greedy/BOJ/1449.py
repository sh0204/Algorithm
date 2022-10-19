#1449 수리공 항승

n,l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

start = arr[0] - 0.5
cnt = 1

for i in range(1, len(arr)):
  if start + l >= arr[i]+0.5:
    continue
  else:
    start = arr[i]-0.5
    cnt += 1

print(cnt)