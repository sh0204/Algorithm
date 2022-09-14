def search(n,arr,array):
  for i in range(n):
    if array[i] == arr:
      return i+1

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
data = input().split()
n = int(data[0])
arr = data[1] #찾을 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(search(n,arr,array))