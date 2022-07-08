

def instructions(line):
    line = list(line)

    while ' ' in line:
        line.remove(' ')

    return(line)
