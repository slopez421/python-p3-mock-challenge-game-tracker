import ipdb
class Game:
    all = []
    def __init__(self, title):
        self.title = title
        Game.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        elif hasattr(self, "title"):
            return title
        else:
            raise ValueError("Title must be a str.") 

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        unique_players = []
        for result in Result.all:
            if (result.game == self) and (result.player not in unique_players):
                unique_players.append(result.player)
        return unique_players

    def average_score(self, player):
        scores = []
        for result in player.results():
            scores.append(result.score)
        return sum(scores)/len(scores)
            

class Player:
    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise ValueError("Username must be a str between 2 and 16 characters.")

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        unique_games = []
        for result in Result.all:
            if result.player == self and result.game not in unique_games:
                unique_games.append(result.game)
        return unique_games
    
    def played_game(self, game):
        if game in self.games_played():
            return True
        else:
            return False

    def num_times_played(self, game):
        count = 0

        for result in Result.all:
            if result.player == self and result.game == game:
                count +=1
        return count
        

class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    
    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise ValueError("player must be a type of Player")
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise ValueError("Game must be of the Game class.")
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if hasattr(self, "score"):
            return
        elif 0 < score <= 5002 and isinstance(score, int):
            self._score = score
        else: 
            raise ValueError("Score must be an int between 0 and 5000.")
