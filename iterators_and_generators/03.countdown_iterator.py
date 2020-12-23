class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.zero = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.zero:
            num = self.count
            self.count -= 1
            return num
        raise StopIteration()



iterator = countdown_iterator(15)
for item in iterator:
    print(item, end=" ")


