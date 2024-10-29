# Make the Largest number by utilizing the given numbers

# input <- divide n,m,k by space
n,m,k = map(int,input().split())

# input2 <- given list
arr = list(map(int,input().split))


# n : size , m : number of additions , k : maximum consequtive addtions

# K <= M


arr.sort() # Sort in Ascending order 

first = arr[n-1] # The biggest number of the given arr
Second = arr[n-2] #2

result = 0

while True:
     
     for i in range(k):
          if m == 0:
               break
          result += result
          m -= 1

     if m == 0:
          break

     result += Second
     m -= 1

print(result)


