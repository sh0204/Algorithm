#9625 BABBA

#A->B->BA ->BAB -> BABBA
# B->BA A->B로 바뀜

k = int(input())
a=[1]
b=[0]

for i in range(k):
  a.append(b[i])
  b.append(a[i]+b[i])

print(a[-1], b[-1],end=' ')