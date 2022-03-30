import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, game_settings, screen, ship, bullets):
    """nuppude peal hoidmise kontrollimine"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """nuppude pealt hoidmise kontrollimine"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(game_settings, screen, stats, play_button, ship, aliens, bullets):
    """hiire ja klaviatuuri kontollimine"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(game_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        game_settings.init_dynamic_settings()
        stats.game_active = True
        pygame.mouse.set_visible(False)
        aliens.empty()
        bullets.empty()
        create_fleet(game_settings, screen, ship, aliens)
        ship.ship_center()

def update_screen(game_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """ekraani uuendamine """
    # ekranni tausta muutmine
    screen.fill(game_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # laeva ekraanile asetamine
    ship.blitme()
    # tulnuka asetamien ekraanile
    aliens.draw(screen)
    # tulemustabeli asetamine
    sb.draw_score()
    # play nupu asetamine
    if not stats.game_active:
        play_button.draw_button()
    # viimase ekraani asetamine
    pygame.display.flip()

def update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets):
    """Kuulide asukoha muutmine ja kustutamine"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(game_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(game_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        stats.score += game_settings.alien_points
        sb.prepare_score()
    # kuulide kustutamine ja uue laevastiku tekitamine
    if len(aliens) == 0:
        bullets.empty()
        game_settings.increase_speed()
        create_fleet(game_settings, screen, ship, aliens)

def fire_bullet(game_settings, screen, ship, bullets):
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(game_settings, alien_width):
    """Arv tulnukaid rivis"""
    available_space_x = game_settings.screen_width - 1 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(game_settings, ship_height, alien_height):
    """arv reas defineerimine"""
    available_space_y = game_settings.screen_height - 2 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(game_settings, screen, aliens, alien_number, row_number):
    # tulnuka tegemine ja selle reasse panemine
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(game_settings, screen, ship, aliens):
    """Tulnuka laevastiku tegemine"""
    # tulnuka tegemine ja defineerimine mitu saab korraga reas olla
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)
    # esimese rea tegemine
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(game_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break

def change_fleet_direction(game_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1

def update_aliens(game_settings, stats, screen, ship, aliens, bullets):
    """tulnuka asukoha uuendamine"""
    check_fleet_edges(game_settings, aliens)
    aliens.update()
    # tulnuka ja laeva asukoha kontrollimine
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, stats, screen, ship, aliens, bullets)
    # tulnuka ekraani all vaatamine
    check_aliens_bottom(game_settings, stats, screen, ship, aliens, bullets)

def check_aliens_bottom(game_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(game_settings, stats, screen, ship, aliens, bullets)
            break

def ship_hit(game_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        # laevu üks jäänud
        stats.ships_left = stats.ships_left - 1
        # tulnuka ja gruppide arv on tühi
        aliens.empty()
        bullets.empty()
        # uue tulnuka laevastiku tegemine
        create_fleet(game_settings, screen, ship, aliens)
        # laeva keskele asetamine
        ship.ship_center()
        # pausile panemine
        sleep(2)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)




