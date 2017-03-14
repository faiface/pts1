def protected(password):
    def decorator(f):
        def wrapper(*args, **kwargs):
            attempts = 3
            while attempts > 0:
                user_password = input("Password: ")
                if user_password == password:
                    break
                print("Invalid password.")
            else:
                print("3 incorrect attempts.")
                return
            f(*args, **kwargs)
        return decorator
