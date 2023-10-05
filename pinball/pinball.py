import numpy as np

def get_input():
    segments = []
    n = int(input())
    for _i in range(n):
        row = input().split()
        segments.append((int(row[0]), int(row[1]), int(row[2]), int(row[3])))
    start_pos = int(input())

    return start_pos, segments


def is_collision(pos_x, segment):
    # Calculate dot product
    a0 = [segment[0], segment[1]]
    a1 = [segment[2], segment[3]]
    b0 = [pos_x, 1]
    b1 = [pos_x, segment[1]-10]
    # print('a0: {}, a1: {}, b0: {}, b1: {}'.format(a0, a1, b0, b1))


    return True


def get_segment_direction(segment):
    if segment[0] < segment[2]:
        print('- Right')
        return 1
    else:
        print('- Left')
        return -1
    return 0


def main():
    pos_x, segments = get_input()
    for segment in segments:
        if not is_collision(pos_x, segment):
            continue

        direction = get_segment_direction(segment)
        assert(direction != 0)
        pos_x += direction

    print(pos_x)
    return pos_x


if __name__ == '__main__':
    main()
