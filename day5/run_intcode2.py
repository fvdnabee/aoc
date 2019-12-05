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

        # third_param_mode = int(instr_first_value // 10000)
        second_param_mode = int((instr_first_value % 10000) // 1000)
        first_param_mode = int((instr_first_value % 1000)//100)

        # Note: first,second and third param might be invalid depending on the instruction
        first_param = intcode[ipc+1] if ipc+1 < intcode.size else None
        second_param = intcode[ipc+2] if ipc+2 < intcode.size else None
        third_param = intcode[ipc+3] if ipc+3 < intcode.size else None

        # Read operands according to param modes:
        # Note whether op1, op2 contain valid operands depends on the instruction
        op1, op2 = (0, 0)
        if first_param is not None:
            if first_param_mode == 1:
                op1 = first_param
            else:
                if first_param < intcode.size:  # avoid out of bounds IndexError
                    op1 = intcode[first_param]
        if second_param is not None:
            if second_param_mode == 1:
                op2 = second_param
            else:
                if second_param < intcode.size:  # avoid out of bounds IndexError
                    op2 = intcode[second_param]

        if opcode in [1, 2]:  # addition/multiplication instruction
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
            outp = op1
            print("output: {}".format(outp))
            instr_length = 2
        elif opcode == 5:  # jump-if-true
            cond = (op1 != 0)
            if cond:
                ipc = op2
                instr_length = 0
            else:
                instr_length = 3
        elif opcode == 6:  # jump-if-false
            cond = (op1 == 0)
            if cond:
                ipc = op2
                instr_length = 0
            else:
                instr_length = 3
        elif opcode == 7:  # less than
            if op1 < op2:
                intcode[third_param] = 1
            else:
                intcode[third_param] = 0
            instr_length = 4
        elif opcode == 8:  # equals
            if op1 == op2:
                intcode[third_param] = 1
            else:
                intcode[third_param] = 0
            instr_length = 4
        elif opcode == 99:
            print("Encountered opcode 99 at position {}, exiting program.".format(ipc))
            return
        else:
            raise Exception("Unknown opcode: {}".format(opcode))

        ipc += instr_length
        if ipc >= intcode.size:
            raise Exception("IPC {} passed beyond buffer length".format(ipc))


if __name__ == "__main__":
    run()
