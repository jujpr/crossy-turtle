import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Crossy-Turtle")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.add_car()
    car.move()

    for _ in car.cars:
        if player.distance(_) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() >= 280:
        player.reset_position()
        scoreboard.point()
        car.increase_difficulty()





screen.exitonclick()
