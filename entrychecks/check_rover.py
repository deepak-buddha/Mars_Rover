from objects.plateau import Plateau


def check_rover(line,P:Plateau):
    if len(line)==3:
        line = list(line)
    else:
        line = line.split()
    value = True
    error = "None"

    if len(line)!=3:
        error = 'Rover coordinates and direction should be expressed only with 3 characters.'
        value=False

    else:
        for i in range(len(line)):
            if i!=2:
                try:
                    coordinate = int(line[i])
                    assert (coordinate >= 0)
                except AssertionError:
                    error = 'Coordinate values should be greater than or equal to zero.'
                    value = False
                    break
                except:
                    error = 'Plateau coordinates can only be a non-negative integer.'
                    value = False
                    break
            elif i==2:
                directions = 'N S E W'.split()
                count=0
                for dir in directions:
                    if line[i]==dir:
                        count=1
                        break
                if count!=1:
                    error = 'Direction of Rover should be in NSEW direction (Also capitalise if necessary).'
                    value=False

    if value==True:
            if(int(line[0])<=P.x_axis):
                if(int(line[1])<=P.y_axis):
                    value=True
                else:
                    value=False
            else:
                value=False

            if value==False:
                error = "Rover coordinates exceed Plateau coordinates."

    return(error,value)



