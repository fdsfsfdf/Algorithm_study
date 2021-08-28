N,M = map(int,input().split())

cnt =0
while N!=1:
  if N/M == N//M:
    N=N/M
    cnt+=1
  else:
    N=N-1
    cnt+=1
print(cnt)

#1을 빼는 동작이 개별 동작이므로 n이 100억 이상이 될 경우 문제가 생김. 
#빠르게 동작하려면 N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 소스코드 작성 필요.
