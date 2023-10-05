

def get_input():
    segments = []
    n = input()
    for _i in range(int(n)):
        row = input().split()
        segments.append((int(row[0]), int(row[1]), int(row[2]), int(row[3])))
    start_pos = input()

    return start_pos, segments


def is_collision(pos, segment):

    return True


def main():
    pos_x, segments = get_input()
    for segment in segments:
        if is_collision(pos_x, segment):
            # TODO Move horizontal
            continue

    print(pos_x)
    return pos_x


if __name__ == '__main__':
    main()
