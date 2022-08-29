#숫자 카드 게임
# N: 행 M : 열
# 행선택 -> 가장 낮은 숫자 카드 뽑
# min 함수 이용


#N, M 공백으로 나눠서 한 줄 출력
n,m = map(int, input().split())
result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  # 행들 중에서 가장 작은 값 뽑 -> 그 중 가장 큰 값
  result = max(result, min_value)

print(result)