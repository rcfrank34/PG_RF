import pyautogui as pg
import webbrowser

English = ["https://docs.google.com/document/d/1SsZ9B7Ee2AHwMW78J3aTmV0d8y6ldprYOXHdLbOss6U/edit"]

Math = ["https://docs.google.com/spreadsheets/d/1XCutu8j7jy6_HFJSNhbu_84J0msWd26Gsub6dfFRKTU/edit#gid=0"]

answer = pg.prompt(
"""
Which would you rather do?
a)English Homework
b)Math Homework


"""
    )

if answer == "a":
    for i in English:
        webbrowser.open(i)


elif answer == "b":
    for i in Math:
        webbrowser.open(i)
