from flask import Blueprint, request, jsonify
from app.models import User
import sys
from app.db import get_db
import sqlalchemy

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/users', methods=['POST'])
def signup():
    data= request.get_json()
    db = get_db()
    
    # create a new user
    try:
        message = 'Successful Registration'
        newUser = User(
            username = data['username'],
            email = data['email'],
            password = data['password']
        )
        # save in database
        db.add(newUser)
        db.commit()
        print(message)
        
    except AssertionError:
        print("Validation error, check inputs and types")
    except sqlalchemy.exc.IntegrityError:
        print("There was an error with SQL database")
    except:
        # insert failed, so send error to front end
        message = 'Registration failed.. Try again later'
        print(message)
        db.rollback()
        return jsonify(message), 500
    print(newUser)
    print(sys.exe_info()[0])

    return jsonify(id=newUser.id)