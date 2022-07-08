right_lst = ['N','E','S','W','N']
left_lst = ['N','W','S','E','N']


class Rover():

    def __init__(self,x_pos,y_pos,direction):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direction = direction

    def left_turn(self):
        for i in range(len(left_lst)):
            if left_lst[i]==self.direction:
                self.direction = left_lst[i+1]
                break

    def right_turn(self):
        for i in range(len(right_lst)):
            if right_lst[i]==self.direction:
                self.direction = right_lst[i+1]
                break
    def move(self):
        if self.direction == 'N':
            self.y_pos = self.y_pos + 1
        elif self.direction == 'S':
            self.y_pos = self.y_pos - 1
        elif self.direction == 'E':
            self.x_pos = self.x_pos + 1
        else:
            self.x_pos = self.x_pos - 1


