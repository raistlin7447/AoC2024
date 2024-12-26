registers = dict()
z_registers = []

initial_states, operations = open("day24_input.txt").read().split("\n\n")

for initial_state in initial_states.splitlines():
    register, value = initial_state.split(": ")
    registers[register] = ("BIT", int(value), "_")

for operation in operations.splitlines():
    expression, result_register = operation.split(" -> ")
    if result_register.startswith("z"):
        z_registers.append(result_register)

    o1, opr, o2 = expression.split(" ")

    registers[result_register] = (opr, o1, o2)

def get_register(register_name):
    operation, operand1, operand2 = registers[register_name]

    match operation:
        case "BIT":
            return operand1
        case "AND":
            return get_register(operand1) & get_register(operand2)
        case "OR":
            return get_register(operand1) | get_register(operand2)
        case "XOR":
            return get_register(operand1) ^ get_register(operand2)

z_registers.sort(reverse=True)

bits = ""
for register in z_registers:
    bits += str(get_register(register))

print(int(bits, 2))