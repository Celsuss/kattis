BINARY = 0
DECIMAL = 1
NEITHER = -1
OUTPUTS = ['binary', 'decimal', 'neither']

def processQuery(query: [], rows: [[int]]) -> str:

    return OUTPUTS[NEITHER]


def getMap() -> []:
    r, c = input().split(' ')
    rows = []
    for _i in range(int(r)):
        row_str = input()
        row = []
        for j in range(int(c)):
            row.append(int(row_str[j]))
        rows.append(row)
    return rows


def getQuerries() -> []:
    n = int(input())
    queries = []
    for _i in range(int(n)):
        query = input().split(' ')
        queries.append(query)
    return queries


def getInput():
    rows = getMap()
    queries = getQuerries()
    return rows, queries


def main():
    rows, queries = getInput()
    outputs = []
    for q in queries:
        outputs.append(processQuery(q, rows))

    return ['']


if __name__ == '__main__':
    main()
