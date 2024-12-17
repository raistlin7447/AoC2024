import enum

class OP(enum.Enum):
    adv = 0
    bxl = 1
    bst = 2
    jnz = 3
    bxc = 4
    out = 5
    bdv = 6
    cdv = 7

REG_A = 4
REG_B = 5
REG_C = 6

class CPU:
    def __init__(self, registers, program):
        self.memory = [0, 1, 2, 3] + registers    # 4, 5, and 6 are the registers
        self.program = program
        self.ip = 0                               # Instruction Pointer
        self.output = []

    def execute_next_instruction(self):
        opcode = self.program[self.ip]
        operand = self.program[self.ip + 1]

        match OP(opcode):
            case OP.adv:
                self.memory[REG_A] = self.memory[REG_A] // 2 ** self.memory[operand]
            case OP.bxl:
                self.memory[REG_B] = self.memory[REG_B] ^ operand
            case OP.bst:
                self.memory[REG_B] = self.memory[operand] % 8
            case OP.jnz:
                if self.memory[REG_A] != 0:
                    self.ip = operand - 2
            case OP.bxc:
                self.memory[REG_B] = self.memory[REG_B] ^ self.memory[REG_C]
            case OP.out:
                self.output.append(self.memory[operand] % 8)
            case OP.bdv:
                self.memory[REG_B] = self.memory[REG_A] // 2 ** self.memory[operand]
            case OP.cdv:
                self.memory[REG_C] = self.memory[REG_A] // 2 ** self.memory[operand]

        self.ip += 2

    def execute(self):
        while self.ip < len(self.program):
            self.execute_next_instruction()

    def print_output(self):
        print(",".join(map(str,self.output)))

    def dump_state(self):
        print(f'IP: {self.ip}')
        print(f'Memory: {self.memory}')
        print(f'Program: {self.program}')


data_section, program_section = open("day17_input.txt").read().split("\n\n")

memory_input = []

for line in data_section.splitlines():
    memory_input.append(int(line.split(": ")[1]))

program = list(map(int, program_section.split(": ")[1].split(",")))

solutions = [0]
for length in range(1, len(program) + 1):

    output = []
    for solution in solutions:
        for offset in range(8):
            memory_input[0] = 8 * solution + offset
            cpu = CPU(memory_input, program)
            cpu.execute()

            if cpu.output == program[-length:]:
                output.append(memory_input[0])

    solutions = output

print(min(solutions))