import turtle,pandas
SCREEN=turtle.Screen()
turtle.title("Map Game :")
turtle.bgpic("assets/map-arab-countries.gif")
turtle.setup(width=890,height=511)
turtle.tracer(0)
DATA=pandas.read_csv("assets/coordinates.csv")
COUNTRIES=DATA.COUNTRY.to_list()
GUESSED=[]
MISSING_COUNTRIES=[]
while len(GUESSED)<17:
    ANSWER=turtle.textinput(title=f"Guess A Country :{len(GUESSED)}/17",prompt="Type a Country And Hit to Enter or Type Exit to Quit :").title()
    if ANSWER in COUNTRIES:
        GUESSED.append(ANSWER)
        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        COUNTRY_X=DATA[DATA.COUNTRY==ANSWER]["X"].item()
        COUNTRY_Y=DATA[DATA.COUNTRY==ANSWER]["Y"].item()
        t.goto(COUNTRY_X,COUNTRY_Y)
        t.pendown()
        t.write(ANSWER,font=("Arial",10,"normal"))
        t.begin_fill()
        t.color("red")
        t.fillcolor()
        t.circle(5)
        t.end_fill()
    elif ANSWER=="Exit":
        for country in COUNTRIES:
            if country not in GUESSED:
                MISSING_COUNTRIES.append(country)
                FINAL_FILE=pandas.DataFrame(MISSING_COUNTRIES)
                FINAL_FILE.to_csv("assets/missing_countries.csv")
        break





