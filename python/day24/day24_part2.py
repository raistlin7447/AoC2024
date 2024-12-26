from random import randint

registers = dict()
z_registers = []
x_registers = []
y_registers = []

initial_states, operations = open("day24_input.txt").read().split("\n\n")

for initial_state in initial_states.splitlines():
    register, value = initial_state.split(": ")
    if register.startswith("x"):
        x_registers.append(register)
    elif register.startswith("y"):
        y_registers.append(register)

    #registers[register] = ("BIT", int(value), "_")
    registers[register] = ("BIT", randint(0,1), "_")


x_registers.sort(reverse=True)
x_bits = ""
for register in x_registers:
    x_bits += str(registers[register][1])
x_int = int(x_bits, 2)

y_registers.sort(reverse=True)
y_bits = ""
for register in y_registers:
    y_bits += str(registers[register][1])
y_int = int(y_bits, 2)

register_fixes = {
    "dhg": "z06",
    "z06": "dhg",
    "dpd": "brk",
    "brk": "dpd",
    "bhd": "z23",
    "z23": "bhd",
    "nbf": "z38",
    "z38": "nbf",
}

for operation in operations.splitlines():
    expression, result_register = operation.split(" -> ")
    if result_register.startswith("z"):
        z_registers.append(result_register)

    if result_register in register_fixes:
        result_register = register_fixes[result_register]

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
z_bits = ""
for register in z_registers:
    z_bits += str(get_register(register))
z_int = int(z_bits, 2)

print(f"{z_int}, {x_int}, {y_int}")
print(f" {x_bits=}  {x_int:0b}")
print(f" {y_bits=}  {y_int:0b}")
print(f"{z_bits=} {x_int+y_int:0b}")
print(f" z_int='{x_int+y_int:0b}'")

print(",".join(sorted(register_fixes.keys())))

if z_int != x_int+y_int:
    print(f"{z_int=} {x_int+y_int=}")
    print("FAILED")