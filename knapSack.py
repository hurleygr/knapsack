def knapSack():
    """
    Solves 0-1 knapsack problem with bottom up dynamic programming
    Takes as input a file named data.txt with lines of weight value for each item
    Also takes user input for capacity
    Returns table, solution, and subset of weights that make up solution
    """
    cap = int(input("Enter Capacity: "))
    inFile = open('data.txt', 'r')
    arr = []
    line = list(map(int, inFile.readline().split()))
    while line:
        arr.append(line)
        line = list(map(int,inFile.readline().split()))
    arr.sort(key=lambda x: x[0])
    table = [[0 for _ in range(cap + 1)] for _ in range(len(arr) + 1)]

    for item in range(1, len(arr) + 1):
        for weight in range(1, cap + 1):
            if arr[item-1][0] > weight:
                table[item][weight] = table[item-1][weight]
            else:
                table[item][weight] = max(table[item-1][weight], table[item-1][weight-arr[item-1][0]] + arr[item-1][1])
    print(table)
    print("The maximum obtainable value is: " + str(max(map(max, table))))

    row = len(arr)
    col = cap
    sub_set = []
    while row > 0 and col > 0:
        if table[row][col] == table[row-1][col]:
            row -= 1
        else:
            sub_set.append(row)
            row -= 1
            col -= arr[row][0]

    print("The optimal subset is: ")
    print(sub_set)
knapSack()
