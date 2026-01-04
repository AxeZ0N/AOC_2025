from math import floor,ceil

with open("input.txt", "r") as f:
    inpt = [line.strip() for line in f]


#inpt = ["R1000"]
dial_curr = 50
counter = 0

for line in inpt:
    direction, amt = str(line[0]), int(line[1:])
    amt = amt * 10000
    print(direction, amt)

    if direction == "L":
        for i in range(amt):
            dial_curr += 1
            dial_curr %= 100

            if dial_curr == 0:
                counter += 1
    else:
        for i in range(amt):
            dial_curr -= 1
            dial_curr %= 100

            if dial_curr == 0:
                counter += 1

print(counter)
