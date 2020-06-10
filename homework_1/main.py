language = input()
with open(f'{language}.text', 'r') as file:
    data = file.readlines()
    for line in data:
        print(line)