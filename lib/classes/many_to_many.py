class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, "_title"):
            pass
        elif isinstance(new_title, str) and len(new_title) > 0:
            self._title = new_title

    def results(self):
        # game_results = []
        # for result in Result.all:
        #     if result.game == self:
        #         game_results.append(result)

        # return game_results
        return [result for result in Result.all if result.game == self]

    def players(self):
        game_players = []
        for result in self.results():
            if result.player not in game_players:
                game_players.append(result.player)
        return game_players

    def average_score(self, player):
        scores = [result.score for result in self.results() if result.player == player]
        return sum(scores) / len(scores)

    def __repr__(self) -> str:
        return f"<Game {self.title}>"

class Player:


    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2 <= len(new_username) <= 16:
            self._username = new_username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        player_games = []
        for result in self.results():
            if result.game not in player_games:
                player_games.append(result.game)
        return player_games

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        # count = 0
        # for result in self.results():
        #     if result.game == game:
        #         count += 1
        # return count
        return len([result for result in self.results() if result.game == game])

    def __repr__(self) -> str:
        return f"<Player {self.username}>"

class Result:
    
    all = []
    
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if hasattr(self, "_score"):
            pass
        elif isinstance(new_score, int) and 1 <= new_score <= 5000:
            self._score = new_score

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        if isinstance(new_player, Player):
            self._player = new_player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if isinstance(new_game, Game):
            self._game = new_game

    def __repr__(self) -> str:
        return f"<Result {self.player} - {self.game} - {self.score}>"