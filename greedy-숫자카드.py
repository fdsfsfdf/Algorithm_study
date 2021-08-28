n, m = map(int,input().split())
ans = []
for i in range(n):
  row =list(map(int,input().split()))
  row.sort()
  ans.append(row)
ans2 = []
for i in range(n):
  ans2.append(ans[i][0])
ans2.sort(reverse=True)
print(ans2[0])


#min - list에서 가장 작은 원소 리턴
