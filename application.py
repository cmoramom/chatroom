import datetime

from flask import Flask
from flask_socketio import SocketIO
from flask_wtf import CSRFProtect

from config import config
from resources.auth import bp_auth
from resources.home import bp_home
from resources.index import bp_index
from utils.consume_api import Consume
from utils.csv_to_json import CVStoJSON
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


# this controls the socketIO workflow and calls the chatbot API
# if the stock_code is sent in the chat meessage

@socketio.on('my event')
def handle_my_custom_event(json):
    print('Event: ' + str(json))
    command = json.get('message')
    time = datetime.datetime.now()
    json.update({"timestamp": time.strftime("%m/%d/%Y, %H:%M:%S")})
    socketio.emit('response_message', json)
    if '/stock=' in str(command):
        stock_code = command.split('=')[1]

        url = str(config.CHATBOT_API[0])
        #http://stooq.com/q/l/?s={0}&f=sd2t2ohlcv&h&e=csv'.format(stock_code)
        data = str(config.API_TO_CONSUME[0]).format(stock_code)
        api = Consume(url=url, data=data)
        data = api.consume_api()
        if data is not None:
            response_msg = {'user_name': 'ChatBot', 'timestamp': time.strftime("%m/%d/%Y, %H:%M:%S"),
                            'message': 'Processing stock code = ' + stock_code}
            socketio.emit('response_message', response_msg)
        else:
            response_msg = {'user_name': 'ChatBot', 'timestamp': time.strftime("%m/%d/%Y, %H:%M:%S"),
                            'message': 'Error processing stock code = ' + stock_code}

        socketio.emit('response_message', response_msg)


if __name__ == '__main__':
    socketio.run(application, debug=True)
