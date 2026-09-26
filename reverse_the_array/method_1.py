def reverseArray(a):
    result = []
    for i in range(sizeOfArray - 1, -1, -1):
        result.append(a[i])
    return result

# now we actually USE the function
sizeOfArray = int(input())
my_list = list(map(int,input().split()))
answer = reverseArray(my_list)

for i in range(sizeOfArray):
    print(answer[i], end=" ")




    
#explaination of the line - for i in range(len(a) - 1, -1, -1):
#len(a) - 1 ---> where to start, the last element
# next -1 ---> where to stop
# next -1 ---> 

#this one also working but not with the inputs