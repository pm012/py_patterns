class Event(list):
    def __call__(self, *args, **kwds):
        for item in self:
            item(*args, **kwds)

class Game:
    def __init__(self):
        self.events = Event()

    def fire(self, args):
        self.events(args)

class GoalScoredInfo:
    def __init__(self, who_scored:Player, goals_scored:int):
        self.who_scored = who_scored
        self.goals_scored = goals_scored

class Player:
    def __init__(self, name:str, game: Game):
        self.name = name
        self.game = game
        self.goals_scored = 0

    def score(self):
        self.goals_scored += 1
        args = GoalScoredInfo(self.name, self.goals_scored)
        self.game.fire(args)

class Coach:
    def __init__(self, game: Game):
        game.events.append(self.celebrate_goal)

    def celebrate_goal(self, args):
        if isinstance(args, GoalScoredInfo) and args.goals_scored < 3:
            print(f'Coach says: well done, {args.who_scored}!')

if __name__ == "__main__":
    game = Game()
    player = Player('Sam', game)

    coach = Coach(game)

    player.score()
    player.score()

    