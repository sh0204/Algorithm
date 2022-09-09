#6-11 성적이 낮은 순서로 학생 출력하기

#학생 이름을 성적이 낮은 순서대로 
#(학생, 점수)로 입력 받고 점수 기준으로 오름차순 정렬

n = int(input())

arr =[]
for i in range(n):
  data = input().split()
  arr.append((data[0], int(data[1]))) #점수는 정수형으로 변환

#점수를 기준으로 정렬
arr = sorted(arr, key=lambda info : info[1])

for info in arr:
  print(info[0], end = ' ')
  