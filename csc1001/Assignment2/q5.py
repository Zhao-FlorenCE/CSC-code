lock = [0] * 100
i = 1
while i <= 100:
    j = 0
    while j < 100:
        lock[j] = not lock[j]
        j += i
    i += 1
ans = 0
for i in range(100):
    if lock[i]:
        ans += 1
print(ans)