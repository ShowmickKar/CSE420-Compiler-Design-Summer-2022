def lexical_analyzer(java_program):
    methods_with_return_types = []
    for line in java_program:
        for i, lexim in enumerate(line):
            if lexim in ["int", "char", "float", "void", "double", "String"] and line[i + 2] == "(" and line[-1] == ")" and line[i + 1] != "main":
                methods_with_return_types.append(
                    f"{' '.join(line[i + 1:])}, return type: {lexim}")
                break
    return methods_with_return_types


def read():
    file = open("input.txt", "r")
    java_program = []
    for line in file:
        java_program.append(line.strip().split(" "))
    return java_program


java_program = read()
print(java_program)
methods_with_return_types = lexical_analyzer(java_program)
for method in methods_with_return_types:
    print(method)
