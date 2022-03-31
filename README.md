# Python game
How do create a python scripted game yourself

## Getting started
 
### Prerequisites

You need software where you can create and run a python script

```
For example Thonny or PyCharm
```

### Installing

Before you start you also need the pygame script

that can be achieved in PyCharm by...

```
Open File > Settings > Project from the PyCharm menu.
Select your current project.
Click the Python Interpreter tab within your project tab.
Click the small + symbol to add a new library to the project.
```

You then need to start with something basic that defines the items you'd like the game to have like I have done....

```
def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Example Game")
    play_button = Button(game_settings, screen, "Play")
    stats = GameStats(game_settings)
    sb = Scoreboard(game_settings, screen, stats)

    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(game_settings, screen, ship, aliens)

```

So for an example I have defined the game settings, play button, stats, scoreboard, ship, bullets etc

And then created classes for them like for example scoreboard...

```
import pygame.font
class Scoreboard():
    def __init__(self, game_settings, screen, stats):
        """Init scoreboard atributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats
        # score atributes - size, color, font
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 46)
        # setting ready graphic score
        self.prepare_score()

    def prepare_score(self):
        """converting the score into graphic component"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20

    def draw_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)
```

Or for bullets...

```
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Kuuli klass"""
    def __init__(self, game_setting, screen, ship):
        """Bullet spawing place near the ship"""
        super().__init__()
        self.screen = screen
        # making the bullet
        self.rect = pygame.Rect(0, 0, game_setting.bullet_width, game_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # position of the bullet
        self.y = float(self.rect.y)
        # settings of bullets
        self.color = game_setting.bullet_color
        self.speed_factor = game_setting.bullet_speed_factor
    def update(self):
        """Updating bullets location"""
        self.y -= self.speed_factor
        self.rect.y = self.y
    def draw_bullet(self):
        """Making the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
```

##Notes to keep in mind
Don't forget to import your classes, it's really important if you want your game to run properly as an example...

```
from pygame.sprite import Group

from settings import Settings

from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

from ship import Ship
from alien import Alien
import game_functions as gf
```
## Authors

* **Enar Jõesaar** - *Github* [EnarJoesaar](https://github.com/EnarJoesaar)

## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/) - Used to create the game

## My creation

You can find and clone my game at...

* **https://github.com/EnarJoesaar/Python_game** 