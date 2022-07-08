import os

from objects.plateau import Plateau

from check_content import check_content

from entrychecks.check_rover import check_rover
from actions.rover_initialise import rover_initialise
from actions.rover_final_pos import rover_final_pos
from actions.instructions import instructions

from flask import Flask, render_template
from flask_restful import Resource,Api


app = Flask("__main__")
api = Api (app)






Q = Plateau(0,0)
glob_roverpos = []

@app.route('/')
def index():
    return render_template('basic.html')

@app.route('/run.html')
def run():

    global Q
    global glob_roverpos
    filename = os.path.abspath("mars.txt")
    if os.path.isfile(filename)==True:

        error = "None"
        value = True
        error,value = check_content(filename)


        if value==False:
            out_err = []
            out_err.append(error)
            return render_template('/run.html',out=out_err)

        else:
            with open(filename,'r') as f:
                lines = f.readlines()

                non_empty_lines = [line.strip() for line in lines if line.strip() != ""]

                lines = non_empty_lines

                roverpos = []


                for ind in range(len(lines)):
                    out_msg = "None"
                    if ind==0:
                        plateau_coord = lines[ind].split()
                        P = Plateau(int(plateau_coord[0]), int(plateau_coord[1]))
                        Q=P

                    elif ind%2==1:
                        R = rover_initialise(lines[ind])
                    else:
                        I = instructions(lines[ind])

                        result= rover_final_pos(R,P,I)

                        if result.x_pos>P.x_axis or result.y_pos > P.y_axis:
                            out_msg = 'Rover out of bounds'
                        elif result.x_pos < 0 or result.y_pos < 0:
                            out_msg = 'Rover out of bounds'
                        else:
                            out_msg = f"{result.x_pos} {result.y_pos} {result.direction} "
                        roverpos.append(out_msg)

                glob_roverpos = roverpos
                return render_template('/run.html', out=roverpos)

    else:
        msg=["Error!! Please ensure that mars.txt exists"]
        return render_template('/run.html', out=msg)


@app.route('/update.html')
def update():
    global Q
    global glob_roverpos
    msg=[]
    R = Plateau(0,0)
    if glob_roverpos == []:
        msg = ["Kindly run the program through /run.html before updating rovers"]
        return render_template('/update.html',out=msg)
    else:
        return render_template('/update.html',out=glob_roverpos)





class UpdateRover(Resource):
    def post(self,rover_updates):

        global Q
        global glob_roverpos



        if Q==Plateau(0,0):
            return {'update':'Unsuccessful. Please use /run.html before updating rover'}
        elif len(rover_updates)!=6:
            return {'update':'Unsuccessful. Incorrect rover parameters entered'}
        else:
            old_rover = rover_updates[:3]
            new_rover = rover_updates[3:]

            error = "None"
            value = True

            error, value = check_rover(old_rover, Q)
            if value == True:
                error, value = check_rover(new_rover, Q)
                if value == True:
                    old_rover_str = ""
                    new_rover_str = ""

                    old_rover = list(old_rover)
                    new_rover = list(new_rover)


                    for i in old_rover:
                        old_rover_str = old_rover_str + i + " "

                    for i in new_rover:
                        new_rover_str = new_rover_str + i + " "

                    count=0
                    for ind,el in enumerate(glob_roverpos):
                        if el == old_rover_str:
                            glob_roverpos[ind] = new_rover_str
                            count=1
                            return {'update': 'Successful. Please use /update.html to view the updated rovers'}

                    if count==0:
                        return {'update': 'Unsuccessful. Rover to be replaced not found'}


                else:
                    return {'update': "Unsuccessful. " + error}
            else:
                return {'update': "Unsuccessful. " + error, 'Q_xaxis':Q.x_axis,'Q_yaxis':Q.y_axis}


api.add_resource(UpdateRover,'/<string:rover_updates>')



if __name__ == "__main__":
    app.run(port=5000,threaded=True,host='0.0.0.0')



