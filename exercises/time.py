import sys
import time
import os

counter=0
s = 0
m = 0
n = int(input("Till How Many Seconds do you want the timer to be?: "))
print("")

while counter <= n:
    sys.stdout.write("\x1b[1A\x1b[2k")
    print(m, 'Minutes', s, 'Seconds')
    time.sleep(1)
    s += 1
    counter+=1
    if s == 60:
        m += 1
        s = 0

print("\nTime Is Over Sir! Timer Complete!\n")