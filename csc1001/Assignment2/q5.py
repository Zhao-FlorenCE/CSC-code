# Initialize the state of the locker are locked
lock = [0] * 100
i = 1
# Change the statement of the lockers
while i <= 100:
    j = i - 1
    while j < 100:
        lock[j] = not lock[j]
        j += i
    i += 1
# Print the solution of the problem
ans = 0
answer = str()
for i in range(100):
    if lock[i]:
        ans += 1
        lock[i] = 'L' + str(i + 1) + ': open'
        answer += str(i + 1) + ' '
    else:
        lock[i] = 'L' + str(i + 1) + ': locked'
print('%d lockers are open.' % ans)
print('The serial of the open lockers are:\n', answer.split(), sep = '')
print('This is the detailed information:\n', lock, sep = '')