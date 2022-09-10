#2628 종이자르기

#종이 가로, 세로 길이, 잘라야할 점선 -> 가장 큰 종이 조각 넓이?
#가로로 자르는 점선은 (0,잘라야할 번호), 세로로 자르는 점선은 (1,잘라야할 번호)

#가로 x 세로 y

x, y = map(int, input().split())
x_cut=[0,x]
y_cut=[0,y]

for _ in range(int(input())):
  a,b = map(int, input().split())
  if a == 0: #가로로 자르는 선
    y_cut.append(b)
  elif a == 1: #세로로 자르는 선
    x_cut.append(b)

x_cut.sort()
y_cut.sort()    

#옆의 값과 비교해서 차가 가장 큰것 골라주기

sub_x=[]
sub_y=[]
for i in range(len(x_cut)-1):
  sub_x.append(x_cut[i+1]- x_cut[i])
for i in range(len(y_cut)-1):
  sub_y.append(y_cut[i+1]- y_cut[i])

print(max(sub_x)*max(sub_y))