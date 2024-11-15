from collections import deque


class Barrier:

    def __init__(self):
        self.__B = [[False for j in range(8)] for i in range(8)]
    
    def get_bars(self):
        return self.__B
    
    def get_bar(self, coor):
        i = coor[0] - 1
        j = coor[1] - 1
        return self.__B[i][j]
    
    def set_bar(self, coor, val):
        i = coor[0] - 1
        j = coor[1] - 1
        self.__B[i][j] = val


class Snake(Barrier):

    def __init__(self, coor: tuple):
        super().__init__()
        self.head = coor
        self.set_bar((1, 1), True)
        #self.tail = coor
        #self.body = coor
        self.snake = deque([coor])

    def new_coor(self, old: tuple, direction: str | tuple):
        if type(direction) is str:
            direction = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}[direction]
        else:
            pass
        return old[0] + direction[0], old[1] + direction[1]

    def run(self, direction: str, apple: bool = False):
        new = self.new_coor(self.head, direction)
        if apple:
            if self.is_pos_coor(new):
                self.head = new
                self.set_bar(self.head, True)
                self.snake.append(self.head)
                #self.snake.popleft()
        else:
            if self.is_pos_coor(new):
                self.head = new
                self.set_bar(self.head, True)
                self.snake.append(self.head)
                self.set_bar(self.snake.popleft(), False)
            

    def is_pos_coor(self, coor):
        y = coor[0]
        x = coor[1]
        if 1 <= y <= 8 and 1 <= x <= 8:
            return True
        else:
            return False


def bfs(start_point: tuple, end_point: tuple, snake: Snake) -> int:
    queue = deque([(start_point, 0)])  # (current_position, distance)
    visited = set([start_point])
    directions = ['u', 'd', 'l', 'r']

    while queue:
        current, dist = queue.popleft()
        
        if current == end_point:
            #snake.run(current, True)
            return dist
        
        for direction in directions:
            next_pos = snake.new_coor(current, direction)
            
            if snake.is_pos_coor(next_pos) and not snake.get_bar(next_pos) and next_pos not in visited:
                apple = True if next_pos == end_point else False
                snake.run(direction, apple)
                #print("snake: ", snake.snake)
                visited.add(next_pos)
                queue.append((next_pos, dist + 1))
    
    return -1  # Agar yo'l topilmasa

def inp():
    rel = []
    n = int(input())
    for i in range(n):
        y, x = map(int, input().split())
        rel.append((y, x))
    return rel

sana = 0
pos_cor = inp()
snake = Snake((1, 1))
dast = (1, 1)
for p in pos_cor:
    m = bfs(dast, p, snake)
    dast = p
    #print("m: ", m)
    if m > 0:
        sana += m
    else:
        pass
print(snake.get_bars())
print(sana)
print(snake.head)
