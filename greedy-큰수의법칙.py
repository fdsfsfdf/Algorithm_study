N,M,K =input().split()
n = int(N)
m = int(M)
k = int(K)

no = list(map(int,input().split()))
no.sort(reverse=True)

sum = 0
cnt = 0
h = True
t = m
while h:
  for i in range(k):
    if t==0:
      h = False
      break
    sum += no[0]
    t=t-1
    
  if t>=1:
    sum+=no[1]
    t = t-1
print(sum)


  
