from objects.rover import Rover
from objects.plateau import Plateau



def rover_final_pos(R:Rover,P:Plateau,I):
    for el in I:
        if el=='L':
            R.left_turn()
        elif el=='R':
            R.right_turn()
        else:
            R.move()


    return(R)



