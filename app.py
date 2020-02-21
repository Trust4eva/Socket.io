# app.py
import os, flask, flask_socketio  
import flask_sqlalchemy


app = flask.Flask(__name__)
import models
#socketio = flask_socketio.SocketIO(app) 

@app.route('/')
#def hello():
 #   return flask.render_template('index.html')
    
def index():
    messages = models.Message.query.all()
    html = ['<li>' + m.text + '</li>' for m in messages]
    return '<ul>' + ''.join(html) + '</ul>'

    
if __name__ == '__main__':
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
"""
@socketio.on('connect') 
def on_connect():
    print('Someone connected!')
    
    socketio.emit('update', {
        'data': 'Got your connection!'
    })
    
socketio.run(
    app,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
"""