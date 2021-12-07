import turtle
import time
import sys


class Outplay:
    def __init__(self, win_rate=0, start="0"):
        self.win_rate = win_rate
        self.start = start

    def rec(self, w, h, c1, c2, y):
        """ Draw a rectangle for decoration

        :param w: int
        :param h: int
        :param c1: string
        :param c2: string
        :param y: int
        """
        turtle.color("#fdf5e6")
        turtle.speed(0)
        turtle.hideturtle()
        turtle.penup()
        turtle.pensize(3)
        turtle.speed(0)
        turtle.goto((-1 * (w / 2)), y + 80)
        turtle.pendown()
        turtle.shape()
        turtle.color(c1)
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(w)
            turtle.right(90)
            turtle.forward(h)
            turtle.right(90)
        turtle.end_fill()
        turtle.pu()
        turtle.goto((-1 * (w / 2)) + 10, y + 90)
        turtle.color(c2)
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(w)
            turtle.right(90)
            turtle.forward(h)
            turtle.right(90)
        turtle.end_fill()

    def choose_start(self):
        """ Use the Python Turtle Graphics window to interact with the user by asking
        whether the user wants to start or exit the game."""
        win = turtle.Screen()
        win.register_shape("hangman.gif")
        hm = turtle.Turtle()
        hm.hideturtle()
        hm.penup()
        hm.goto(-500, -200)
        hm.showturtle()
        hm.shape("hangman.gif")
        pen1 = turtle.Turtle()
        pen1.penup()
        pen1.hideturtle()
        pen1.screen.bgcolor("#fdf5e6")
        pen1.goto(0, 200)
        pen1.color("#8b4513")
        self.rec(600, 100, "#708090", "#b0b4de", 200)
        pen1.write("HANGMAN GAME", move=False, align='center', font=('Comic Sans MS', 50, 'bold'))
        pen1.goto(0, -60)
        self.rec(300, 80, "#bc8f8f", "#ffe4e1", -80)
        pen1.write("1 : START", move=False, align='center', font=('Comic Sans MS', 40, 'bold'))
        pen1.goto(0, -180)
        self.rec(300, 80, "#bc8f8f", "#ffe4e1", -200)
        pen1.write("2 : EXIT", move=False, align='center', font=('Comic Sans MS', 40, 'bold'))
        screen = turtle.Screen()
        self.start = screen.textinput("Do you want to play?", "Type a number (1 or 2)")
        if self.start == "2":
            pen1.screen.clear()
            pen1 = turtle.Turtle()
            pen1.hideturtle()
            pen1.penup()
            pen1.screen.bgcolor("#d2b48c")
            pen1.goto(-3, -3)
            pen1.color("#696969")
            pen1.write("Goodbye", move=False, align='center',
                       font=('Comic Sans MS', 70, 'bold'))
            pen1.goto(0, 0)
            win = turtle.Screen()
            win.register_shape("molang2.gif")
            mol2 = turtle.Turtle()
            mol2.hideturtle()
            mol2.penup()
            mol2.goto(0, -200)
            mol2.showturtle()
            mol2.shape("molang2.gif")
            pen1.color("white")
            pen1.write("Goodbye", move=False, align='center',
                       font=('Comic Sans MS', 70, 'bold'))
            time.sleep(2)
            sys.exit()
        else:
            while self.start != "1" and self.start != "2":
                screen = turtle.Screen()
                self.start = screen.textinput("Do you want to play?", "Type a number (1 or 2)")
            pen1.screen.clear()

    def choose_level(self):
        """ Use the Python Turtle Graphics window to interact with the user
        by asking whether the user wants to play which level (from 3 levels)
        in this game.

        :return: string
        """
        win = turtle.Screen()
        win.bgcolor("#fdf5e6")
        win.register_shape("spark.gif")
        win.register_shape("molang.gif")
        sp = turtle.Turtle()
        mol1 = turtle.Turtle()
        mol1.hideturtle()
        sp.hideturtle()
        sp.penup()
        mol1.penup()
        sp.goto(500, -200)
        mol1.goto(-500, -330)
        mol1.showturtle()
        sp.showturtle()
        mol1.shape("molang.gif")
        sp.shape("spark.gif")
        pen1 = turtle.Turtle()
        pen1.hideturtle()
        pen1.penup()
        pen1.screen.bgcolor("#fdf5e6")
        pen1.goto(0, 200)
        pen1.color("#8b4513")
        self.rec(1000, 120, "#708090", "#b0b4de", 200)
        pen1.write("Please choose the level", move=False, align='center', font=('Comic Sans MS', 50, 'bold'))
        pen1.goto(0, 0)
        self.rec(500, 90, "#bc8f8f", "#ffe4e1", -20)
        pen1.write("1 : Basic", move=False, align='center', font=('Comic Sans MS', 40, 'bold'))
        pen1.goto(0, -150)
        self.rec(500, 90, "#bc8f8f", "#ffe4e1", -170)
        pen1.write("2 : Intermediate", move=False, align='center', font=('Comic Sans MS', 40, 'bold'))
        pen1.goto(0, -300)
        self.rec(500, 90, "#bc8f8f", "#ffe4e1", -320)
        pen1.write("3 : Expert", move=False, align='center', font=('Comic Sans MS', 40, 'bold'))
        screen = turtle.Screen()
        if self.start == "1":
            level = screen.textinput("Choose the level you want to play", "Type a number (1-3)")
            while (not level.isnumeric()) or int(level) <= 0 or int(level) > 3:
                level = screen.textinput("Please try again", "Invalid number. Please try again")
            if level == "1":
                user_level = "basic.txt"
            elif level == "2":
                user_level = "intermediate.txt"
            else:
                user_level = "expert.txt"
            pen1.screen.clear()
            return user_level
        else:
            pass

    def times_input(self):
        """ Use the Python Turtle Graphics window to interact with the user by asking
        how many times the user wants to play this game (in one round).

        :return int
        """
        win = turtle.Screen()
        win.bgcolor("#fdf5e6")
        win.register_shape("loading.gif")
        win.register_shape("tree.gif")
        hm = turtle.Turtle()
        hm.speed(0)
        tree = turtle.Turtle()
        tree.speed(0)
        tree.color("#fdf5e6")
        tree.hideturtle()
        hm.hideturtle()
        hm.color("#fdf5e6")
        hm.penup()
        hm.goto(-500, -300)
        hm.showturtle()
        hm.shape("loading.gif")
        tree.penup()
        tree.goto(600, -250)
        tree.showturtle()
        tree.shape("tree.gif")
        pen1 = turtle.Turtle()
        pen1.penup()
        pen1.hideturtle()
        pen1.screen.bgcolor("#fdf5e6")
        pen1.goto(0, 200)
        self.rec(1000, 100, "#708090", "#b0b4de", 190)
        pen1.color("white")
        pen1.write("How many times you want to play?", move=False, align='center', font=('Comic Sans MS', 50, 'bold'))
        pen1.goto(0, 50)
        self.rec(800, 50, "#708090", "#b0b4de", 5)
        pen1.write("You can choose from 1 to 50", move=False, align='center', font=('Comic Sans MS', 30, 'bold'))
        screen = turtle.Screen()
        times = screen.textinput("How many times you want to play?", "Please input a number")
        while (not times.isnumeric()) or int(times) <= 0 or int(times) > 50:
            screen = turtle.Screen()
            times = screen.textinput("Please try again", "Invalid number. Please try again")
        pen1.screen.clear()
        return int(times)

    def board(self):
        """ Use the Python Turtle to draw the board background for wrong alphabet input."""
        tree = turtle.Turtle()
        tree.color("#fdf5e6")
        tree.speed(0)
        tree.hideturtle()
        tree.penup()
        tree.goto(600, -250)
        tree.showturtle()
        tree.shape("tree.gif")
        turtle.color("#fdf5e6")
        turtle.hideturtle()
        turtle.penup()
        turtle.pensize(3)
        turtle.speed(0)
        turtle.goto(150, 190)
        turtle.pendown()
        turtle.shape()
        turtle.color("#bc8f8f")
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(300)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
        turtle.end_fill()
        turtle.pu()
        turtle.goto(160, 200)
        turtle.color("#ffe4e1")
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(300)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
        turtle.end_fill()

    def lose(self, w):
        """ Use the Python Turtle to draw the page showing that the user lose this round."""
        pen1 = turtle.Turtle()
        pen1.color("#fdf5e6")
        pen1.pu()
        pen1.goto(0, 0)
        pen1.hideturtle()
        pen1.screen.bgcolor("gray")
        pen1 = turtle.Turtle()
        pen1.penup()
        pen1.hideturtle()
        pen1.goto(0, -100)
        pen1.screen.clear()
        pen1.screen.bgpic("gameover.gif")
        pen1.color("red")
        pen1.write("The word is " + w, move=False, align='center', font=('Comic Sans MS', 35, 'bold'))
        pen1.pensize(8)
        pen1.goto(0, 0)
        pen1.write("GAME OVER", move=False, align='center', font=('Comic Sans MS', 70, 'bold'))
        time.sleep(2)
        pen1.screen.clear()

    def win(self):
        """ Use the Python Turtle to draw the page showing that the user win this round."""
        pen1 = turtle.Turtle()
        pen1.pu()
        pen1.goto(-3, -3)
        pen1.hideturtle()
        pen1.screen.clear()
        pen1.screen.bgcolor("#f0fff0")
        win = turtle.Screen()
        win.register_shape("win.gif")
        happy = turtle.Turtle()
        happy.hideturtle()
        happy.penup()
        happy.goto(0, -300)
        happy.showturtle()
        happy.shape("win.gif")
        pen1.pensize(8)
        pen1.color("#9370DB")
        pen1.write("YOU WIN", move=False, align='center', font=('Comic Sans MS', 70, 'bold'))
        pen1.goto(0, 0)
        pen1.color("#e6e6fa")
        pen1.write("YOU WIN", move=False, align='center', font=('Comic Sans MS', 70, 'bold'))
        time.sleep(2)
        pen1.screen.clear()
        self.win_rate += 1

    def summarize(self, times):
        """Use the Python Turtle to summarize the score for user."""
        pen1 = turtle.Turtle()
        pen1.pu()
        pen1.goto(0, 0)
        pen1.hideturtle()
        pen1.screen.clear()
        pen1.screen.bgcolor("#fdf5e6")
        pen1.pensize(8)
        self.rec(1000, 80, "#bc8f8f", "#ffe4e1", -20)
        pen1.goto(-3, -3)
        pen1.color("#696969")
        pen1.write(f"You got {self.win_rate} out of {times}", move=False, align='center',
                   font=('Comic Sans MS', 50, 'bold'))
        pen1.goto(0, 0)
        pen1.color("white")
        pen1.write(f"You got {self.win_rate} out of {times}", move=False, align='center',
                   font=('Comic Sans MS', 50, 'bold'))
        time.sleep(3)
        pen1.screen.clear()
