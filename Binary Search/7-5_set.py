#7-5 부품 찾기

#부품이 N개
#M개 종류의 부품을 대량으로 구매

#set 활용
#특정한 수가 한번이라도 등장했는지 검사하면 되기 때문에 집합 자료형 사용

n = int(input())
arr = set(map(int, input().split()))
m = int(input())
x = list(map(int,input().split()))

#손님이 확인 요청한 부품 번호 하나씩 확인
for i in x:
  if i in arr:
    print('yes', end = ' ')
  else:
    print('no', end = ' ')