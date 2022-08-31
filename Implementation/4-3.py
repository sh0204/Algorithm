#왕실의 나이트

#8X8 좌표평면
#수직 2, 수평 1
#수평 2, 수직 1

#열c,행r 으로 이뤄짐
data = input()
r = int(data[1])
c = int(ord(data[0]))-int(ord('a')) + 1 

#나이트 이동 가능 방향
route = [(-2,-1),(-2,1),(2,-1),(2,1),(1,-2),(1,2),(-1,-2),(-1,2)]

#방향에 따라 가능한 경로 확인

cnt = 0
for i in route:
  #이동하고 싶은 위치
  next_r = r+i[0]
  next_c = c+i[1]
  if next_r >= 1 and next_r<= 8 and next_c<=8 and next_c>=1:
    cnt+=1

print(cnt)