import sys
sys.path.append('libs') # Include files in the "libs" folder


from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from ants_plans import create_game_state
from ants import *
import logging, socket
import webbrowser


app = Flask(__name__, static_folder='static') # Create flask app
socketio = SocketIO(app) # Use websocket
game, game_state = None, None # Global variable to represent a game and a gamestate


# Disable verbose for Flask messages
def disable_verbose():
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR) # Disable verbose for Flask messages


# Create new game
def create_new_game():
    """Create new game by reseting game_state and game"""
    global game_state, game
    game_state = create_game_state()
    game = game_state.simulate()


# Automatically called by socketio when client connects to server
@socketio.on('connect')
def handle_connect():
    socketio.emit('loadLobby', {}) # Send loadLobby signal to frontend
    """
    Note: index() is also called when the user loads the webpage, so technically this function can be merged into index()
    But this is here because index() must return to render the html, but we want to load the lobby only after rendering the html,
    so this must be a seperate function and this would be called after index() returns and renders the html.
    """


# Automatically called by flask when loading webpage
@app.route('/')
def index():
    # Loads/renders index.html
    print('\n ===== New Game Started ===== \n')
    create_new_game()
    return render_template('index.html')


@app.route('/initialize_game', methods=['POST'])
def initialize_game():
    "Called by the front end when it's time to start a game."
    next(game) # Advance the game

    game_data = {
        'dimensions_x': game_state.dimensions[0],
        'dimensions_y': game_state.dimensions[1],
        'ant_types': [str(ant) for ant in game_state.ant_types],
    }

    wet_places = [place for place in game_state.places.values() if type(place) is Water]

    # Parse the names of places to figure out where they are.
    game_data['wet_places'] = [[int(place.name.split('_')[1]), int(place.name.split('_')[2])] for place in wet_places]

    return jsonify(game_data) # Send game_data back to frontend


@app.route('/deploy_ants', methods=['POST'])
def deploy_ants():
    "Called by the front end when it's time to deploy an ant."
    data = request.get_json()
    pos = data.get('pos').split('-') # in the form of 'row-col'
    tunnel = f'tunnel_{pos[0]}_{pos[1]}'
    ant_name = data.get('ant')
    message = {
        'deployed': False,
        'insect_id': None
    }

    ant = None
    try:
        ant = game_state.deploy_ant(tunnel, ant_name)
    except KeyError: # tile is wet
        tunnel = f'water_{pos[0]}_{pos[1]}'
        ant = game_state.deploy_ant(tunnel, ant_name)
    finally:
        if ant: # If successfuly deployed ant
            message['deployed'] = True
            message['insect_id'] = ant.id

    return jsonify(message)


def insects_take_actions():
    """Ask insects to take actions by advancing the game. Signal frontend through socket if game ended."""
    result = next(game)
    if result is True:
        socketio.emit('endGame', {'antsWon': True})
    elif result is False:
        socketio.emit('endGame', {'antsWon': False})
    return jsonify({})


@app.route('/ants_take_actions')
def ants_take_actions():
    return insects_take_actions()


@app.route('/bees_take_actions')
def bees_take_actions():
    return insects_take_actions()


@app.route('/update_stats')
def update_stats():
    "Send food count, turn count, and available ants to frontend."
    data = {
        'food': game_state.food,
        'turn': game_state.time,
        'available_ants': [ant.name for ant in game_state.ant_types.values() if ant.food_cost <= game_state.food]
    }
    return jsonify(data)


def move_bee(bee, place):
    "Send message to frontend to move a bee from one place to another."
    data = {
        'bee_id': bee.id,

        # Not a good way to get the position. Changes should be made to Place class in ants.py
        'destination': place.name.split('_')[1:], # [x, y] where x is row, y is col
        'current_pos': bee.place.name.split('_')[1:],
    }
    socketio.emit('moveBee', data)


def move_bee_from_hive(bee, place):
    "Send message to frontend to move a bee from the hive."
    data = {
        'bee_id': bee.id,
        'bee_name': bee.name,

        # Not a good way to get the position. Changes should be made to Place class in ants.py
        'destination': place.name.split('_')[1:] # [x, y] where x is row, y is col
    }
    socketio.emit('moveBeeFromHive', data)


def insect_move_decorator(func):
    """A decorator that takes in the original move_to method of a bee.
    Calls corresponding GUI functions to move bee before calling the original method.
    """
    def inner(self, place):
        if type(self.place) == Hive:
            move_bee_from_hive(self, place)
        else:
            move_bee(self, place)
        return func(self, place)
    return inner


def throw_at_decorator(func):
    """A decorator for Thrower's throw_at method."""
    def inner(self, target):
        if target is not None:
            data = {
                'target_pos': target.place.name.split('_')[1:],
                'thrower_pos': self.place.name.split('_')[1:],
            }
            socketio.emit('throwAt', data)
        func(self, target)
    return inner


def reduce_health_decorator(func):
    """A decorator for Insect's reduce_health method."""
    def inner(self, amount):
        data = {'insect_id': self.id}
        socketio.emit('reduceHealth', data)
        return func(self, amount)
    return inner


def zero_health_callback_gui(self):
    """A callback for when an insect reaches zero health."""
    data = {'insect_id': self.id}
    socketio.emit('onInsectDeath', data)


def decorate_events():
    Bee.move_to = insect_move_decorator(Bee.move_to)
    ThrowerAnt.throw_at = throw_at_decorator(ThrowerAnt.throw_at)
    Insect.reduce_health = reduce_health_decorator(Insect.reduce_health)
    Insect.zero_health_callback = zero_health_callback_gui


def display_messages(port):
    print('\n******************** Ants vs SomeBees GUI ********************\n')
    print('Instructions: ')
    print('  Hit Control + C to stop running this file')
    print('  Refresh webpage to start new game')
    print(f'  Game available at: http://127.0.0.1:{port}/\n')


def is_port_open(port):
    """
    Checks if a port is open on the localhost.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('localhost', port))
            return True
        except OSError:
            print(f'*** Can not access port {port} ***')
            return False


if __name__ == '__main__':
    disable_verbose()
    decorate_events()
    create_new_game()
    for port in [31415, 8000, 5555, 5000]: # Determining an open port
        if is_port_open(port):
            open_port = port
            break
    else:
        raise Exception("Ports 8000, 5555, and 5000 are all occupied")
    display_messages(open_port)
    webbrowser.open("http://localhost:" + str(open_port), new=0, autoraise=True)
    sys.tracebacklimit = 1
    app.run(debug=False, port=open_port)


"""
Contributors: Benji Xu, Justin Park, Noah Han, Jim Feng, Rajoshi Basu, Susanna Atanessian, Maria Rufova
Special thanks to John DeNero, Ken Zheng, Hans Mao, Amy Xu, Shane Guo, Robert Shi, Ayush Mahale, Lyndon Yang, Shamith Pasula
29th, Feb, 2024, Berkeley, CA
"""