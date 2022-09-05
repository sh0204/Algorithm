#4673 셀프넘버

#n에 대하여 d(n)을 n과 n의 각 자리수를 더하는 함수
#생성자가 없는 숫자를 셀프 넘버

#set 연산 활용해서 1~100000까지 집합에서 생성자가 있는 집합 제거

all = set(i for i in range(1,10001))
self = set()

for i in range(1,10001):
  for j in str(i):
    i += int(j)
  self.add(i)


for i in sorted(all-self):
  print(i)