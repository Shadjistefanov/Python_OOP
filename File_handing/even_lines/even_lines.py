
symbols = {"-", ",", ".", "!", "?"}
with open('text.txt', "r") as file:

    for idx, line in enumerate(file):
        if idx % 2 == 0:

            for el in symbols:
                line = line.replace(el, '@')
            words = reversed(line.split())
            print(' '.join(words))

