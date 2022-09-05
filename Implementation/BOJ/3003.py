#3003 킹, 퀸,룩, 비숍, 나이트, 폰
#     1   1  2    2     2    8
#양수 -> 피스 더해줌
#음수 -> 제거 해줌

ans = [1,1,2,2,2,8]
arr = list(map(int, input().split()))

for i in range(6):
  print(ans[i]-arr[i], end =' ')