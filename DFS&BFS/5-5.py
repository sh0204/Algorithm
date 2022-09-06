#5-5
#팩토리얼 예제 - 재귀

def fact(n):
  if n <= 1 :
    return 1
  else:
    return n*fact(n-1)


print(fact(5))