from objects.plateau import Plateau
from objects.rover import Rover

def rover_initialise(line):
    line = line.split()
    x_axis = int(line[0])
    y_axis = int(line[1])
    direction = line[2]

    R = Rover(x_axis,y_axis,direction)

    return(R)

