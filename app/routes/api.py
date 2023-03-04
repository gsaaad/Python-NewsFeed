from flask import Blueprint, request, jsonify, session
from app.models import User, Post, Comment, Vote
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
        # ADD user 
        db.add(newUser)
        # commit/save database changed
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
        print(sys.exe_info()[0])
        # if there was an error, rollback / cancel pending process
        db.rollback()
        return jsonify(message), 500
    
    # adding session of user login
    session.clear()
    session['user_id'] = newUser.id
    session['loggedIn'] = True
    
    
    # for front end, we want to return a more meaningful response. JSON format
    return jsonify(id=newUser.id)

@bp.route("/users/logout", methods =['POST'])
def logout():
    # remove session variables
    session.clear()
    return '', 204


@bp.route("/users/login", methods=['POST'])
def login():
    data = request.get_json()
    db = get_db()
    
    try:
        user = db.query(User).filter(User.email == data['email']).one()
        print("grabbed user",user)
        
        
    except:
        print(sys.exc_info()[0])
        
        return jsonify(message = 'Incorrect credentials'), 400
    if user.verify_password(data['password']) ==False:
            return jsonify(message = 'Incorrect credentials'), 400
    
    session.clear()
    session['user_id'] = user.id
    session['loggedIn'] = True
    
    return jsonify(id = user.id)

@bp.route('/comments', methods=['POST'])
def comment():
    data = request.get_json()
    db = get_db()
    
    try:
        # create a new comment
        newComment = Comment(
            comment_text = data['comment_text'],
            post_id = data['post_id'],
            user_id = session.get('user_id')
            
        )
        
        db.add(newComment)
        db.commit()
    except:
        print(sys.exc_info()[0])
        
        db.rollback()
        return jsonify(message = 'Comment failed'), 500
    
    return jsonify(id = newComment.id)