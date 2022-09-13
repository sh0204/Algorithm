#5800 성적통계

# 각반의 수학성적, 최대 점수 최소 점수, 점수 차이 구하는 프로그램

k = int(input())

for i in range(k):
  student = list(map(int, input().split()))
  n = student[0]
  student = student[1:] 
  student.sort(reverse=True) #내림차순 정렬
  gap =[]
  for j in range(n-1):
    gap.append(student[j]-student[j+1]) #인접 값 계산
  print('Class',i+1)
  print('Max', str(max(student))+',' ,'Min', str(min(student))+',', 'Largest gap', max(gap))