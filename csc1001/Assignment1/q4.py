while True:
    try:
        row = int(input('Input your row: '))
    except:
        print('Please input an integer.')
        continue
    if row <= 0:
        print('Please input a positive nunber.')
        continue
    else:
        print('m\tm + 1\tm ** (m + 1)')
        for i in range(row):
            print('%d\t%d\t%d' % (i + 1, i + 2, (i + 1) ** (i + 2)))
        break