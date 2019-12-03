import copy
import sys

import numpy as np

with open('input', 'r') as f:
    buf = f.read()

intcode = np.array(buf.split(','), dtype=int)
intcode_backup = copy.deepcopy(intcode)
for noun in range(100):
    for verb in range(100):
        intcode = copy.deepcopy(intcode_backup)
        intcode[1] = noun
        intcode[2] = verb

        for i in range(0, intcode.size, 4):
            r = 0
            opcode = intcode[i]

            if opcode in [1, 2]:
                pos1 = intcode[i+1]
                pos2 = intcode[i+2]
                op1 = intcode[pos1]
                op2 = intcode[pos2]
                if opcode == 1:
                    r = op1 + op2
                else:
                    r = op1 * op2
            elif opcode == 99:
                print("Encountered opcode 99 at position {}, checking output.".format(i))
                if intcode[0] == 19690720:
                    print("output is equal to 19690720, exiting and writing to output")
                    answer = 100 * noun + verb
                    print("Answer: 100 * {} + {} = {}".format(noun, verb, answer))
                    with open('output', 'w') as f:
                        output = ",".join([str(i) for i in intcode])
                        f.write(output)
                    sys.exit()
                break  # continue to next (noun, verb)
            else:
                print(intcode)
                raise Exception("Unknown opcode: {} at position {}".format(opcode, i))

            # write result to intcode at position intcode[3]
            pos3 = intcode[i+3]
            intcode[pos3] = r
