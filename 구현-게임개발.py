n,m = map(int,input().split())
a,b,d = map(int,input().split())
mapp=[]
gocnt = 0
for i in range(n):
  mapp.append(list(map(int,input().split())))

dx=[0,1,0,-1]
dy=[-1,0,1,0]
# print(mapp)
# 0 - 육지, 1- 바다
# d 0 - 북 1-동 2-남 3-서

cnt = 1
def turn():
  global d
  d=d-1
  if d==-1:
    d =3

def go():
  global a,b,gocnt,cnt,dx,dy

  na= a+dy[d]
  nb = b+dx[d]
  gocnt+=1
  if(mapp[na][nb]==0):
    a = na
    b = nb
    gocnt-=1
    cnt+=1
  

orgina=a
orginb=b
while True: 
  turn()
  go()
  if(gocnt==4):
    na = a-dy[d]
    nb = b-dx[d]
    if(mapp[na][nb]==1):
      break;
print(cnt)


### 방문한 위치 저장이 고려가 안되었음.
### 아래는 정답
