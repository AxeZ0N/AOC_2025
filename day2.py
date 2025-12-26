# Must id digit strings that consist of at least two repeats of the same string
# EX: 123123, 10121012, 1212, 111
# Invalid ID's must PASS my test

# O(n)^2
# Check each digit
# If pass, add to check
# If fail, break

from time import time

with open("input.txt", "r", encoding="UTF-8") as f:
    inpt_raw = f.read().strip()

csv = inpt_raw.split(",")

ranges = [x.split("-") for x in csv]


# print(csv)
# print(ranges)

# Given an id ID
# For ID to pass, it must be invalid.
# Any given invalid ID must satisfy
# Where x = range(1,len(ID) // 2 + 1), x >= 1 and len(ID) % x == 0
# There exists a string of len x where grouping the digits in ID in groups of x produces a set of 1

# Prove ID: 11 is INVALID, and thus PASSES my test
# x = [1, ]
# len('11') % x = 0
# ID[:1] == ID[1:]

# Prove ID: 121121 is INVALID, and thus PASSES my test
# x = [1, 2, 3]
# len(id') % x = 0 is true for [1, 2, 3]
# ID[:1] != ID[1:2] != ID[2:3]...
# ID[:2] != ID[2:4] != ID[4:6]...
# ID[:3] == ID[3:]

# Prove ID: 10121012 is INVALID, and thus PASSES my test
# x = [1, 2, 3, 4]
# len(id') % x = 0 is true for [1, 2, 4]
# ID[:1] != ID[1:2] != ID[2:3]...
# ID[:2] != ID[2:4] != ID[4:6]...
# ID[:4] == ID[4:]

# Prove ID: 123123123 is INVALID, and thus PASSES my test
# x = [1, 2, 3, 4]
# len(id') % x = 0 is true for [1, 3]
# ID[:1] != ID[1:2] != ID[2:3]...
# ID[:3] == ID[3:5] == ID[5:]

# Prove ID: 12345 is VALID, and thus FAILS my test
# x = [1, 2]
# len(id') % x = 0 is true for [1]
# ID[:1] != ID[1:2] != ID[2:3] != id...


def test_n_chunks(n: int, ID: str):
    """Split the id into n chunks, return if they are all identical"""
    if n > len(ID):
        return False

    my_set = set()

    while len(ID) > 0:
        to_add = ID[0:n]
        my_set.add(to_add)
        ID = ID[n:]

    return len(my_set) == 1


def get_num_chunks(ID: str):
    """Find valid chunk partitions for the ID"""
    chunk_sizes = []
    for i in range(1, (len(ID) // 2) + 1):
        if len(ID) % i == 0:
            chunk_sizes += [i]

    return chunk_sizes


def test_int_chunks(n: int, ID: int):
    chunks = set()
    ID = int(ID)
    while ID > 0:
        ch = ID % 10**n
        ID = ID // 10**n
        chunks.add(ch)

    return len(chunks) == 1


tic = time()
ID = "123123123"
# ranges = [] # For testing other stuff
bad_ids = 0
for start, end in ranges:
    # print(f"Range: {start,end}")
    for ID in range(int(start), int(end) + 1):
        for chunk_size in get_num_chunks(str(ID)):
            if test_int_chunks(chunk_size, str(ID)):
                # print(f"\tID: {ID} is invalid for n = {chunk_size}")
                bad_ids += int(ID)
                break
    print(f"{ranges.index([start,end])} / {len(ranges)}")

toc = time()
print(bad_ids)
print(f"time: {toc-tic}")

# More optimal solution?
# An invalid id can be represented such that
# A = sequence of digits
# n = len(A)
# m = num repetitions
# Thus: N = A * (10^(n(m-1)) + ... + 1)

# Repeating digits must be in first half of ID,
# Starting size = n = len(ID)//2
# While n >= 1:
# if len(ID) % n != 0: continue
# Split ID into a set of chunks of length n
# If len(set) == 1: invalid ID
# n -= 1
