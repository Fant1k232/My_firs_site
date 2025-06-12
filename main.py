from flask import Flask, redirect, render_template, request, session, url_for
from db_script import get_bio_team, get_bio_driver, get_races_driver, get_wins_driver

app = Flask(__name__, template_folder="temp",static_folder="temp/img")


def index():
    return render_template("index.html")
def calendar():
    return render_template("calendar.html")
def teams():
    return render_template("teams.html")
def drivers():
    return render_template("drivers.html")

@app.route("/team/<teamname>")
def team(teamname):
    bio = get_bio_team(teamname)
    bio = str(bio)
    dont_need='"()[]'
    bio_result = "".join([char for char in bio if char not in dont_need])
    bg = "/img/"+teamname+"_bg.png"
    name = teamname
    dont_need_name = "_"
    name_result = "".join([char for char in name if char not in dont_need_name])
    return render_template("teams_sh.html",bio=bio_result,bg=bg, name=name_result)
@app.route("/drivers/<drivername>")
def one_driver(drivername):
    bio, racas,wins = get_bio_driver(drivername),get_races_driver(drivername),get_wins_driver(drivername)
    bio, racas, wins = str(bio),str(racas),str(wins)
    dont_need = '"[](),'
    bio_result = "".join([char for char in bio if char not in dont_need])
    racas_result = "".join([char for char in racas if char not in dont_need])
    wins_result = "".join([char for char in wins if char not in dont_need])
    return render_template("driver_sh.html", name=drivername,bio=bio_result,races=racas_result,wins=wins_result,bg="/img/"+"driver_bg.png")


app.config["SECRET_KEY"] = "123qweewq321"

app.add_url_rule("/","index",index)
app.add_url_rule("/calendar","calendar",calendar)
app.add_url_rule("/teams","teams",teams)
app.add_url_rule("/drivers","drivers",drivers)

if __name__ == "__main__":
    app.run()