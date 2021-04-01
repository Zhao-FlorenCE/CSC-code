s = ''
location = dict()
appearance = dict()
i = 0
ans = 0
while i < len(s):
    appearance[s[i]] = appearance.get(s[i], 0) + 1
    location[s[i]] = i
    try:
        if appearance.get(s[i + 1], 0) == 1:
            ans = max(i + 1 - location[s[i + 1]], ans)
            i = location[s[i + 1]]
            appearance.clear()
            location.clear()
    except:
        break
    i += 1
print(ans)