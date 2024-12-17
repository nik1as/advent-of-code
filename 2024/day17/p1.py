lines = ""
while True:
    try:
        lines += input() + "\n"
    except EOFError:
        break

registers, program = lines.split("\n\n")
registers = [int(e.split(": ")[-1]) for e in registers.split("\n")]
program = list(map(int, program.strip().split(": ")[-1].split(",")))

combo_operand = [
    lambda: 0,
    lambda: 1,
    lambda: 2,
    lambda: 3,
    lambda: registers[0],
    lambda: registers[1],
    lambda: registers[2],
]

outputs = []
pointer = 0
while pointer < len(program) - 1:
    opcode = program[pointer]
    operand = program[pointer + 1]

    match opcode:
        case 0:
            registers[0] = registers[0] // 2 ** combo_operand[operand]()
        case 1:
            registers[1] = registers[1] ^ operand
        case 2:
            registers[1] = combo_operand[operand]() % 8
        case 3:
            if registers[0] != 0:
                pointer = operand
                continue
        case 4:
            registers[1] = registers[1] ^ registers[2]
        case 5:
            outputs.append(combo_operand[operand]() % 8)
        case 6:
            registers[1] = registers[0] // 2 ** combo_operand[operand]()
        case 7:
            registers[2] = registers[0] // 2 ** combo_operand[operand]()

    pointer += 2

print(",".join(map(str, outputs)))
