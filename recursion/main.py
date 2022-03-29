# Created on iPad (Timur).
def sum_rec(N):
    if N ==0:
        return 0
    return sum_rec(N-1) + N
def fibonacci(N):
    if N <= 2:
        return 1
    return N-1 + fibonacci(N-2)
n = int(input("Please enter a number\n"))
print("Recursive sum: " + str(sum_rec(n)))
print("Fibonacci sequence: ")
for i in range(n):
    print(fibonacci(i+1),end =' ')
print('')