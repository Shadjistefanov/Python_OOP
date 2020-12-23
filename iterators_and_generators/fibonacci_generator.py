def fibonacci():
    current_num = 0
    previous_num = 1
    while True:
        yield current_num
        current_num, previous_num = previous_num, current_num + previous_num



generator = fibonacci()
for i in range(10):
    print(next(generator))
