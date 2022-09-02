#1931 회의실 배정

#n개의 회의
#시작시간, 끝나는 시간 주어짐
#끝나는 동시에 다른 회의 시작

#끝나는 시간 오름차순
#시작시간 오름차순

n = int(input())
time =[]

for i in range(n):
  start, end = map(int, input().split())
  time.append([start, end])
  
time = sorted(time, key = lambda x : (x[0],x[1])) #2차원 기준 여러개 적용 정렬


cnt = 0
last = 0
for start, end in time:
  if start >= last:
    cnt += 1
    last = end

print(cnt)