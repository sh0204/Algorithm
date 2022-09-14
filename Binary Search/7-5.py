#7-5 부품 찾기

#부품이 N개
#M개 종류의 부품을 대량으로 구매


#부품을 오름차순으로 정렬한 후에 이진탐색으로 부품 종류 탐색

def binary(arr,target ,start, end):
  while start <= end:
    mid = (start+end) //2
    if arr[mid] == target :
      return mid
    elif arr[mid] > target:
      end = mid-1
    else:
      start = mid +1
  return None

n = int(input())
#부품 번호
arr = list(map(int, input().split()))
#부품 번호 오름차순 정렬
arr.sort()
#원하는 부품 갯수
m= int(input())
want =list(map(int, input().split()))

for i in want:
  result = binary(arr, i, 0, n-1)
  if result != None:
    print('yes', end = ' ')
  else:
    print('no', end = ' ')