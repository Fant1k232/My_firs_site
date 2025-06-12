import sqlite3

conn = sqlite3.connect("f1.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Teams (id INTEGER PRIMARY KEY,name VARCHAR, bio VARCHAR, bg VARCHAR)")
cursor.execute("CREATE TABLE IF NOT EXISTS Driver (id INTEGER PRIMARY KEY, name VARCHAR, bio VARCHAR, races INTEGER, wins INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS Connect (id INTEGER PRIMARY KEY, team_id INTEGER, driver_id INTEGER, FOREIGN KEY(team_id) REFERENCES Team(id),FOREIGN KEY(driver_id) REFERENCES Driver(id))")
conn.commit()

f1_teams_info = [("Red_Bull_Racing","Red Bull were no strangers to F1 - as sponsors - prior to formally entering as a works team in 2004. Nonetheless, the scale of their success over the following decadewas staggering. After a first podium in 2006, the team hit their stride in 2009, claiming six victories and second in the constructors' standings. Over the next fourseasons they were a tour de force, claiming consecutive title doubles between 2010 and 2013, with Sebastian Vettel emerging as the sport's youngest quadruple champion. Now they are recapturing that glory with an equally exciting talent – one named Max Verstappen…","img/rb_bg.png"),
                 ("McLaren", "Since entering the sport in 1966 under the guidance and restless endeavour of eponymous founder Bruce, McLaren's success has been nothing short of breathtaking. Five glittering decades have yielded countless victories, pole positions and podiums, not to mention nine constructors' championships. What's more, some of the sport's greatest drivers made their names with the team, including Emerson Fittipaldi, Ayrton Senna, Mika Hakkinen and Lewis Hamilton...", "img/mc_bg.png"),
                 ("Ferrari","For many, Ferrari and Formula 1 racing have become inseparable. The only team to have competed in every season since the world championship began, the Prancing Horse has grown from the humble dream of founder Enzo Ferrari to become one of the most iconic and recognised brands in the world. Success came quickly through the likes of Alberto Ascari and John Surtees, and continued – in amongst leaner times – with Niki Lauda in the 1970s and then Michael Schumacher in the 2000s, when Ferrari claimed a then unprecedented five consecutive title doubles, securing their status as the most successful and decorated team in F1 history...", "img/fr_bg.png"),
                 ("Mercedes","Mercedes’ modern F1 revival started with the creation of a works squad for 2010 - the platform for a meteoric rise up the Grand Prix order. The team generated huge excitement from the off with the sensational return of Michael Schumacher, but headlines soon followed on track: three podiums in their debut season, all via Nico Rosberg - who then claimed a breakthrough pole/victory double at China in 2012. The following season he was paired with Lewis Hamilton, the duo going on to stage some epic title battles as the Silver Arrows swept all before them to become one of the most dominant forces of the modern F1 era – until Red Bull came and stole that crown. Nevertheless, with proven race-winner George Russell now partnered by rising star Kimi Antonelli, Mercedes remain very much one of the teams to beat…","img/mr_bg.png"),
                 ("Alpine", "Alpine may be a relatively new name to Formula 1, but Renault’s famous sportscar arm has plenty of motorsport heritage. The 2021 rebrand of the team marked the next step in Renault’s F1 revival, begun in 2016 with the takeover of the then-Lotus squad. Already race winners in their new guise, regular podiums and a tilt at the title must be their next target…", "img/al_bg.png"),
                 ("Aston_Martine","Aston Martin’s original Formula 1 foray – over half a century ago – lasted just five races. This time, though, it’s serious. This F1 squad are no strangers to success, having won in their original guise of Jordan and most recently as Racing Point in 2020. Renowned for their ability to punch above their weight, and now with a two-time champion leading their driver line-up - and F1's most famous designer coming onboard in 2025 - Aston Martin are very much a team to watch…", "img/as_bg.png"),
                 ("Haas","The youngest team on the grid, Haas made their highly impressive debut in 2016, and in the process became the first all-American-led F1 squad in three decades. Founded by industrialist Gene Haas, they are based in the United States on the same Kannapolis, North Carolina facility as his championship-winning NASCAR Sprint Cup Series team, Stewart-Haas Racing. The Ferrari-powered team also have a UK factory in Banbury", "img/ha_bg.png"),
                 ("Williams","Driven on by the brilliance and passion of the late Sir Frank Williams, Williams grew from humble beginnings to become a Formula 1 behemoth, unrivalled by all except Ferrari and McLaren in terms of enduring success. Over the past four decades the team has racked up Grand Prix wins and championship glory, and in the process nurtured some of the greatest talents in the sport, both in and out the cockpit. And, following the Williams family's decision to step aside after the 2020 sale of the team to Dorilton Capital, a new era has begun...","img/wi_bg.png"),
                 ("Racing_Bulls", "Established in 2006 as a squad in which young drivers from Red Bull’s prodigious talent pool could cut their F1 teeth, Racing Bulls – originally named Toro Rosso, then AlphaTauri, then RB – were formed from the ashes of the plucky Minardi team. Sebastian Vettel gave validity to the approach almost immediately, delivering a fairy-tale win in 2008, before going on to enjoy world championship success with parent team Red Bull Racing. Today the ethos of nurturing talent still holds true, though the Italian squad are no longer simply a ‘B team’ but a constructor in their own right...", "mg/rcb_bg.png"),
                 ("Kick_Sauder","Having enjoyed considerable success in world sportscars, where he helped nurture the emerging talents of future F1 stars Michael Schumacher and Heinz-Harald Frentzen, Peter Sauber guided his eponymous squad into F1 in 1993.The team has since established itself as a mainstay of the grid, becoming race winners under BMW’s brief ownership, and developing a well-earned reputation not only for producing competitive cars, but also for developing young drivers.In recent seasons they raced under the Alfa Romeo name - and in 2026 will become the works Audi squad - but since 2024 a new title sponsor has brought a new identity to the famous Swiss team.", "img/ki_bg.png")]
cursor.execute("DELETE FROM Teams")
cursor.execute("DELETE FROM Connect")
cursor.executemany("INSERT INTO Teams (name, bio, bg) VALUES (?,?,?)", f1_teams_info)
cursor.execute("INSERT INTO Connect (team_id, driver_id) VALUES (?,?)",[1,1])
conn.commit()
cursor.close()
conn.close()




def get_bio_team(name_team):
    conn = sqlite3.connect("f1.db")
    cursor = conn.cursor()
    cursor.execute("SELECT bio FROM Teams WHERE name=?",(name_team,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def add_driver_info():
    conn = sqlite3.connect("f1.db")
    cursor = conn.cursor()
    ans = input("Do you want add drivers y/n: ")
    if ans == "y":
        while ans =="y":
            add_name = input("Last_name:")
            add_bio = input("Bio:")
            add_races = int(input("Races:"))
            add_wins = int(input("Wins:"))
            cursor.execute("INSERT INTO Driver (name,bio,races,wins) VALUES (?,?,?,?)",[add_name,add_bio,add_races,add_wins],)
            ans = input("Do you want add drivers y/n:")

    result = cursor.execute("SELECT * FROM Driver")
    cursor.close()
    conn.commit()


def get_bio_driver(name):
    conn = sqlite3.connect("f1.db")
    cursor = conn.cursor()
    cursor.execute("SELECT bio FROM Driver WHERE name=?",(name,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
def get_races_driver(name):
    conn = sqlite3.connect("f1.db")
    cursor = conn.cursor()
    cursor.execute("SELECT races FROM Driver WHERE name=?",(name,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
def get_wins_driver(name):
    conn = sqlite3.connect("f1.db")
    cursor = conn.cursor()
    cursor.execute("SELECT wins FROM Driver WHERE name=?",(name,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def show(table):
    query = "SELECT * FROM " + table
    conn = sqlite3.connect("f1.db")
    cursor = conn.cursor()
    cursor.execute(query)
    print(cursor.fetchall())
    cursor.close()
    conn.close()

def show_tables():
    show("Teams")
    show("Driver")
    show("Connect")
