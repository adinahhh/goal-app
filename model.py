from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """ Users stored in the database"""

    __tablename__ = "dreamers"

    # def __init__(self, user_id, name, email, password):
    #     """Create new user via id, name, email, password"""

    #     self.user_id = user_id
    #     self.name = name
    #     self.email = email
    #     self.password = password

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(20), nullable=False)


    def __repr__(self):
        """Provide info on user"""

        return f"User: {self.user_id} email: {self.email}"

class Goals(db.Model):
    """Goals user adds to their profile in database"""

    __tablename__ = "goals"

    # def __init__(self, goal_id, goal_info):
    #     """ User can create new goal"""

    #     self.goal_id = goal_id
    #     self.goal_info = goal_info

    goal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    goal_info = db.Column(db.String(250), nullable=False)

    #connecting goal to user id
    user_id = db.Column(db.Integer, db.ForeignKey('dreamers.user_id'))


    def __repr__(self):
        """Provide info on goal"""

        return f"Goal: {self.goal_id} goal info: {self.goal_info}"


def connect_to_db(app, db_uri="postgresql:///user_goals"):
    """ Connect database to Flask app."""

    # Configure to use my PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # if I run this module interactively, it will leave
    # me in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")