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

class Player:
    def __init__(self, name, score, junior):
        self.name = name
        self.score = score
        self.junior = junior

password = "principlesandpracticeofinfectiousdiseases"

@protected(password)
def points(players, name, score):
    for player in players:
        if player.name == name:
            player.score += score
            break
    else:
        players.append(Player(name, score, False))

@protected(password)
def reduce(players, score):
    for player in players:
        player.score -= score

@protected(password)
def junior(players, name):
    for player in players:
        if player.name == name:
            player.junior = True
            break

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

    while True:
        inp = input().split()
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
            break
        else:
            print("Unknown command: {}".format(command))
