import math
import heapq

def find_divisors(n):
    divisors = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors += 1
            if i != n // i:
                divisors += 1
    return divisors

N = int(input())

def processing(N):
    heap = []
    for i in range(1, N + 1):
        chipta_balli = find_divisors(i)
        heapq.heappush(heap, (chipta_balli, i))
    
    top = heap[0][0]
    res = []
    while heap:
        item = heapq.heappop(heap)
        if item[0] == top:
            res.append(item[1])
        else:
            break
    return res

for i in processing(N):
    print(i)
