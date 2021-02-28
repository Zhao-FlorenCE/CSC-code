row = int(input('Input your row: '))

if row > 0:
    print('m\tm + 1\tm ** (m + 1)')
    for i in range(row):
        print('%d\t%d\t%d' % (i + 1, i + 2, (i + 1) ** (i + 2)))
else:
    print('Please input a positive nunber.')