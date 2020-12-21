n=int(input())

GROWING:int = 1
DECREASING:int = -1

def print_rhombus(direction):
    if direction ==1:
        for i in range(0,n+1):
            print(' '*(n-i)+'* '*i)
    else:
        for i in range(n-1, 0,-1):
            print(' ' * (n - i) + '* ' * i)


print_rhombus(GROWING)
print_rhombus(DECREASING)