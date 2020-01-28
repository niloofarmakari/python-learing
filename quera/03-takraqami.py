number = input()

while len(number) > 1:
    jam = 0
    for char in number:
        jam = jam + int(char)

    number = str(jam)

print(number)
