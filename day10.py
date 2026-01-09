
file = 'test_input.txt'

with open(file,'r') as f:
    inpt = f.readlines()

def get_input(inpt):

    for line in inpt:

        code, other = line.strip().split(' ',maxsplit=1)

        joltage, wiring = ''.join(reversed(other)).split(' ',maxsplit=1)
        joltage, wiring = ''.join(reversed(joltage)),''.join(reversed(wiring))

        yield code,wiring,joltage

inpt = list(get_input(inpt))

for x in inpt: print(x)
