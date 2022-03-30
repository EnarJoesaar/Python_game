class Settings:
    """Klass kus hoitakse kõiki sätteid"""

    def __init__(self):
        """mängu sättete käivitamine"""
        # ekraani sätted
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (23, 86, 212)
        # laeva sätted
        self.ship_limit = 3
        # kuuli sätted
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 0, 0
        self.bullets_allowed = 10000
        # tulnuka sätted
        self.fleet_drop_speed = 5
        # mängu kiirendamise faktor
        self.speedup_scale = 1.1
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.3

        # laeva suund
        self.fleet_direction = 1

        # punktid
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale