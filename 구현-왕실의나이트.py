x = input()
a = x[0] # a to h a:1 b2 c3 d4 e5 f6 g7 h8
b = int(x[1]) # 1 to 8

kv = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'} 
# print(kv[8])
cnt = 0

dx =[2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]
c = kv[a]
for i in range(8):
  nx = c+dx[i]
  ny = b+dy[i]
  if(nx<1 or nx>8 or ny<1 or ny>8): continue
  cnt+=1
print(cnt)

#dictionary 말고 int(ord('a'))이용해서 더 편하게 숫자 변환가능
print(int(ord(x[0])) - int(ord('a'))+1)