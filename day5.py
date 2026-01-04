with open('input.txt', 'r') as f:
    ranges1 = []
    while (line := f.readline()) != '\n':
        ranges1 += [line.strip()]

    items = [int(x.strip()) for x in f.readlines()]

# Combine all ranges, find numbers not in any range

ranges = [x.split('-') for x in ranges1]

ranges = [(int(a),int(b)) for a,b in ranges]

my_ranges = ranges.copy()

ranges = [range(a,b) for a,b in ranges]

ranges = []

fresh = []
spoiled = []

for item in items:
    for r in ranges:
        if item not in r: continue
        fresh += [item]
        break

    if item not in fresh:
        spoiled += [item]

# Sort ranges?
# Combine any that are inside each other
# Expand others to include

#range_pairs = my_ranges
#
#range_pairs.sort(key=lambda x: x[0])
#merged = []
#for start, end in range_pairs:
#    if not merged or start > merged[-1][1]:
#        merged.append([start, end])
#    else:
#        merged[-1][1] = max(merged[-1][1], end)
#
#print( sum([max_val + 1 - min_val for min_val, max_val in merged]) )

my_ranges.sort()

print(my_ranges)

merged = []

# my_ranges[0][0] is lowest possible num
# my_ranges[-1][1] is largest possible num
for start, end in my_ranges:
    # if start is more than the largest number we've seen
    # it's the start of a new range
    if not merged or start > merged[-1][1]:
        merged.append([start,end])
    # otherwise, that means the lower value is inside our range
    # Thus, remaining task is to determine the new end value
    else:
        # new max is whatever is bigger between current and end
        merged[-1][1] = max(merged[-1][1],end)

count = 0

for start,end in merged:
    count += len(range(start,end+1))

print(count)
