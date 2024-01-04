from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for Red Sox team
red_sox_info = {
    "team_name": "Boston Red Sox",
    "seasons": "123 (1901 to 2023)",
    "record": "9874-9182, .518 W-L%",
    "playoff_appearances": "25",
    "pennants": "14",
    "world_series_wins": 9,
    "home_ballpark": "Fenway Park"
}

# Sample data for Red Sox players
red_sox_players = [
    {"id": 1, "name": "Connor Wong", "position": ["Catcher"]},
    {"id": 2, "name": "Caleb Hamilton", "position": ["Catcher"]},
    {"id": 3, "name": "Jorge Alfaro", "position": ["Catcher"]},
    {"id": 4, "name": "Reese McGuire", "position": ["Catcher"]},
    {"id": 5, "name": "Triston Casas", "position": ["First Base"]},
    {"id": 6, "name": "Bobby Dalbec", "position": ["First Base", "Shortstop"]},
    {"id": 7, "name": "Christian Arroyo", "position": ["Second Base", "Shortstop"]},
    {"id": 8, "name": "David Hamilton", "position": ["Second Base"]},
    {"id": 9, "name": "Luis Urias", "position": ["Second Base"]},
    {"id": 10, "name": "Enmanuel Valdez", "position": ["Second Base"]},
    {"id": 11, "name": "Rafael Devers", "position": ["Third Base"]},
    {"id": 12, "name": "Trevor Story", "position": ["Shortstop"]},
    {"id": 13, "name": "Kike Hernandez", "position": ["Second Base", "Center Field", "Shortstop"]},
    {"id": 14, "name": "Pablo Reyes", "position": ["Second Base", "Shortstop"]},
    {"id": 15, "name": "Yu Chang", "position": ["Second Base", "Third Base", "Shortstop"]},
    {"id": 16, "name": "Masataka Yoshida", "position": ["Left Field", "Designated Hitter"]},
    {"id": 17, "name": "Rob Refsnyder", "position": ["Utility Outfield"]},
    {"id": 18, "name": "Ramiel Tapia", "position": ["Utility Outfield"]},
    {"id": 19, "name": "Ceddanne Rafaela", "position": ["Center Field"]},
    {"id": 20, "name": "Jarren Duran", "position": ["Center Field"]},
    {"id": 21, "name": "Adam Duvall", "position": ["Center Field"]},
    {"id": 22, "name": "Alex Verdugo", "position": ["Right Field"]},
    {"id": 23, "name": "Wilyer Abreu", "position": ["Right Field"]},
    {"id": 24, "name": "Justin Turner", "position": ["First Base", "Third Base", "Designated Hitter"]},
    {"id": 25, "name": "Tanner Houck", "position": ["Starting Pitcher"]},
    {"id": 26, "name": "Matt Dermody", "position": ["Starting Pitcher"]},
    {"id": 27, "name": "Chris Sale", "position": ["Starting Pitcher"]},
    {"id": 28, "name": "James Paxton", "position": ["Starting Pitcher"]},
    {"id": 29, "name": "Brayan Bello", "position": ["Starting Pitcher"]},
    {"id": 30, "name": "Garrett Whitlock", "position": ["Starting Pitcher", "Relief Pitcher"]},
    {"id": 31, "name": "Kutter Crawford", "position": ["Starting Pitcher", "Relief Pitcher"]},
    {"id": 32, "name": "Corey Kluber", "position": ["Starting Pitcher", "Relief Pitcher"]},
    {"id": 33, "name": "Nick Pivetta", "position": ["Starting Pitcher", "Relief Pitcher"]},
    {"id": 34, "name": "Ryan Sherriff", "position": ["Relief Pitcher"]},
    {"id": 35, "name": "Ryan Brasier", "position": ["Relief Pitcher"]},
    {"id": 36, "name": "Nick Robertson", "position": ["Relief Pitcher"]},
    {"id": 37, "name": "Brandon Walter", "position": ["Relief Pitcher"]},
    {"id": 38, "name": "Joe Jacques", "position": ["Relief Pitcher"]},
    {"id": 39, "name": "Zack Weiss", "position": ["Relief Pitcher"]},
    {"id": 40, "name": "Taylor Scott", "position": ["Relief Pitcher"]},
    {"id": 41, "name": "Jake Faria", "position": ["Relief Pitcher"]},
    {"id": 42, "name": "John Schreiber", "position": ["Relief Pitcher"]},
    {"id": 43, "name": "Mauricio Llovera", "position": ["Relief Pitcher"]},
    {"id": 44, "name": "Justin Garza", "position": ["Relief Pitcher"]},
    {"id": 45, "name": "Kyle Barraclough", "position": ["Relief Pitcher"]},
    {"id": 46, "name": "Chris Murphy", "position": ["Relief Pitcher"]},
    {"id": 47, "name": "Joely Rodriguez", "position": ["Relief Pitcher"]},
    {"id": 48, "name": "Richard Bleier", "position": ["Relief Pitcher"]},
    {"id": 49, "name": "Josh Wincowski", "position": ["Relief Pitcher"]},
    {"id": 50, "name": "Kenley Jansen", "position": ["Relief Pitcher"]},
    {"id": 51, "name": "Chris Martin", "position": ["Relief Pitcher"]},
    {"id": 52, "name": "Kaleb Ort", "position": ["Relief Pitcher"]},
    {"id": 53, "name": "Zack Littel", "position": ["Relief Pitcher"]},
    {"id": 54, "name": "Zack Kelley", "position": ["Relief Pitcher"]},
    {"id": 55, "name": "Brennan Bernardino", "position": ["Relief Pitcher"]},
]

top_players = [
    {"name": "Ted Williams", "image_url": "/static/images/ted_williams.jpg"},
    {"name": "Carl Yastrzemski", "image_url": "/static/images/carl_yastrzemski.jpg"},
    {"name": "Roger Clemens", "image_url": "/static/images/roger_clemens.jpg"},
    {"name": "Wade Boggs", "image_url": "/static/images/wade_boggs.jpg"},
    {"name": "Cy Young", "image_url": "/static/images/cy_young.jpg"},
    {"name": "Dwight Evans", "image_url": "/static/images/dwight_evans.jpg"},
    {"name": "Tris Speaker", "image_url": "/static/images/tris_speaker.jpg"},
    {"name": "Pedro Martinez", "image_url": "/static/images/pedro_martinez.jpg"},
    {"name": "David Ortiz", "image_url": "/static/images/david_ortiz.jpg"},
    {"name": "Dustin Pedroia", "image_url": "/static/images/dustin_pedroia.jpg"},
    # Add more players as needed
]

# A dictionary to store the correct answers (player names)
correct_answers = {player['id']: player['name'] for player in red_sox_players}

@app.route('/')
def team_home():
    return render_template('team_info.html', team_info=red_sox_info, top_players=top_players)

@app.route('/players_list')
def players_list():
    return render_template('index.html', players=red_sox_players)

@app.route('/player/<int:player_id>')
def player_detail(player_id):
    player = next((p for p in red_sox_players if p["id"] == player_id), None)
    if player:
        return render_template('player_detail.html', player=player)
    else:
        return "Player not found", 404

@app.route('/name_the_players', methods=['GET', 'POST'])
def name_the_players():
    if request.method == 'POST':
        # Process user input and calculate the score
        user_answers = {f'player_{player["id"]}': request.form[f'player_{player["id"]}'] for player in red_sox_players}
        score = sum(1 for user_answer in user_answers.values() if check_answer(user_answer))
        total_questions = len(correct_answers)

        return render_template('score.html', score=score, total=total_questions, correct_answers=correct_answers)

    return render_template('name_the_players.html', players=red_sox_players)

def check_answer(user_answer):
    # Check if the user's answer matches any of the correct positions for any player
    for player_id, correct_positions in correct_answers.items():
        if any(position.lower() == user_answer.lower() for position in correct_positions):
            return False
    return True

@app.route('/sox_logs')
def sox_logs():
    return render_template('sox_logs.html')

if __name__ == '__main__':
    app.run(debug=True)