from collections import namedtuple

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

def ranking(players):
    for player in sorted(players, key=lambda p: p.score, reverse=True):
        print("{:4}: {} ({})".format(
            player.score,
            player.name,
            "junior" if player.junior else "senior",
        ))

def ranking_junior(players):
    ranking(filter(lambda p: p.junior, players))

if __name__ == "__main__":
    players = []
