alphabets = ["A", "B", "C", "D", "E", "F", "G", "H"]
board = []

WIDTH = 8
HEIGHT = 8
user_input = input("Please select a coordinate: ")

coordinate = (alphabets.index(user_input[0].upper()),
              HEIGHT - int(user_input[1]))

for height in range(HEIGHT):
    board.append([])
    for width in range(WIDTH):
        board[height].append(f"{alphabets[width]}{HEIGHT - height}")

board[coordinate[1]][coordinate[0]] = "KN"

for x, y in [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]:

    if (coordinate[0] + x >= 0 and coordinate[0] + x <= 7) and (coordinate[1] + y >= 0 and coordinate[1] + y <= 7):
        board[coordinate[1] + y][coordinate[0] + x] = "XX"

for height in range(HEIGHT):
    for width in range(WIDTH):
        print(board[height][width], end=" ")
    print()