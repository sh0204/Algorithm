#25305 커트라인
# n명의 학생 점수가 높은 k명 상 
# 상 받는 사람 중 점수가 가장 낮은 사람의 점수?

n,k = map(int, input().split())
score = list(map(int, input().split()))
score.sort(reverse=True)

print(score[k-1])
