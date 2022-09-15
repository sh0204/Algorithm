#10815 숫자카드

def binary(have, target,start, end):
  while start <= end:
    mid = (start+end)//2
    if have[mid] == target:
      return mid
    elif have[mid]>target:
      end = mid-1
    else:
      start = mid+1

n = int(input())
have = list(map(int, input().split()))
have.sort()
m = int(input())
want = list(map(int, input().split()))

for i in want:
  result = binary(have, i, 0, n-1)
  if result != None:
    print('1', end = ' ')
  else:
    print('0', end = ' ')

            