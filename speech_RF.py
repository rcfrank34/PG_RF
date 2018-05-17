import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What is your name? Note: I am with the CIA, and am recording all of your information and sending it to the Secret Service.")
answer = pg.prompt("Enter your name.")

speak.Speak("Hello " + answer + ". I will be recording you forever.")


speak.Speak("What is your favorite color? Recording...")
color = pg.prompt("Enter in your favorite color.")

if color == "Red":
    speak.Speak("Thank you, but the favorite color of....INSERT COLOR....red is most common amongst criminals. A SWAT team is on its way.")

else:
    speak.Speak("Thank you. Your answer has been recorded, letting us learn more about you")

speak.Speak("What video would you like to watch? Note: I can watch it with you because I have remote control over your computer.")
video = pg.prompt("Enter video here")
wb.open("https://www.youtube.com/results?search_query=" + video)
