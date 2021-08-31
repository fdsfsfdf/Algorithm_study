n,m = map(int,input().split())
mapp = []

for i in range(n):
  mapp.append(list(map(int,input())))


def dfs(a,b):
    if a<=-1 or a>=n or b<=-1 or b>=m:
      return False
    if mapp[a][b]==0:
      mapp[a][b]=1
      dfs(a-1,b)
      dfs(a,b-1)
      dfs(a+1,b)
      dfs(a,b+1)
      return True
    return False

ans =0
for a in range(n):
  for b in range(m):
    if dfs(a,b)==True:
      ans+=1

print(ans)
