class vowels:
    vowels_char = ['a', 'e', 'i', 'o', 'u', 'y']
    def __init__(self, string):
        self.string = string
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.idx < len(self.string):
            temp = self.idx
            self.idx += 1
            if self.string[temp].lower() in self.vowels_char:
                return self.string[temp]
            else:
                return self.__next__()
        raise StopIteration()



my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

