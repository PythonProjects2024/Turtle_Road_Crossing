from Modules.car_control import CarManager

from Modules.player import Player
from Modules.scoreboard import Scoreboard
from turtle import Screen
import time



screen = Screen()
player = Player()
cars_coming = CarManager()
score = Scoreboard()
game_in_on = True

screen.setup(600, 600)
screen.title("Road Crossing Game")
screen.tracer(0)

screen.listen()
screen.onkeypress(player.start_go_up, "Up")  # Start moving on key press
screen.onkeyrelease(player.stop_go_up, "Up")  # Stop moving on key release


while game_in_on:
    time.sleep(0.1)
    screen.update()

    cars_coming.create_cars()
    cars_coming.move_cars()


    for car in cars_coming.all_cars:
        if car.distance(player) < 20:
            game_in_on = False
            score.game_over()


    if player.finish_line():
        player.go_to_start()
        cars_coming.level_up()
        score.increase_score()
        

    

screen.exitonclick()




