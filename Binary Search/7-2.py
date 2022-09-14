#7-2 재귀 함수로 구현한 이진 탐색 소스코드

#원소의 개수와 찾고자하는 문자열 입력
#전체 원소 입력 받고

def binary_search(arr, want, start, end):
  if start > end:
    return None
  mid = (start+want)//2
  if arr[mid] == want:
    return mid
  elif arr[mid] > want:
    return binary_search(arr, want, start, mid-1)
  else:
    return binary_search(arr, want, mid+1, end)
n, want = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = binary_search(arr, want, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다")
else:
  print(result+1)