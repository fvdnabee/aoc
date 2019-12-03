import numpy as np
import sys

with open('input', 'r') as f:
    buf = f.read()

intcode = np.array(buf.split(','), dtype=int)
print(intcode)
for i in range(0, intcode.size, 4):
    r = 0
    opcode = intcode[i]

    if opcode == 1 or opcode == 2:
        pos1 = intcode[i+1]
        pos2 = intcode[i+2]
        op1 = intcode[pos1]
        op2 = intcode[pos2]
        if opcode == 1:
            r = op1 + op2
        else:
            r = op1 * op2
    elif opcode == 99:
        print("Encountered opcode 99 at position {}, exiting program.\n"
              "Writing output to output".format(i))
        with open('output', 'w') as f:
            output = ",".join([str(i) for i in intcode])
            f.write(output)
        sys.exit()
    else:
        raise Exception("Unknown opcode: {}".format(opcode))

    # write result to intcode at position intcode[3]
    pos3 = intcode[i+3]
    intcode[pos3] = r
