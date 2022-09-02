# 9237 이장님 초대

# 묘목 하나 심는데 걸리는 시간 1일
# 최소 자라는기간으로

n = input()
grow = list(map(int, input().split()))
grow.sort(reverse =True) #내림차순 정렬

for i in range(len(grow)):
  grow[i] = grow[i]+ i+1

print(max(grow)+1) #이장님은 다음날