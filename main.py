# Día 1
# Puzle 1
def read_dataset():
    depths = open("data_day1.txt", "r").readlines()
    return depths


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


test_depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

if __name__ == '__main__':
    depths = read_dataset()
    print(count_increases_in_depth(depths))
    print(count_in_windows(depths))
