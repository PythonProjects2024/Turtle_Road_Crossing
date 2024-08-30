from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)
        self.moving_up = False
        

    def go_up(self):
        if self.moving_up:
            self.forward(MOVE_DISTANCE)
            self.screen.ontimer(self.go_up, 100)

    def start_go_up(self):
        self.moving_up = True
        self.go_up()

    def stop_go_up(self):
        self.moving_up = False

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
         
  


