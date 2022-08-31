#시각
#정수 N이 입력되면 N시 59분 59초까지 3이 포함되면 체크

#시각을 문자열로 바꿔서 3이 포함되었는지 체크

n = int(input())

cnt = 0
for i in range(n+1): #시간
  for j in range(60): #분
    for k in range(60): #초
      if '3' in str(i)+str(j)+str(k):
        cnt += 1


print(cnt)