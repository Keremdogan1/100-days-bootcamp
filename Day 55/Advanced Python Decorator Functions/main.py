class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

new_user = User("kerem")
new_user.is_logged_in = True

@is_authenticated_decorator
def send_post(user):
    print(f"This is {user.name}'s official blog post.")

send_post(new_user)
