#2512 예산

# 최대의 총 예산
#상한액을 정해서 그 이하면 요청 금액 주고, 그 이상이면 상한액으로

def binary(start, end):
  while start<= end:
    mid = (start+end)//2
    result = 0
    for i in arr:
      if i > mid:
        result += mid
      else:
        result += i
    if result <= total: #총 금액보다 결과가 작으면 더 상한액을 높여서
      start = mid+1
    else:
      end = mid-1
  return end
  
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
total = int(input())

print(binary(0,arr[-1]))