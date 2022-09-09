#9076 점수 집계
t = int(input())
for i in range(t):
  arr = list(map(int,input().split()))
  arr.sort() #오름차순 정렬

  if arr[3]- arr[1] >= 4:
    print('KIN')
  else:
    print(sum(arr[1:4]))