def count_mines(field, x, y, n, m):
    count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == '*':
            count += 1
    return count

def solve_minesweeper(fields):
    field_number = 1
    for field in fields:
        n, m = len(field), len(field[0])
        print("Field #{}:".format(field_number))
        for i in range(n):
            for j in range(m):
                if field[i][j] == '*':
                    print("*", end="")
                else:
                    mines_count = count_mines(field, i, j, n, m)
                    print(mines_count, end="")
            print()
        print()
        field_number += 1

if __name__ == "__main__":
    fields = []
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        field = [input() for _ in range(n)]
        fields.append(field)
    solve_minesweeper(fields)
