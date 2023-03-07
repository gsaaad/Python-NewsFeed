from flask import session, redirect
from functools import wraps


def login_required(func):
    # login required function that expects a function as argument
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        print('wrapper')
        # if logged in, call orgiginal function with original arguments
        if session.get('loggedIn') ==True:
            return func(*args, **kwargs)
        return redirect('/login')
    
    return wrapped_function




# ! login_required is a decorator funciton
# ! this calls login_required then callback
# @login_required
# def callback():
#   print('hello')

#! callback() # prints 'wrapper', then 'hello'


# !python decorator is similar to this!
# function login_required(func) {
#   function wrapped_function() {
#     console.log('wrapper');
#     // func(*args, **kwargs)
#     return func(...arguments);
#   }
#   return wrapped_function;
# }
# // @login_required
# // def callback():
# const callback = login_required(() => {
#   console.log('hello');
# });
# callback();