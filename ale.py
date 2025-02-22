import sys

programFilePath = sys.argv[1]

intVars = {}
program_lines = []
with open(programFilePath, 'r') as programFile:
    program_lines = [line.strip() for line in programFile.readlines()]

def math(num1, num2, symb):
    if symb == '+': print(num1 + num2)
    elif symb == '-': print(num1 - num2)
    elif symb == '*': print(num1 * num2)
    elif symb == '/': print(num1 / num2)
    elif symb == '^': print(num1 ** num2)


pc = 0
pcIgnore = 0
pyUtilized = False
while pc < len(program_lines):  # Iterate through the program lines
    cline = program_lines[pc]  # Get the current line
    pc += 1
    if cline.startswith('#'):
        continue
    elif 'utilz py' == cline:
        pyUtilized = True
    elif ';=' in cline:
        intVars[str(cline.split(';=')[0])] = cline.split('=')[1]
        exec(cline.replace(';','',1))
    elif cline.startswith('print'):
        if cline.startswith('print~'):
            variable_name = cline.split('print~')[1]
            if variable_name in intVars:
                print(intVars[variable_name])
        else:
            print(cline.replace('print', '', 1)[1:-1])
    elif cline.startswith('math(') and cline.endswith(')'):
        temp = list(cline.replace('math(', '').replace(')', ''))
        exec(cline)
    elif '@repeat' == cline or '@again' == cline:
        pc = pcIgnore
    elif '@rep_ignore' == cline:
        pcIgnore = pc
    elif cline.startswith('py.') and pyUtilized:
        exec(cline.replace('py.','',1))