# Día 1
# Puzle 1
def read_dataset(file):
    data = open(file, "r").readlines()
    return data


def count_increases_in_depth(depths):
    increase = 0
    aux = 0
    for i in depths:
        if aux != 0:
            if aux < int(i):
                increase += 1
        aux = int(i)
    return increase


# Puzle 2
def count_in_windows(depths):
    previous_window = int(depths[0]) + int(depths[1]) + int(depths[2])
    increase = 0
    for i in range(1, len(depths) - 2):
        current_window = int(depths[i]) + int(depths[i + 1]) + int(depths[i + 2])
        if previous_window < current_window:
            increase += 1
        previous_window = current_window
    return increase


# Día 2
# Puzle 1
def calculate_position(moves):
    horizontal = 0
    depth = 0
    for move in moves:
        move.splitlines()
        if move[0] is "f":
            horizontal += int(move[8])
        if move[0] is "u":
            depth -= int(move[3])
        if move[0] is "d":
            depth += int(move[5])
    return horizontal*depth


# Puzle 2
def calculate_position_with_aim(moves):
    aim = 0
    horizontal = 0
    depth = 0
    for move in moves:
        move.splitlines()
        if move[0] is "f":
            horizontal += int(move[8])
            depth += aim * int(move[8])
        if move[0] is "u":
            aim -= int(move[3])
        if move[0] is "d":
            aim += int(move[5])
    return horizontal*depth


if __name__ == '__main__':
    moves = read_dataset("data_day2.txt")
    print(calculate_position(moves))
    print(calculate_position_with_aim(moves))
