N = int(input())

arr = N * [0]
temp = 0

for i in range(N):
    arr[i] = int(input())


for i in range(N-1):
    for j in range(N - 1 - i ):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp


for i in range(N):
    print(arr[i])

    









