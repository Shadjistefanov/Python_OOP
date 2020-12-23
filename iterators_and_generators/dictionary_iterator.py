class dictionary_iter:
    def __init__(self, dicts):
        self.dictionary = dicts
        self.length = len(self.dictionary)
        self.key = list(self.dictionary.keys())
        self.current = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.length:
            key = self.key[self.current]
            value = self.dictionary[key]
            self.current += 1
            return (key, value)
        raise StopIteration()




result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
