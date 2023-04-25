n = int(input())
maze = []
for i in range(n):
    maze.append(list(map(int, input().split())))

def check(x, y):
    if x < 0 or x >= n or y < 0 or y >= n or maze[x][y] == 1:
        return False
    return True

def solve_maze(x, y):
    if x == n-1 and y == n-1:
        maze[x][y] = 2
        return True
    if check(x, y):
        maze[x][y] = 2
        if solve_maze(x+1, y):
            return True
        if solve_maze(x, y+1):
            return True
        maze[x][y] = 0
        return False
    return False

print('Yes' if solve_maze(0, 0) else 'No')