#7-5 부품 찾기

#부품이 N개
#M개 종류의 부품을 대량으로 구매

#계수 정렬

n = int(input())
#부품 번호
arr = [0] * 100000001

#가게에 있는 부품 번호 입력받아서 기록
for i in input().split():
  arr[int(i)] = 1

m = int(input())
#전체 부품 번호 공백으로 구분하여 입력
x = list(map(int, input().split()))

#손님이 확인 요청한 부품 번호 하나씩 확인
for i in x:
  if arr[i] == 1:
    print('yes', end =' ')
  else:
    print('no', end = ' ')