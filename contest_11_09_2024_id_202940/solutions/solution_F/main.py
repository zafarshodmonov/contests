
def input_data():
    N, M = map(int, input().split())
    nums = [[1 if j == "." else 0 for j in input()] for i in range(N)]
    return N, M, nums

N, M, nums = input_data()
pos = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def processing(N: int, M: int, nums: list[list[int]]) -> int:
    vis = [[False] * M for _ in range(N)]
    def dfs(i, j):
        if vis[i][j]:
            pass
        else:
            vis[i][j] = True
            for p in pos:
                ni = p[0] + i
                nj = p[1] + j
                if 0 <= ni < N and 0 <= nj < M:
                    if nums[ni][nj] == 1:
                        dfs(ni, nj)
                    else:
                        vis[ni][nj] = True
    sana = 0
    for i in range(N):
        for j in range(M):
            if vis[i][j]:
                pass
            else:
                if nums[i][j] == 1:
                    sana += 1
                    dfs(i, j)
                else:
                    vis[i][j] = True
    return sana

ans = processing(N, M, nums)
print(ans)