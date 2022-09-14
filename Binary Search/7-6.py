#7-6 떡볶이 떡 만들기

#높이 h지정 -> h보다 작으면 안잘리고, 크면 잘림
#떡의 개수 n개 떡의 길이 m
# m만큼의 떡을 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값?

#시작점 0 끝점 가장 긴 떡, 중간점 잘랐을 때 나머지 값의 합이 m보다 크면 시작점을 증가

def binary(arr, m, start, end):
  result = 0
  while start<= end:
    cnt = 0
    mid = (start+end)//2
    
    for i in arr:
      if i >= mid:
        cnt += (i-mid)
    #떡의 양이 부족한 경우 -> 왼쪽 탐색
    if cnt < m:
      end = mid -1
    else:
      result = mid
      start = mid +1
  return result
  
n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

print(binary(arr, m, 0, arr[-1]))

