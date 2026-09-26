# this one use a inbuilt method to do this reverse machanism

n = int(input())

arr = list(map(int, input().split()))

result = arr[::-1]
print(' '.join(map(str,result)))