class reverse_iter():

    def __init__(self, some_list):
        self.some_list = some_list

    def __iter__(self):
        return self

    def __next__(self):
        counter = 0
        while self.some_list:
            counter += 1
            res = self.some_list.pop()
            return res
        raise StopIteration



reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
