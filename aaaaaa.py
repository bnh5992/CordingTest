from collections import defaultdict

def move_fireball(n, m, k, fireballs):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    board = defaultdict(int)

    for i in range(m):
        x, y, power, speed, direction = fireballs[i]
        while k >= speed:
            x += dx[direction-1] * speed
            y += dy[direction-1] * speed
            k -= speed

            if x < 0 or x >= n or y < 0 or y >= n:
                break
            board[(x, y)] += power

        if x < 0 or x >= n or y < 0 or y >= n:
            continue
        x += dx[direction-1] * k
        y += dy[direction-1] * k
        board[(x, y)] += power

    return sum(board.values())

n, m, k = map(int, input().split())
fireballs = [list(map(int, input().split())) for _ in range(m)]
print(move_fireball(n, m, k, fireballs))