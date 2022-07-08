def check_actions(line):
    line = list(line)
    error = "None"


    while ' ' in line:
        line.remove(' ')

    value=True

    actions='L R M'.split()
    count=0
    for el in line:

        for act in actions:
            if el==act:
                count+=1
                break

    if count==len(line):
        value=True
    else:
        error = 'Invalid rover action detected (Capitalise if necessary).'
        value=False

    return(error,value)
