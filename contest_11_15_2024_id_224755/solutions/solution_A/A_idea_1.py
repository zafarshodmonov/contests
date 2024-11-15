def input_():
    t = int(input())  # 1 <= t <= 1000
    rel = []
    for _ in range(t):
        n = int(input())  # 1 <= n <= 50
        rel.append((n, list(map(int, input().split()))))
    return rel

matrix = input_()
print(matrix)