class GameStates:
    """跟踪游戏信息"""

    def __init__(self, ai_game):
        self.game_active = False
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
