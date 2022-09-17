#1966 프린터 큐
#숫자가 크면 중요도가 높음

t= int(input())
for _ in range(t):
  n,m = map(int, input().split())
  arr = list(map(int, input().split()))
  want =[0 for _ in range(n)]
  want[m] = 1
  cnt =0

  while True:
    if arr[0] == max(arr): #중요도가 가장 큰 값이면
      cnt += 1

      if want[0] != 1: #원하는 문서가 아니면
        del arr[0]
        del want[0]
      else: #원하는 문서라면
        print(cnt)
        break
    else:
      arr.append(arr.pop(0))
      want.append(want.pop(0))