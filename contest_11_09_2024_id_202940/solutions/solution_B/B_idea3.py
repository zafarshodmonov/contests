from itertools import permutations
from collections import deque

# Yangi koordinata qaytarish funksiyasi
def new_coor(old: tuple, direction: str | tuple):
    if type(direction) is str:
        direction = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}[direction]
    return old[0] + direction[0], old[1] + direction[1]

# 8x8 doskada harakat cheklovlari uchun yordamchi funksiya
def is_pos_coor(y, x):
    return 1 <= y <= 8 and 1 <= x <= 8

# Barrier klassi: To'siqlarni saqlash uchun
class Barrier:
    def __init__(self):
        self.__B = [[False for j in range(8)] for i in range(8)]
    
    def get_bar(self, y, x):
        return self.__B[y-1][x-1]
    
    def set_bar(self, y, x, val):
        self.__B[y-1][x-1] = val

# Ilon klassi: Ilonning harakati va tanasi uchun
class Snake(Barrier):
    def __init__(self, coor: tuple):
        super().__init__()
        self.head = coor
        self.set_bar(coor[0], coor[1], True)
        self.snake = deque([coor])

    def move(self, new_head, apple=False):
        """Ilonni berilgan yangi koordinataga olib boradi"""
        self.snake.append(new_head)
        self.set_bar(*new_head, True)  # Yangi joyni to'siq sifatida belgilash
        if not apple:  # Agar olma yemasdan harakatlansa
            tail = self.snake.popleft()  # Oxirgi qismini o'chirish
            self.set_bar(*tail, False)  # To'siqni olib tashlash
        self.head = new_head  # Boshni yangilash

# BFS yordamida ikkita nuqta orasidagi eng qisqa masofani hisoblash
def bfs(start, end, snake):
    queue = deque([(start, 0)])  # (koordinata, masofa)
    visited = set([start])
    directions = ['u', 'd', 'l', 'r']
    
    while queue:
        current, dist = queue.popleft()
        
        if current == end:
            return dist
        
        for direction in directions:
            next_pos = new_coor(current, direction)
            y, x = next_pos
            
            if is_pos_coor(y, x) and not snake.get_bar(y, x) and next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, dist + 1))
    
    return float('inf')  # Yo'l topilmasa

# Minimal yo'lni topish uchun asosiy funksiya
def minimal_snake_path(start, apples):
    min_path = float('inf')
    
    for order in permutations(apples):
        snake = Snake(start)  # Har bir tartib uchun yangi ilon yaratiladi
        total_dist = 0
        current_position = start
        
        for apple in order:
            dist = bfs(current_position, apple, snake)
            if dist == float('inf'):  # Agar yo'l topilmasa
                total_dist = float('inf')
                break
            total_dist += dist
            snake.move(apple, apple=True)  # Olmani yeb yangi boshga ko'chish
            current_position = apple
        
        min_path = min(min_path, total_dist)
    
    return min_path

# Kirish qismi
N = int(input().strip())
apples = [tuple(map(int, input().split())) for _ in range(N)]

# Chiqish qismi
start = (1, 1)
print(minimal_snake_path(start, apples))
