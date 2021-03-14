from queue import PriorityQueue
import time
import os
import random

class Solution:
    @staticmethod
    def calDistance(node, w):
        dis = 0
        for i in range(len(node)):
            if node[i] == 0:
                continue
            dis += abs(i // w - (node[i] - 1) // w) + abs(i % w - (node[i] - 1) % w)
        return dis

    def solve(self, board):
        size = int(len(board) ** 0.5)
        start = tuple(board)
        process = []
        target = tuple([i for i in range(1, size ** 2)] + [0])

        pQueue = PriorityQueue()
        pQueue.put([0 + self.calDistance(start, size), start, start.index(0), 0, process])

        seen = {start}

        while not pQueue.empty():
            _pri, board, pos0, depth, process = pQueue.get()

            if board == target:
                return depth, process
            for d in (-1, 1, -size, size):
                nei = pos0 + d
                if abs(nei // size - pos0 // size) + abs(nei % size - pos0 % size) != 1:
                    continue
                if 0 <= nei < size ** 2:
                    newboard = list(board)
                    newboard[pos0], newboard[nei] = newboard[nei], newboard[pos0]
                    newt = tuple(newboard)
                    if newt not in seen:
                        seen.add(newt)
                        pQueue.put(
                            [depth + 1 + 0.9 * self.calDistance(newt, size), newt, nei, depth + 1, process + [d]])

def game_self():

    global map
    map_size = size ** 2

    map = random.sample(range(map_size), map_size)
    map_test()

def map_test():

    global zero_position, moves, is_game_start

    moves = -1
    is_game_start = False
    inversion_num = 0

    for i in range(len(map)):
        if map[i] == 0:
            zero_position = i
        for j in range(len(map) - i):
            if map[len(map) - 1 - i] < map[j] and map[len(map) - 1 - i] * map[j] != 0:
                inversion_num += 1
    if size % 2 != 0:
        if inversion_num % 2 == 0:
            is_game_start = True
        else:
            is_game_start = False
    else:
        if inversion_num % 2 == 0:
            if (size - (zero_position // size + 1)) % 2 == 0:
                is_game_start = True
            else:
                is_game_start = False
        else:
            if (size - (zero_position // size + 1)) % 2 != 0:
                is_game_start = True
            else:
                is_game_start = False

if __name__ == '__main__':

    #time.sleep(0.1)
    os.system('cls')
    global size

    while True:
        
        n = tot_time = 0
        size = int(input())
        print()
        while n < 10:

            game_self()

            while not is_game_start:
                game_self()

            t0 = time.time()
            print('>', map, time.strftime('%H:%M:%S',time.localtime(time.time())))
            print('>', Solution().solve(map))
            print('>', time.time() - t0, '\n')
            tot_time += time.time() - t0
            n += 1

        print('Average time on size', size, 'is', tot_time / 10, '\n')