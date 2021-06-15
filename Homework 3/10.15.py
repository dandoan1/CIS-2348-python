# Dan Doan 1986920
# making the class
class Team:
    def init(self):
        self.teamname = 'none'
        self.team_wins = 0
        self.team_losses = 0

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)


# asking for input
if __name__ == "__main__":
    average = Team()
    name = input()
    wins = int(input())
    losses = int(input())
    average.teamname = name
    average.team_wins = wins
    average.team_losses = losses
    winrate = average.get_win_percentage()
    # after calculation if more win than losses, then congrats if not, no
    if winrate > .5:
        print("Congratulations, Team {} has a winning average!".format(name))
    else:
        print("Team {} has a losing average.".format(name))
