# Mars Rover Challenge

#### Note:
1. Use `docker-compose up` to run through docker.
2. To access it, especially if you are using mac, use `http://localhost:5000/` instead of the address provided to access the home page.
3. Incase if you want to make changes to the code itself and run the docker, then use `docker-compose up --force-recreate --build -d` to rewrite existing docker image.

---

## Assumptions Made
1. Data is fed through ***mars.txt***
2. Rovers are initialised only if ***mars.txt*** is completely error-free. In case of error, the rover no. where the error occurred is displayed on screen in order for the user to make the necessary corrections easily.
3. More than one rover can occupy the same coordinates. (This is done to simplify the analysis). In case of updating the rovers, if more than one rover occupies the same coordinates and orientation, the update happens only on the first occuring rover in ***mars.txt***

---


## File descriptions

 **marsrover**<br />
----> ***mars.txt***<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text file containing Plateau coordinates,Rover parameters and the Instructions for each particular rover to follow to get to its final position.<br />
----> ***app***<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Our main python file containing Flask App and API. This is our file which needs to be run to initiate our mars rover challenge.All the other functions listed are called and executed here. Code includes routing to:
* get the final coordinates, after running our mars.txt file - displayed at localhost:*port*/run.html
* dynamically enter new rover parameters to update existing rover parameters. You can use the POST function to enter the old rover and new rover parameters in this format
localhost:port/oldroverparam_newroverparam.**Eg**: localhost:*port*/13N24E --> changes existing rover position from 1 3 N to 2 4 E
* display the updated rover parameters at localhost:*port*/update.html

----> ***check_content***<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;checks if the data in mars.txt is valid. It makes calls to files in<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;marsrover --> entrychecks
<br /><br />


**marsrover --> objects**<br />
----> ***plateau***<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contains class Plateau with parameters *x_axis* and *y_axis* describing its coordinates.<br />
----> ***rover***<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contains class Rover with parameters *x_pos*, *y_pos* and *direction* to desribe its position and orientation.<br /><br />

**marsrover --> entrychecks**<br />
----> ***check_plateau***<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Checks validity of Plateau.<br />
----> ***check_actions***<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Checks validity of Instructions to move the rover.<br />
----> ***check_rover***<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Checks validity of Rover.<br /><br />


**marsrover --> actions**<br />
Once all the validities are checked, each rover is initialised, fed instructions to move to its final position and its moved to its final positon.<br />
---->***rover_initalise***<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initialises Rover.<br />
----> ***instructions***<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read instructions to move the rover to its final position.<br />
---->***rover_final_pos***<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Using the rover's initial position and the instructions fed, move the rover to its final position and get its parameters.

---
