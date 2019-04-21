import datetime

from flask import Flask
from flask_socketio import SocketIO
from flask_wtf import CSRFProtect
from resources.auth import bp_auth
from resources.home import bp_home
from resources.index import bp_index
from utils.generate_hash import GenerateHash

application = Flask(__name__)
socketio = SocketIO(application)
application.config.from_object('config.config')
application.jinja_env.autoescape = True
application.jinja_env.globals['csrf_token'] = \
    GenerateHash(value_to_hash='this needs to be hash').generate()
application.register_blueprint(bp_auth)
application.register_blueprint(bp_index)
application.register_blueprint(bp_home)
CSRFProtect(application)


@socketio.on('my event')
def handle_my_custom_event(json):
    print('Event: ' + str(json))
    command = json.get('message')
    time = datetime.datetime.now()
    json.update({"timestamp": time.strftime("%m/%d/%Y, %H:%M:%S")})
    socketio.emit('response_message', json)
    if '/stock=' in str(command):
        print(command)
        response_dict = {'user_name': 'ChatBot', 'timestamp':time.strftime("%m/%d/%Y, %H:%M:%S"),
                         'message':'Processing command...'}
        socketio.emit('response_message', response_dict)


if __name__ == '__main__':
    socketio.run(application, debug=True)
