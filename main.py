from flask import Flask, redirect, render_template, request, session, url_for
from db_script import get_bio_team, get_bg_team

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



app.config["SECRET_KEY"] = "123qweewq321"

app.add_url_rule("/","index",index)
app.add_url_rule("/calendar","calendar",calendar)
app.add_url_rule("/teams","teams",teams)
app.add_url_rule("/drivers","drivers",drivers)

if __name__ == "__main__":
    app.run()