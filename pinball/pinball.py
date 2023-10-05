
def get_input():
    segments = []
    n = int(input())
    for _i in range(n):
        row = input().split()
        segments.append((int(row[0]), int(row[1]), int(row[2]), int(row[3])))
    start_pos = int(input())

    return start_pos, segments


def intersect(pos_x, segment):
    if (pos_x >= segment[0] and pos_x <= segment[2]) or \
       (pos_x >= segment[2] and pos_x <= segment[0]) or \
       (pos_x == segment[0] or pos_x == segment[2]):
        return True
    else:
        return False


def get_displaced_position(segment):
    if segment[1] < segment[3]:
        return segment[0]
    return segment[2]


def get_segment_direction(segment):
    if segment[0] < segment[2]:
        return 1
    else:
        return -1
    return 0


def main():
    pos_x, segments = get_input()
    for segment in segments:
        if intersect(pos_x, segment):
            pos_x = get_displaced_position(segment)

    print(pos_x)
    return pos_x


if __name__ == '__main__':
    main()
