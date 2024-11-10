from collections import deque

def new_coor(old: tuple, direction: str | tuple):
    if type(direction) is str:
        direction = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}[direction]
    else:
        pass
    return old[0] + direction[0], old[1] + direction[1]

class Barrier:

    def __init__(self):
        self.__B = [[False] * 8] * 8
    
    def get_bar(self, y, x):
        i = y - 1
        j = x - 1
        return self.__B[i][j]
    
    def set_bar(self, y, x, val):
        i = y - 1
        j = x - 1
        self.__B[i][j] = val

class Snake(Barrier):

    def __init__(self, coor: tuple):
        super().__init__()
        self.head = coor
        self.set_bar(1, 1, True)
        self.tail = coor
        self.body = coor
        self.snake = deque([coor])


    def run(self, direction: str, apple: bool = False):
        if apple:
            self.head = new_coor(self.head, direction)
            self.set_bar(*self.head, True)
            self.snake.append(self.head)
            #self.snake.popleft()
        else:
            self.head = new_coor(self.head, direction)
            self.set_bar(*self.head, True)
            self.snake.append(self.head)
            self.set_bar(*self.snake.popleft(), False)
            

def is_pos_coor(y, x):
    if 1 <= y <= 8 and 1 <= x <= 8:
        return True
    else:
        return False



def f(start_point: tuple, end_point: tuple, snake: Snake) -> int:
    pass

B = Barrier()
B.set_bar(1, 1, True)

y = int(input("y: "))
x = int(input("x: "))

# if is_pos_coor(y, x):
#     print(B.get_bar(y, x))
#     print('New coor: ', new_coor((y, x), input("tomon: ")))
