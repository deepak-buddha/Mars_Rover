def check_plateau(line):
    line = line.split()
    error = "None"
    value = True

    if len(line)!=2:
        error = 'Coordinate axes of Plateau has more than 2 characters.'
        value=False
    elif line == ['0','0']:
        error = 'Right hand top coordinate axes of Plateau should not be [0,0].'
        value=False
    else:

        for el in line:
            try:
                coordinate = int(el)
                assert (coordinate>=0)
            except AssertionError:
                error = 'Coordinate values should be greater than or equal to zero.'
                value = False
                break
            except:
                error = 'Plateau coordinates can only be a non-negative integer.'
                value = False
                break




    return(error, value)

