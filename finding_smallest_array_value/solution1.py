arr = [1,2,3,4,5]

for i in range(len(arr)):
    if arr[i-1] < arr[i]:
        minimumValue = arr[i]
print()
