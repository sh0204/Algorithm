# 곱하기 혹은 더하기
# * + 연산자를 넣어 가장 큰 수를 구하는 프로그램 작성
# 왼쪽 부터 순서대로


s = input()

#첫번째 문자를 숫자로 변경
result = int(s[0]) 

for i in range(1, len(s)):
  # 두 수 중 하나라도 1이하인 경우
  num = int(s[i])
  if num <= 1 or result <=1:
    result += num
  else:
    result *= num

print(result)
