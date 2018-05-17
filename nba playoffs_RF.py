import pyautogui as pg
import webbrowser

answer = pg.confirm(text="Which Conference Are You Interested In?", title="Choose your conference", buttons=['East', 'West'])


if answer == "East":
    question2 = pg.confirm("Which team are you intrested in?","Choose your team", ["Toronto Raptors", "Boston Celtics", "Philadelphia 76ers", "Cleveland Cavaliers", "Indiana Pacers", "Miami Heat", "Milwaukee Bucks", "Washington Wizards"])
    if question2 == "Toronto Raptors":
        webbrowser.open("http://www.espn.com/nba/team/_/name/tor/toronto-raptors")
    elif question2 == "Boston Celtics":
        webbrowser.open("http://www.espn.com/nba/team/_/name/bos/boston-celtics")
    elif question2 == "Philadelphia 76ers":
        webbrowser.open("http://www.espn.com/nba/team/_/name/phi/philadelphia-76ers")
    elif question2 == "Cleveland Cavaliers":
        webbrowser.open("http://www.espn.com/nba/team/_/name/cle/cleveland-cavaliers")
    elif question2 == "Indiana Pacers":
        webbrowser.open("http://www.espn.com/nba/team/_/name/ind/indiana-pacers")
    elif question2 == "Miami Heat":
        webbrowser.open("http://www.espn.com/nba/team/_/name/mia/miami-heat")
    elif question2 == "Milwaukee Bucks":
        webbrowser.open("http://www.espn.com/nba/team/_/name/mil/milwaukee-bucks")
    elif question2 == "Washington Wizards":
        webbrowser.open("http://www.espn.com/nba/team/_/name/was/washington-wizards")
    
    
if answer == "West":
    question3 = pg.confirm("Which team are you intrested in?","Choose your team", ["Houston Rockets", "Golden State Warriors", "Portland Trail Blazers", "Oklahoma City Thunder", "Utah Jazz", "New Orleans Pelicans", "San Antonio Spurs", "Minnesota Timberwolves"])
    if question3 == "Houston Rockets":
        webbrowser.open("http://www.espn.com/nba/team/_/name/hou/houston-rockets")
    elif question3 == "Golden State Warriors":
        webbrowser.open("http://www.espn.com/nba/team/_/name/gs/golden-state-warriors")
    elif question3 == "Portland Trail Blazers":
        webbrowser.open("http://www.espn.com/nba/team/_/name/por/portland-trail-blazers")
    elif question3 == "Oklahoma City Thunder":
        webbrowser.open("http://www.espn.com/nba/team/_/name/okc/oklahoma-city-thunder")
    elif question3 == "Utah Jazz":
        webbrowser.open("http://www.espn.com/nba/team/_/name/utah/utah-jazz")
    elif question3 == "New Orleans Pelicans":
        webbrowser.open("http://www.espn.com/nba/team/_/name/no/new-orleans-pelicans")
    elif question3 == "San Antonio Spurs":
        webbrowser.open("http://www.espn.com/nba/team/_/name/sas/San Antonio Spurs")
    elif question3 == "Minnesota Timberwolves":
        webbrowser.open("http://www.espn.com/nba/team/_/name/min/minnesota-timberwolves")

