import sys


def protected(password):
    """Requests the user to input the password before running decorated function."""
    def decorator(f):
        def wrapper(*args, **kwargs):
            attempts = 3
            while attempts > 0:
                user_password = input("Password: ")
                if user_password == password:
                    break
                print("Invalid password.")
                attempts -= 1
            else:
                print("3 incorrect attempts.")
                return
            f(*args, **kwargs)
        return wrapper
    return decorator


class Player:
    """Stores name, score and junior attributes of a player."""
    def __init__(self, name, score, junior):
        self.name = name
        self.score = score
        self.junior = junior


password = "principlesandpracticeofinfectiousdiseases"


@protected(password)
def points(players, name, score):
    """Adds given score to the exising score of the player with given name or creates a new player."""
    for player in players:
        if player.name == name:
            player.score += score
            break
    else:
        players.append(Player(name, score, False))


# REVIEW: percentá na vstupe sú od 0 po 100, nie od 0 po 1
@protected(password)
def reduce(players, percent):
    """Reduces scores of all players by given percentage."""
    for player in players:
        player.score = int(player.score * (1 - percent))


@protected(password)
def junior(players, name):
    """Sets the player with given name as a junior."""
    for player in players:
        if player.name == name:
            player.junior = True
            break


def ranking(players):
    """Prints a nice table of all players sorted by their score."""
    for i, player in enumerate(sorted(players, key=lambda p: p.score, reverse=True)):
        print("{:2}. {:4}, {} ({})".format(
            i+1,
            player.score,
            player.name,
            "junior" if player.junior else "senior",
        ))


def ranking_junior(players):
    """Prints a nice table of all junior players sorted by their score."""
    ranking(filter(lambda p: p.junior, players))


@protected(password)
def quit():
    """Exits the program."""
    sys.exit(0)


if __name__ == "__main__":
    players = []
# REVIEW po spustení má pýtať heslo
    while True:
        inp = input("> ").split()
        command = inp[0]

        if command == "points":
            points(players, inp[1], int(inp[2]))
        elif command == "reduce":
            reduce(players, int(inp[1]))
        elif command == "junior":
            junior(players, inp[1])
        elif command == "ranking":
            if len(inp) > 1 and inp[1] == "junior":
                ranking_junior(players)
            else:
                ranking(players)
        elif command == "quit":
            quit()
        else:
            print("Unknown command: {}".format(command))
