import random

class Ecosystem(object):

    def __init__(self, river = '', fish = 0, bear = 0, step = 0, length = 0, move = [-1, 0, 1, -1, 0, 1]):
        self.river = river
        self.bear = bear
        self.fish = fish
        self.step = step
        self.length = length
        self.move = move

    def set_river(self):
        self.length = int(input('Please enter the river length\n> '))
        self.fish = int(input('Please enter the fish number\n> '))
        self.bear = int(input('Please enter the bear number\n> '))
        while True:
            self.step = int(input('Please enter a valid step\n> '))
            if self.step > 0:
                break
        if self.fish + self.bear > self.length:
            print('This is not a valid ecosystem.')
            exit()
        self.river += 'F' * self.fish + 'B' * self.bear + 'N' * (self.length - self.fish - self.bear)
        self.river = random.sample(self.river, self.length)

    def simulation(self):
        temp_move = 0
        for _ in range(self.step):
            print('step', _ + 1, ''.join(self.river[__] for __ in range(len(self.river))))
            if len(set(self.river)) < 2 or (len(set(self.river)) == 2 and sorted(self.river)[len(self.river) - 1] == 'N'):
                break
            for i in range(len(self.river)):
                if temp_move == 1:
                    temp_move = 0
                    continue
                if self.river[i] == 'N':
                    continue
                else:
                    if i == 0:
                        temp_move = abs(self.move[random.randint(0, 5)])
                    elif i == len(self.river) - 1:
                        temp_move = -abs(self.move[random.randint(0, 5)])
                    else:
                        temp_move = self.move[random.randint(0, 5)]
                    print(i, self.river[i], temp_move)
                    print(self.river)
                    if self.river[i + temp_move] == self.river[i]:
                        if temp_move == 0 or len(set(self.river)) == 2:
                            continue
                        else:
                            while True:
                                random_position = random.randint(0, len(self.river) - 1)
                                if self.river[random_position] == 'N':
                                    self.river[random_position] = self.river[i]
                                    break
                        temp_move = 0
                    else:
                        if self.river[i + temp_move] > self.river[i]:
                            self.river[i + temp_move] = self.river[i]
                        else:
                            temp_move = 0
                        self.river[i] = 'N'

ecosystem = Ecosystem()