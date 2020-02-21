import flask_sqlalchemy, app, os


# app.app = app module app variable

app.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') #'postgresql://trust:Jmsimqz4@localhost/postgres'
db = flask_sqlalchemy.SQLAlchemy(app.app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # key
    text = db.Column(db.String(120))
    
    def __init__(self, t):
        self.text = t
        
    def __repr__(self):
        return '<Usps address: %s>' % self.address 
