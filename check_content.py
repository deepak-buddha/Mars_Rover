from objects.plateau import Plateau
from entrychecks.check_plateau import check_plateau
from entrychecks.check_rover import check_rover
from entrychecks.check_actions import check_actions

def check_content(filename):
    with open(filename,'r') as f:
        lines = f.readlines()

        non_empty_lines = [line.strip() for line in lines if line.strip() != ""]

        lines = non_empty_lines

        error = "None"


        value=True

        for ind in range(len(lines)):

            if ind ==0:
                error,check1 = check_plateau(lines[ind])
                if check1==False:
                    value=False
                    break

                else:
                    plateau_coord = lines[ind].split()
                    P = Plateau(int(plateau_coord[0]),int(plateau_coord[1]))

            elif ind%2==1:
                error,check2 = check_rover(lines[ind],P)
                if check2==False:
                    error2 = f' Error was encountered in rover: {int(ind/2) + 1}'
                    error = error + "\n" + error2
                    value=False
                    break


            else:
                error,check3 = check_actions(lines[ind])
                if check3==False:
                    error2 = f' Error was encountered in rover: {int(ind / 2)}'
                    error = error + "\n" + error2
                    value=False
                    break

        return(error, value)


