#2455 지능형 기차
#타거나 내리는 사람 수 인식 가능
# 기차 안에 사람이 가장 많을 때의 사람 수 
# 내릴 사람이 모두 내린 후에 탑승

many =[]
people = 0
for i in range(4):
  out, come = map(int, input().split())
  people += come
  people -= out
  many.append(people)

print(max(many))