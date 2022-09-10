#10867 중복 빼고 정렬하기

#n개의 정수 -> 오름차순으로 정렬
#중복 제거

n = int(input())
arr = list(map(int, input().split()))
arr = sorted(set(arr))


for i in arr:
  print(i, end= ' ')