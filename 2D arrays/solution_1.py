# hour glass problem
hourglass_sum = 0


twoDimensionalArray = []
for _ in range(6):  # we use _ when we not caring the count
    row = list(map(int, input().split()))
    twoDimensionalArray.append(row)  # add to the array

hourglass_all_values = []

for x in range(6):
    for y in range(6):

        for row in range(4):
            for col in range(4):
                # calculate the value here
                hourglass_sum = (
                    twoDimensionalArray[row][col]
                    + twoDimensionalArray[row][col + 1]
                    + twoDimensionalArray[row][col + 2]
                    + twoDimensionalArray[row + 1][col + 1]
                    + twoDimensionalArray[row + 2][col]
                    + twoDimensionalArray[row + 2][col + 1]
                    + twoDimensionalArray[row + 2][col + 2]
                )
                hourglass_all_values.append(hourglass_sum)

print(max(hourglass_all_values))


"""
a = arr[row][col]
b = arr[row][col+1]
c = arr[row][col+2]
d = arr[row+1][col+1] (the middle one — skips left and right)
e = arr[row+2][col]
f = arr[row+2][col+1]
g = arr[row+2][col+2]
"""
