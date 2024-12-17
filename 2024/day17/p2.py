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
    lambda _: 0,
    lambda _: 1,
    lambda _: 2,
    lambda _: 3,
    lambda r: r[0],
    lambda r: r[1],
    lambda r: r[2],
]


def run(reg):
    outputs = []
    pointer = 0
    while pointer < len(program) - 1:
        opcode = program[pointer]
        operand = program[pointer + 1]

        match opcode:
            case 0:
                reg[0] = reg[0] // 2 ** combo_operand[operand](reg)
            case 1:
                reg[1] = reg[1] ^ operand
            case 2:
                reg[1] = combo_operand[operand](reg) % 8
            case 3:
                if reg[0] != 0:
                    pointer = operand
                    continue
            case 4:
                reg[1] = reg[1] ^ reg[2]
            case 5:
                outputs.append(combo_operand[operand](reg) % 8)
            case 6:
                reg[1] = reg[0] // 2 ** combo_operand[operand](reg)
            case 7:
                reg[2] = reg[0] // 2 ** combo_operand[operand](reg)

        pointer += 2
    return outputs


default_value = registers[0]
a = 0
_, b, c = registers
while True:
    if a == default_value:
        continue
    output = run([a, b, c])
    if output == program:
        print(a)
        break
    for i in range(min(len(output), len(program)) - 1, -1, -1):
        if output[i] != program[i]:
            a += 8 ** i
            break
    else:
        a += 1
