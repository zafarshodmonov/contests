
def input_data():
    N, M = map(int, input().split())
    nums = [[1 if j == "." else 0 for j in i] for i in input()]
    return N, M, nums

N, M, nums = input_data()
pos = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def processing(N: int, M: int, nums: list[list[int]]) -> int:
    vis = set()
    

    def dfs(i, j):
        if (i, j) in vis:
            pass
        else:
            vis.add((i, j))
            pass
            for p in pos:
                ni = p[0] + i
                nj = p[1] + j
                if 0 <= ni < N and 0 <= nj < M:
                    dfs(ni, nj)
                    pass
                else:
                    pass
                pass
    sana = 0
    for i in range(N):
        for j in range(M):
            if (i, j) in vis:
                pass
            else:
                if nums[i][j] == 1:
                    vis.add((i, j))
                    dfs(i, j)
                    pass
                else:
                    vis.add((i, j))
                    pass
                pass
    pass

ans = processing(N, M, nums)
print(ans)