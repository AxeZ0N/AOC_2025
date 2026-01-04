# Part of the puzzle for this one is parsing the input
# I will first try transposing the input matrix, and looking for clues
# It's not reverse polish or anything
# Transposing didn't seem too helpful
# Maybe write a function to batch out each quadruplet
# Forgot that strip() gets rid of the important spaces too
# Numbers can be any number of digits, must ID the correct space column seps

# To find first separator column, start with i = last_digit + 1
# Continue through array[j][i] until a non blank char is reached
# If the end is reached, j is a separator col
# Else, increment i and start over

# To find ALL sep cols, split the input by whitespace?
# If lines can be blank, that's harder
# Real input has 4 rows + operator. Doesn't look like it has blanks
# Although, that seems pretty obvious. Part 2 might make the spaces meaningful.

# Wrote script to parse spaces and nums separately
# Need to get the numbers per col, and the operator.
# Make dict of operators

# Part 2 turned out to be a different parsing of the numbers. Shouldn't be too bad.....
# My very first idea would have been easier to adapt.

with open('input.txt', 'r') as f:
    inpt = [x.strip('\n') for x in f.readlines()]

def split_whitespace(line):
    line = list(line)
    ret = ['']
    i = 0
    while len(line):

        if line[0] == ' ':
            ret[-1] += line.pop(0)
            while len(line) and line[0] == ' ':
                ret[-1] += line.pop(0)
            ret += ['']

        else:
            ret[-1] += line.pop(0)
            while len(line) and line[0] != ' ':
                ret[-1] += line.pop(0)
            ret += ['']

    return [x for x in ret if x]
        

def parse_inpt(inpt):
    nums,white = [],[]
    for line in inpt:
        inpt_split = split_whitespace(line)
        nums += [[x for x in inpt_split if x.strip()]]
        white += [[x for x in inpt_split if not x.strip()]]

    return nums, white

my_nums, my_whites = parse_inpt(inpt)

cols = []

for i in range(len(my_nums[0])):
    cols += [[num[i] for _,num in enumerate(my_nums)]]

tx_ops = {
        '*':int.__mul__,
        '+':int.__add__,
        }

from itertools import accumulate

count = []

for nums in cols:
    op = tx_ops[nums.pop()]
    nn = [int(x) for x in nums]
    count += [list(accumulate(nn,op))[-1]]

print(sum(count))


def split_p2(line):
    line = list(reversed(line))
    return ''.join(line)

def transpose(inpt):
    foo = list(zip(*inpt))
    ret = []
    for xyz in foo:
        ret.append(''.join([''.join(x) for x in xyz if xyz]))

    return [x for x in ret if x.strip()]

inpt = [split_p2(x) for x in inpt]
txpose = transpose(inpt)
print(txpose)

nums = [[]]
while txpose:
    try: 
        tx = txpose.pop(0)
        nums[-1].append(int(tx))

    except:
        txpose.insert(0,tx)
        *t,o = list(txpose.pop(0))
        t = int(''.join(t).strip())
        nums[-1] = [o] + nums[-1] + [t]
        if not txpose:
            break
        else:
            nums.append([])

rets = []
for n in nums:
    if (foo := n.pop(0)) == "*":
        rets.append(list(accumulate(n, func=int.__mul__))[-1])
    elif foo == "+":
        rets.append(list(accumulate(n, func=int.__add__))[-1])
    print(n, rets[-1])

print(sum(rets))
