stack = []
stack.append(5)
stack.append(4)
stack.append(1)
stack.append(2)
stack.pop()
stack.append(7)
stack.append(3)
stack.pop()

print(stack) #아래부터 출력
print(stack[::-1]) # 역으로 출력. 위부터

from collections import deque
#queue는 deque를 사용한다.
queue = deque()

queue.append(5)
queue.append(4)
queue.append(1)
queue.append(2)
queue.popleft()
queue.append(7)
queue.append(3)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 리버스로 변환
print(queue) #나중에 들어온 순서대로 출력
list(queue) #queue를 list로 저장 가능.  
