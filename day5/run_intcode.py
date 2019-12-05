import sys
import numpy as np

def run():
    with open('input', 'r') as f:
        buf = f.read()

    intcode = np.array(buf.split(','), dtype=int)
    print(intcode)
    ipc = 0
    while ipc < intcode.size:
        instr_first_value = intcode[ipc]
        opcode = instr_first_value % 100

        third_param_mode = int(instr_first_value // 10000)
        second_param_mode = int((instr_first_value % 10000) // 1000)
        first_param_mode = int((instr_first_value % 1000)//100)

        first_param = intcode[ipc+1]
        second_param = intcode[ipc+2]  # Note: might be invalid depending on instruction
        third_param = intcode[ipc+3]  # Note: might be invalid depending on instruction

        if opcode in [1, 2]:  # addition/multiplication instruction
            # Read operands according to param modes:
            op1, op2 = (0, 0)
            if first_param_mode == 1:
                op1 = first_param
            else:
                op1 = intcode[first_param]
            if second_param_mode == 1:
                op2 = second_param
            else:
                op2 = intcode[second_param]

            result = 0
            if opcode == 1:
                result = op1 + op2
            else:
                result = op1 * op2
            # write result to intcode at position intcode[3]
            intcode[third_param] = result
            instr_length = 4
        elif opcode == 3:  # input instruction
            inp = int(input('Enter input: '))
            intcode[first_param] = inp
            instr_length = 2
        elif opcode == 4:  # output instruction
            outp = intcode[first_param]
            print("output: {}".format(outp))
            instr_length = 2
        elif opcode == 99:
            print("Encountered opcode 99 at position {}, exiting program.\n"
                  "Writing output to output".format(ipc))
            with open('output', 'w') as f:
                output = ",".join([str(i) for i in intcode])
                f.write(output)
            sys.exit()
        else:
            raise Exception("Unknown opcode: {}".format(opcode))

        ipc += instr_length


if __name__ == "__main__":
    run()
