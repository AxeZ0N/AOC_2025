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


with open("input.txt", "r", encoding="UTF-8") as f:
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

def search_range(bank, min, max, digit):
    i = int(min)
    while i in range(int(min), int(max)+1):
        if bank[i] == str(digit): return i
        else: i += 1

    return None

# New attempt: Two little crawlers

def battery_bank(bat):

    joltage = []
    reserved_index = lambda: len(bat) - (12-len(joltage))
    # Avoid using the last 12, can tack them on in worst case scenario
    l,r = 0, 0

    # Cycle until a 12 digit number is found
    while len(joltage) < 12:

        d = 9
        # Start each loop with the best digit
        next_l = search_range(bat, l, reserved_index(), d)

        # Might not find it
        if next_l is None:
            d_ = d
            while d_ > 0:
                # Decrement search digit and try again
                next_l = search_range(bat, l, reserved_index(), d_)
                # Again, might not find it
                if next_l is None or bat[next_l] != str(d_): d_ -= 1
                else: break

        if next_l not in range(l, len(bat)):
            raise ValueError(f"{next_l} not in l range!")

        l = next_l

        # Start the next search at one past the prev digit
        next_r = l + 1
        next_r = search_range(bat, l+1, reserved_index(), 9)

        # Might not find 9,
        if next_r is None:
            d_ = d
            while d_ > 0:
                # Decrement search digit and try again
                next_r = search_range(bat, l, reserved_index(), d_)
                # Again, might not find it
                if next_r is None or bat[next_r] != str(d_): d_ -= 1
                else: break


        if next_r not in range(l, len(bat)):
            raise ValueError(f"{next_r} not in r range!")

        r = next_r

        joltage += [l]

        #print([bat[x] for x in range(l,r+1)])

        int_joltage = translate(bat, joltage)
        #print(list(map(bat.__getitem__, joltage)))

        l += 1

    j = translate(bat, joltage)

    return j

jolts = 0
for bat in battery_banks:
    j = battery_bank(bat)
    print(j)
    jolts += j


print(jolts)
