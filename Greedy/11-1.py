#모험가 길드
# N명의 모험가 -> 여행 떠날 수 있는 그룹의 최댓값
# 2번째 줄 각 모험가의 공포도 값

n = int(input())
data = list(map(int, input().split()))

#오름차순 정렬
data.sort()

result =0
cnt = 0

for i in data:
  cnt +=1
  if cnt >= i : #그룹에 포함된 사람이 공포도보다 크면 -> 다음 그룹으로
    result += 1 #그룹 수 증가
    cnt =0 #카운트 값 초기화

print(result)