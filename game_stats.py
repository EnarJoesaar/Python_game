class GameStats():
    """Mängu statistikas"""
    def __init__(self, game_settings):
        """Mängu statistika laadimine"""
        self.game_settings = game_settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """Mängu statistika laadimine ja vahetumine mängus"""
        self.ships_left = self.game_settings.ship_limit
        self.score = 0