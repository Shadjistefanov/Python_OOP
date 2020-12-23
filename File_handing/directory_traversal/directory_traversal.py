import os

path = input()
sep_count = path.count(os.path.sep)
dicts = {}
for root, dirs, files in os.walk(path):
    if sep_count - root.count(os.path.sep) > 1:  # '\\'

        continue
    for file in files:
        extension = file.split('.')[-1]
        if extension not in dicts:
            dicts[extension] = []
        dicts[extension].append(file)

result = ''
for key, value in sorted(dicts.items()):
    result += f'.{key}\n'
    for file in sorted(value):
        result += f'- - - {file}\n'

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
final = desktop + os.path.sep + 'report.txt'

with open(final, 'w') as file:
    file.write(result)