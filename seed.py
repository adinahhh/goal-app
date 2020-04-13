from sqlalchemy import func
from model import User, Goals

from model import connect_to_db, db
from server import app

# load users

# load goals 

# create new users
def create_new_user():
    """Add new user to dB"""
    
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute()
    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    create_new_user()