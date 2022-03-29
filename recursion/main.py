# Created on iPad (Timur).

print ('Hello World!')
def sum_rec(N):
    if N == 0:
        return 0
    return sum_rec(N-1)+N

print(sum_rec(5))