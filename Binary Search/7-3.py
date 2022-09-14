#7-3 반복문으로 구현한 이진탐색 코드

def binary_search(arr, want, start, end):
  while start <= end:
    mid = (start+want)//2
    if arr[mid] == want:
      return mid
    elif arr[mid]>want:
      end = mid-1
    else:
      start = mid + 1
  return None

n, want = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = binary_search(arr, want, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다")
else:
  print(result+1)