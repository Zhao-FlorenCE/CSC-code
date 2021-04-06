import queue
dict = {']' : '[', '}' : '{', ')' : '('}
s = "()[]{}"
dq = queue.deque()
for i in range(len(s)):
    dq.append(s[i])
for i in range(len(s) - 1, -1, -1):
    if dq:
        if dict.get(s[i], 0) == dq[0]:
            dq.popleft()
            dq.pop()
        else: 
            print(dq)
    else:
        print(dq)