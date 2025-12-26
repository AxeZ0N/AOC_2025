import pdb
# given a list of digits
# find ab, where a and b are indices
# such that int(concat(a,b)) is maximized


def get_max(bank):
    my_max = 0
    indices = []
    for left_index in range(len(bank) - 1):
        for right_index in range(1, len(bank)):
            if left_index >= right_index:
                continue
            jolt = jolt = int(bank[left_index] + bank[right_index])
            if jolt > my_max:
                my_max = jolt
                indices = [left_index, right_index]

    return my_max, indices


with open("test_input.txt", "r", encoding="UTF-8") as f:
    inpt_raw = f.read().strip()

battery_banks = [[x for x in y] for y in inpt_raw.split("\n")]

jolts = 0

# Greedy algorithm DOES work.

bat = "4329634636558644535534455549345256353469443795539452657625226416756735576575463654843527584644953254"

# Helpers
def to_int(dig_arr):
    return int("".join(dig_arr))

def from_index(battery, arr):
    return [battery[x] for x in sorted(arr)]

def translate(battery, arr):
    return to_int(from_index(battery, arr))

# New attempt.
# Naive: Try all combinations of numbers and choose the largest.
# Straight up completely impossible, even with rules its sum(2^100-n) possibilites
# Keep track of already tried combos
# Don't reuse indexes

# Sort out battery bank by largest digits.
my_digits = {str(x):[] for x in range(1,10)}
for i,d in enumerate(bat):
    my_digits[d].append(i)

joltage = []
reserved_index = lambda: 12-len(joltage)
lm_index = 0

print(reserved_index())

while len(joltage) < 12:
    joltage = '1234'
    print(reserved_index())
    pass




int_joltage = translate(bat, joltage)
print(len(joltage))
print(joltage)
print(int_joltage)
