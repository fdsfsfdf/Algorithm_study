from collections import deque

n,m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input())))


dx = [-1, 1, 0 , 0]
dy = [0,0,-1,1]

def bfs(a,b):
  queue = deque()
  queue.append((a,b))
  while queue:
    a,b=queue.popleft()
    for i in range(4):
      na = a+dx[i]
      nb = b+dy[i]
      if na<0 or nb<0 or na>=n or nb>=m:
        continue
      if graph[na][nb]==0:
        continue
      if graph[na][nb]==1:
        graph[na][nb] = graph[a][b]+1
        queue.append((na,nb))
  return graph[n-1][m-1]

print(bfs(0,0))