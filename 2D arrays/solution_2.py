def hourglassSum(arr):
    sums = []
    for row in range(4):
        for col in range(4):
            hourglass_sum = (
                arr[row][col]
                + arr[row][col + 1]
                + arr[row][col + 2]
                + arr[row + 1][col + 1]
                + arr[row + 2][col]
                + arr[row + 2][col + 1]
                + arr[row + 2][col + 2]
            )
            sums.append(hourglass_sum)
    return max(sums)


if __name__ == "__main__":
    arr = []
    for _ in range(6):
        row = list(map(int, input().split()))
        arr.append(row)
    result = hourglassSum(arr)
    print(result)
