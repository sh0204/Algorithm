# 6-10 위에서 아래로

# 하나의 수열에 다양한 수 존재. 큰수 부터 작은 순서로 정렬
# 수열을 내림 차순으로 정렬하는 프로그램 자성

#n입력
n= int(input())
#n개의 정수 리스트에 저장
arr = []
for i in range(n):
  arr.append(int(input()))

#파이썬 기본 라이브러리 정렬 사용
arr = sorted(arr, reverse=True) #내림차순

for i in range(n):
  print(arr[i], end=' ')