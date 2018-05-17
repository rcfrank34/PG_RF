import pyautogui as pg
import time
import webbrowser

points = 0

# Question 1

answer = pg.prompt(
"""
What is your favorite city?

a) Boston
b) Pittsburgh
c) New York
d) Los Angeles
"""
    )


# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4


# Question 2

answer = pg.prompt(
"""
Who is your favorite player?

a) Antonio Brown
b) Aaron Judge
c) Lonzo Ball
d) Kyrie Irving
"""
    )


# Give points

if answer == "a":
    points += 2
elif answer == "b":
    points += 3
elif answer == "c":
    points += 4
elif answer == "d":
    points += 1


# Question 3

answer = pg.prompt(
"""
What would you rather do in your free time?

a) Ride the subway
b) Come up with new touchdown celebrations
c) Cheat in a game
d) Go party in Beverly Hills
"""
    )


# Give points

if answer == "a":
    points += 3
elif answer == "b":
    points += 2
elif answer == "c":
    points += 1
elif answer == "d":
    points += 4


# Question 4

answer = pg.prompt(
"""
What is your favorite food?

a) Clam Chowder
b) Pizza
c) In N' Out Burger
d) Hogie
"""
    )


# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 3
elif answer == "c":
    points += 4
elif answer == "d":
    points += 2


# END OF SURVEY

pg.alert("You are a fan of...")

# Boston
if points < 7:
    pg.alert("Boston Sports")
    webbrowser.open("https://www.youtube.com/watch?v=qJuTxoYhbBo")

# Pittsburgh
elif points >= 7 and points < 10:
    pg.alert("Pittsburgh Sports")
    webbrowser.open("https://www.youtube.com/watch?v=B84b0Yqd8Kc")

# New York
elif points >= 10 and points < 14:
     pg.alert("New York Sports")
     webbrowser.open("https://www.youtube.com/watch?v=pyFkPo0dm_I")

# Los Angeles
elif points >= 14:
    pg.alert("Los Angeles Sports")
    webbrowser.open("https://www.youtube.com/watch?v=iYL-k7SOOkE")
