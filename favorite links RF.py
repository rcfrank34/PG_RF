import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=jwerp2SNiTQ","https://www.youtube.com/watch?v=RUlyvjxutE0"]

music = ["https://www.spotify.com/us/","https://soundcloud.com/"]

answer = pg.prompt(
"""
Which would you rather do?
a)Watch videos
b)Listen to music


"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)


elif answer == "b":
    for i in music:
        webbrowser.open(i)

