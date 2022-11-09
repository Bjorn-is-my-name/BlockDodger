import pygame
from pathlib import Path
from pygame import mixer
import random
import time
import fileinput


def program():
    pygame.init()

    WORKING_DIR = Path(__file__).parent.absolute()
    IMAGE_ROOT = Path.joinpath(WORKING_DIR, 'used files', 'images')
    IMAGE_FOLDERS = {
        'other_images': Path.joinpath(IMAGE_ROOT, 'other images'),
        'player_square_images': Path.joinpath(IMAGE_ROOT, 'player square images'),
        'power_up_images': Path.joinpath(IMAGE_ROOT, 'power up images')
    }

    highscore_file_path = Path.joinpath(
        WORKING_DIR, 'used files', 'highscore.txt')
    pacman_font_path = Path.joinpath(WORKING_DIR, 'used files', 'pac-man.ttf')
    coins_file_path = Path.joinpath(WORKING_DIR, 'used files', 'coins.txt')
    shopitems_file_path = Path.joinpath(
        WORKING_DIR, 'used files', 'shop_items.txt')
    backgroundmusic_file_path = Path.joinpath(
        WORKING_DIR, 'used files', 'background_music.wav')

    def pygame_image(image_folder_type, image_name):
        return pygame.image.load(Path.joinpath(IMAGE_FOLDERS[image_folder_type], image_name))

    DISPLAY_WIDTH = 800
    DISPLAY_HEIGHT = 600

    FPS = 60

    black = (0, 0, 0)
    white = (255, 255, 255)
    lightgrey = (105, 105, 105)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    cyan = (0, 255, 255)
    violet = (255, 0, 255)

    screen = pygame.display.set_mode(
        (DISPLAY_WIDTH, DISPLAY_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption('Block Dodger')
    clock = pygame.time.Clock()

    background_image = pygame_image('other_images', 'background.png')
    game_name_image = pygame_image('other_images', 'game_name.png')

    player_square_image = pygame_image(
        'player_square_images', 'player_square.png')

    shielded_player_square_image = pygame_image(
        'player_square_images', 'shielded_player_square.png')
    double_shielded_square_player_image = pygame_image(
        'player_square_images', 'double_shielded_player_square.png')
    triple_shielded_player_square_image = pygame_image(
        'player_square_images', 'triple_shielded_player_square.png')
    quadruple_shielded_player_square_image = pygame_image(
        'player_square_images', 'quadruple_shielded_player_square.png')
    quintuple_shielded_player_square_image = pygame_image(
        'player_square_images', 'quintuple_shielded_player_square.png')

    slowed_player_square_image = pygame_image(
        'player_square_images', 'slowed_player_square.png')
    slowed_shielded_player_square_image = pygame_image(
        'player_square_images', 'slowed_shielded_player_square.png')
    slowed_double_shielded_player_square_image = pygame_image('player_square_images',
                                                              'slowed_double_shielded_player_square.png')
    slowed_triple_shielded_player_square_image = pygame_image('player_square_images',
                                                              'triple_shielded_slowed_player_square.png')
    slowed_quadruple_shielded_player_square_image = pygame_image('player_square_images',
                                                                 'quadruple_shielded_slowed_player_square.png')
    slowed_quintuple_shielded_player_square_image = pygame_image('player_square_images',
                                                                 'quintuple_shielded_slowed_player_square.png')

    speedup_player_square_image = pygame_image(
        'player_square_images', 'speedup_player_square.png')
    speedup_shielded_player_square_image = pygame_image(
        'player_square_images', 'speedup_shielded_player_square.png')
    speedup_double_shielded_player_square_image = pygame_image('player_square_images',
                                                               'speedup_double_shielded_player_square.png')
    speedup_triple_shielded_player_square_image = pygame_image('player_square_images',
                                                               'triple_shielded_speedup_player_square.png')
    speedup_quadruple_shielded_player_square_image = pygame_image('player_square_images',
                                                                  'quadruple_shielded_speedup_player_square.png')
    speedup_quintuple_shielded_player_square_image = pygame_image('player_square_images',
                                                                  'quintuple_shielded_speedup_player_square.png')

    player_square_size = 60

    start_button = pygame_image('other_images', 'start_button.png')
    start_button_x_size = 300
    start_button_y_size = 128

    quit_button = pygame_image('other_images', 'quit_button.png')
    quit_button_x_size = 300
    quit_button_y_size = 128

    pause_game_image = pygame_image('other_images', 'pause.png')
    pause_game_image_x_size = 200
    pause_game_image_y_size = 50

    sound_on_image = pygame_image('other_images', 'sound_on.png')
    sound_off_image = pygame_image('other_images', 'sound_off.png')
    sound_image_x_size = 62
    sound_image_y_size = 48

    controls_button_image = pygame_image('other_images', 'controls_button.png')
    controls_button_image_x_size = 132
    controls_button_image_y_size = 20

    controls_list = ['Left = Move Left',
                     'Right = Move Right',
                     'Space = Start',
                     'Escape = Back/Quit',
                     'P = Pause/Unpause',
                     'C = Controls',
                     'S = Sound on/off',
                     'O = Objects',
                     'V = Shop',
                     'H = Toggle Hard Mode',
                     'N = Toggle AI']

    back_button_image = pygame_image('other_images', 'back_button.png')
    back_button_image_size = 50

    objects_button_image = pygame_image('other_images', 'objects_button.png')
    objects_button_image_x_size = 125
    objects_button_image_y_size = 25

    objects_image = pygame_image('other_images', 'objects.png')
    objects_image_x_size = 600
    objects_image_y_size = 440

    shop_button_image = pygame_image('other_images', 'shop_button.png')
    shop_button_image_x_size = 120
    shop_button_image_y_size = 50

    ai_image = pygame_image('other_images', 'ai.png')

    lock_image = pygame_image('other_images', 'lock.png')

    checkmark_image = pygame_image('other_images', 'checkmark.png')

    death_sounds = [Path.joinpath(WORKING_DIR, 'used files', 'death sounds', 'your_trash_kid_death_sound.mp3'),
                    Path.joinpath(WORKING_DIR, 'used files',
                                  'death sounds', 'dogwater_death_sound.mp3'),
                    Path.joinpath(WORKING_DIR, 'used files',
                                  'death sounds', 'bruh_death_sound.mp3'),
                    Path.joinpath(
                        WORKING_DIR, 'used files', 'death sounds', 'fortnite_knocked_death_sound.mp3'),
                    Path.joinpath(WORKING_DIR, 'used files',
                                  'death sounds', 'roblox_death_sound.mp3'),
                    Path.joinpath(WORKING_DIR, 'used files',
                                  'death sound', 'byee.mp3'),
                    Path.joinpath(WORKING_DIR, 'used files',
                                  'death sound', 'bye-have-a-great-time.mp3'),
                    Path.joinpath(WORKING_DIR, 'used files', 'death sound',
                                  'they-ask-you-how-you-are-and-you-just-have-to-say-youre-fine.mp3'),
                    Path.joinpath(WORKING_DIR, 'used files', 'death sound', 'spongebob.mp3')]

    shield_image = pygame_image('power_up_images', 'shield.png')
    slowdown_movement_image = pygame_image(
        'power_up_images', 'slowdown_movement.png')
    speedup_movement_image = pygame_image(
        'power_up_images', 'speedup_movement.png')
    bomb_image = pygame_image('power_up_images', 'bomb.png')

    sound = True
    hard_mode_active = False
    player_ai_active = False

    KONAMI_CODE = [pygame.K_UP,
                   pygame.K_UP,
                   pygame.K_DOWN,
                   pygame.K_DOWN,
                   pygame.K_LEFT,
                   pygame.K_RIGHT,
                   pygame.K_LEFT,
                   pygame.K_RIGHT,
                   pygame.K_b,
                   pygame.K_a]

    def blocks_dodged(counter):
        font = pygame.font.Font(pacman_font_path, 50)
        text = font.render('Score: ' + str(counter), True, black)
        screen.blit(text, (0, 0))

    def objects_page(sound_state, hard_mode, player_ai):
        screen.fill(lightgrey)

        screen.blit(
            objects_button_image,
            (
                (DISPLAY_WIDTH / 2) - (controls_button_image_x_size / 2),
                50
            )
        )

        screen.blit(
            back_button_image,
            (
                (DISPLAY_WIDTH - 5 - back_button_image_size),
                (DISPLAY_HEIGHT - 5 - back_button_image_size)
            )
        )

        screen.blit(
            objects_image,
            (((DISPLAY_WIDTH / 2) - (objects_image_x_size / 2)),
             ((DISPLAY_HEIGHT / 2) - (objects_image_y_size / 2)))
        )

        while 1:
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        startup_screen(sound_state, hard_mode, player_ai)

                if event.type == pygame.MOUSEBUTTONUP:
                    click_position = pygame.mouse.get_pos()
                    click_x = click_position[0]
                    click_y = click_position[1]

                    if (DISPLAY_WIDTH - 5 - back_button_image_size) < click_x < DISPLAY_WIDTH and \
                            (DISPLAY_HEIGHT - 5 - back_button_image_size) < click_y < DISPLAY_HEIGHT:
                        startup_screen(sound_state, hard_mode, player_ai)

    def controls(sound_state, hard_mode, player_ai):
        screen.fill(lightgrey)

        screen.blit(
            controls_button_image,
            (
                (DISPLAY_WIDTH / 2) - (controls_button_image_x_size / 2),
                50
            )
        )

        screen.blit(
            back_button_image,
            (
                (DISPLAY_WIDTH - 5 - back_button_image_size),
                (DISPLAY_HEIGHT - 5 - back_button_image_size)
            )
        )

        amount_of_controls = 0

        for _ in controls_list:
            amount_of_controls += 1

        loop_counter = 1

        for control in controls_list:
            controls_text = pygame.font.Font(
                pacman_font_path,
                100
            )

            TextSurf, TextRect = text_object(
                control,
                controls_text
            )

            TextRect = (
                200,
                (75 + ((400 / amount_of_controls) * loop_counter))
            )

            screen.blit(
                TextSurf,
                TextRect
            )

            loop_counter += 1

        while 1:
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        startup_screen(sound_state, hard_mode, player_ai)

                if event.type == pygame.MOUSEBUTTONUP:
                    click_position = pygame.mouse.get_pos()
                    click_x = click_position[0]
                    click_y = click_position[1]

                    if (DISPLAY_WIDTH - 5 - back_button_image_size) < click_x < DISPLAY_WIDTH and \
                            (DISPLAY_HEIGHT - 5 - back_button_image_size) < click_y < DISPLAY_HEIGHT:
                        startup_screen(sound_state, hard_mode, player_ai)

    def pause_menu(paused, sound_state):
        global updated_sound_state

        updated_sound_state = sound_state

        mixer.music.pause()

        screen.fill(
            lightgrey,
            (
                0,
                (DISPLAY_HEIGHT - 5 - sound_image_y_size),
                (sound_image_x_size + 5),
                DISPLAY_HEIGHT
            )
        )

        screen.blit(
            pause_game_image,
            (
                ((DISPLAY_WIDTH / 2) - (pause_game_image_x_size / 2)),
                50
            )
        )

        screen.blit(
            back_button_image,
            (
                (DISPLAY_WIDTH - 5 - back_button_image_size),
                (DISPLAY_HEIGHT - 5 - back_button_image_size)
            )
        )

        amount_of_controls = 0

        for _ in controls_list:
            amount_of_controls += 1

        loop_counter = 1

        for control in controls_list:
            controls_text = pygame.font.Font(
                pacman_font_path,
                100
            )

            TextSurf, TextRect = text_object(
                control,
                controls_text
            )

            TextRect = (
                200,
                (75 + ((400 / amount_of_controls) * loop_counter))
            )

            screen.blit(
                TextSurf,
                TextRect
            )

            loop_counter += 1

        if sound_state:
            screen.blit(
                sound_on_image,
                (
                    5,
                    (DISPLAY_HEIGHT - sound_image_y_size)
                )
            )

        if not sound_state:
            screen.blit(
                sound_off_image,
                (
                    5,
                    (DISPLAY_HEIGHT - sound_image_y_size)
                )
            )

        while paused:
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_p:
                        paused = False

                    if event.key == pygame.K_s:
                        updated_sound_state = not sound_state
                        paused = False
                        pause_menu(
                            paused=True, sound_state=updated_sound_state)

                    if event.key == pygame.K_ESCAPE:
                        paused = False

                if event.type == pygame.MOUSEBUTTONUP:
                    click_position = pygame.mouse.get_pos()
                    click_x = click_position[0]
                    click_y = click_position[1]

                    if (DISPLAY_WIDTH - 5 - back_button_image_size) < click_x < DISPLAY_WIDTH and \
                            (DISPLAY_HEIGHT - 5 - back_button_image_size) < click_y < DISPLAY_HEIGHT:
                        paused = False

                    if 5 < click_x < (5 + sound_image_x_size) and \
                            (DISPLAY_HEIGHT - sound_image_y_size) < click_y < DISPLAY_HEIGHT:
                        updated_sound_state = not sound_state
                        paused = False
                        pause_menu(
                            paused=True, sound_state=updated_sound_state)

        return sound_state

    def startup_screen(sound_state, hard_mode, player_ai):
        KONAMI_CODE_ACTIVE = False

        screen.blit(
            background_image,
            (
                0,
                0
            )
        )

        screen.blit(
            game_name_image,
            (
                100,
                100
            )
        )

        screen.blit(
            controls_button_image,
            (
                (DISPLAY_WIDTH - 5 - controls_button_image_x_size),
                (DISPLAY_HEIGHT - 5 - controls_button_image_y_size)
            )
        )

        screen.blit(
            objects_button_image,
            (
                (DISPLAY_WIDTH - 5 - objects_button_image_x_size),
                (DISPLAY_HEIGHT - 15 - controls_button_image_y_size -
                 objects_button_image_y_size)
            )
        )

        screen.blit(
            shop_button_image,
            (
                (DISPLAY_WIDTH - 5 - shop_button_image_x_size),
                (
                    DISPLAY_HEIGHT - 25 - controls_button_image_y_size - objects_button_image_y_size - shop_button_image_y_size)
            )
        )

        highscore_file = open(
            highscore_file_path,
            'r'
        )

        highscore = highscore_file.read()
        highscore_file.close()

        highscore_text = pygame.font.Font(
            pacman_font_path,
            60
        )

        TextSurf, TextRect = text_object(
            f'Highscore: {highscore}',
            highscore_text
        )

        TextRect.center = (
            (DISPLAY_WIDTH / 2),
            (DISPLAY_HEIGHT / 2.8)
        )

        screen.blit(
            TextSurf,
            TextRect
        )

        coins_file = open(
            coins_file_path,
            'r'
        )

        coins = coins_file.read()
        coins_file.close()

        coins_text = pygame.font.Font(
            pacman_font_path,
            60
        )

        TextSurf, TextRect = text_object(
            f'Coins: {coins}',
            coins_text
        )

        TextRect = (
            5,
            5
        )

        screen.blit(
            TextSurf,
            TextRect
        )

        pygame.display.update()
        option_menu(sound_state, KONAMI_CODE_ACTIVE, hard_mode, player_ai)

    def objects(thingX, thingY, thingW, thingH, color):
        pygame.draw.rect(
            screen,
            color,
            [
                thingX,
                thingY,
                thingW,
                thingH
            ]
        )

    def player(x, y, shield_amount, slowdown_movement, speedup_movement):
        if slowdown_movement:
            if shield_amount == 0:
                screen.blit(slowed_player_square_image, (x, y))
            if shield_amount == 1:
                screen.blit(slowed_shielded_player_square_image, (x, y))
            if shield_amount == 2:
                screen.blit(slowed_double_shielded_player_square_image, (x, y))
            if shield_amount == 3:
                screen.blit(slowed_triple_shielded_player_square_image, (x, y))
            if shield_amount == 4:
                screen.blit(
                    slowed_quadruple_shielded_player_square_image, (x, y))
            if shield_amount == 5:
                screen.blit(
                    slowed_quintuple_shielded_player_square_image, (x, y))

        elif speedup_movement:
            if shield_amount == 0:
                screen.blit(speedup_player_square_image, (x, y))
            if shield_amount == 1:
                screen.blit(speedup_shielded_player_square_image, (x, y))
            if shield_amount == 2:
                screen.blit(
                    speedup_double_shielded_player_square_image, (x, y))
            if shield_amount == 3:
                screen.blit(
                    speedup_triple_shielded_player_square_image, (x, y))
            if shield_amount == 4:
                screen.blit(
                    speedup_quadruple_shielded_player_square_image, (x, y))
            if shield_amount == 5:
                screen.blit(
                    speedup_quintuple_shielded_player_square_image, (x, y))

        else:
            if shield_amount == 0:
                screen.blit(player_square_image, (x, y))
            if shield_amount == 1:
                screen.blit(shielded_player_square_image, (x, y))
            if shield_amount == 2:
                screen.blit(double_shielded_square_player_image, (x, y))
            if shield_amount == 3:
                screen.blit(triple_shielded_player_square_image, (x, y))
            if shield_amount == 4:
                screen.blit(quadruple_shielded_player_square_image, (x, y))
            if shield_amount == 5:
                screen.blit(quintuple_shielded_player_square_image, (x, y))

    def shop(sound_state, hard_mode, player_ai):
        screen.fill(lightgrey)

        screen.blit(
            shop_button_image,
            (
                ((DISPLAY_WIDTH / 2) - (shop_button_image_x_size / 2)),
                50
            )
        )

        screen.blit(
            back_button_image,
            (
                (DISPLAY_WIDTH - 5 - back_button_image_size),
                (DISPLAY_HEIGHT - 5 - back_button_image_size)
            )
        )

        coins_file = open(
            coins_file_path,
            'r'
        )

        coins = coins_file.read()
        coins_file.close()

        coins_text = pygame.font.Font(
            pacman_font_path,
            60
        )

        TextSurf, TextRect = text_object(
            f'Coins: {coins}',
            coins_text
        )

        TextRect = (
            5,
            5
        )

        screen.blit(
            TextSurf,
            TextRect
        )

        shop_items_file = open(
            shopitems_file_path,
            'r'
        )

        shop_items_list = shop_items_file.read().splitlines()
        shop_items_file.close()
        one_extra_shield = int(
            ''.join(filter(str.isdigit, shop_items_list[0])))
        two_extra_shields = int(
            ''.join(filter(str.isdigit, shop_items_list[1])))
        triple_shield_max = int(
            ''.join(filter(str.isdigit, shop_items_list[2])))
        quadruple_shield_max = int(
            ''.join(filter(str.isdigit, shop_items_list[3])))
        quintuple_shield_max = int(
            ''.join(filter(str.isdigit, shop_items_list[4])))
        player_ai_shop_item = int(
            ''.join(filter(str.isdigit, shop_items_list[5])))

        screen.fill(green, (100, 350, 600, 50))

        pygame.draw.line(screen, black, (100, 200), (700, 200), 9)
        pygame.draw.line(screen, black, (100, 350), (700, 350), 9)
        pygame.draw.line(screen, black, (100, 400), (700, 400), 9)
        pygame.draw.line(screen, black, (100, 196), (100, 404), 9)
        pygame.draw.line(screen, black, (700, 196), (700, 404), 9)
        pygame.draw.line(screen, black, (250, 200), (250, 400), 9)
        pygame.draw.line(screen, black, (400, 200), (400, 400), 9)
        pygame.draw.line(screen, black, (550, 200), (550, 400), 9)

        if not one_extra_shield:
            buy_text = pygame.font.Font(pacman_font_path, 60)
            TextSurf, TextRect = text_object('5000', buy_text)
            TextRect.center = (175, 370)
            screen.blit(TextSurf, TextRect)
            # drawing what to sell
            screen.blit(shielded_player_square_image, (145, 215))
            one_extra_shield_text_list = ['Start with 1', 'extra shield']
            extra_y = 0
            # extra loop to  make text show below other text because pygame does not support \n (newline)
            for one_extra_shield_text in one_extra_shield_text_list:
                one_extra_shield_text_font = pygame.font.Font(
                    pacman_font_path, 60)
                TextSurf, TextRect = text_object(
                    one_extra_shield_text, one_extra_shield_text_font)
                TextRect.center = (175, (300 + extra_y))
                screen.blit(TextSurf, TextRect)
                extra_y = 20
        # same as before for each shop item
        if one_extra_shield and not two_extra_shields:
            buy_text = pygame.font.Font(pacman_font_path, 60)
            TextSurf, TextRect = text_object('15000', buy_text)
            TextRect.center = (175, 370)
            screen.blit(TextSurf, TextRect)
            screen.blit(double_shielded_square_player_image, (145, 215))
            one_extra_shield_text_list = ['Start with 2', 'extra shields']
            extra_y = 0
            for one_extra_shield_text in one_extra_shield_text_list:
                one_extra_shield_text_font = pygame.font.Font(
                    pacman_font_path, 55)
                TextSurf, TextRect = text_object(
                    one_extra_shield_text, one_extra_shield_text_font)
                TextRect.center = (175, (300 + extra_y))
                screen.blit(TextSurf, TextRect)
                extra_y = 20

        if one_extra_shield and two_extra_shields:
            screen.blit(checkmark_image, (155, 360))
            screen.blit(double_shielded_square_player_image, (145, 215))
            one_extra_shield_text_list = ['Start with 2', 'extra shields']
            extra_y = 0
            for one_extra_shield_text in one_extra_shield_text_list:
                one_extra_shield_text_font = pygame.font.Font(
                    pacman_font_path, 55)
                TextSurf, TextRect = text_object(
                    one_extra_shield_text, one_extra_shield_text_font)
                TextRect.center = (175, (300 + extra_y))
                screen.blit(TextSurf, TextRect)
                extra_y = 20

        if not triple_shield_max and not quadruple_shield_max and not quintuple_shield_max:
            buy_text = pygame.font.Font(pacman_font_path, 60)
            TextSurf, TextRect = text_object('5000', buy_text)
            TextRect.center = (325, 370)
            screen.blit(TextSurf, TextRect)
            screen.blit(shield_image, (300, 215))
            one_extra_shield_text_list = ['Shield limit', 'is 3']
            extra_y = 0
            for one_extra_shield_text in one_extra_shield_text_list:
                one_extra_shield_text_font = pygame.font.Font(
                    pacman_font_path, 60)
                TextSurf, TextRect = text_object(
                    one_extra_shield_text, one_extra_shield_text_font)
                TextRect.center = (325, (300 + extra_y))
                screen.blit(TextSurf, TextRect)
                extra_y = 20

        if triple_shield_max and not quadruple_shield_max and not quintuple_shield_max:
            buy_text = pygame.font.Font(pacman_font_path, 60)
            TextSurf, TextRect = text_object('15000', buy_text)
            TextRect.center = (325, 370)
            screen.blit(TextSurf, TextRect)
            screen.blit(shield_image, (300, 215))
            one_extra_shield_text_list = ['Shield limit', 'is 4']
            extra_y = 0
            for one_extra_shield_text in one_extra_shield_text_list:
                one_extra_shield_text_font = pygame.font.Font(
                    pacman_font_path, 60)
                TextSurf, TextRect = text_object(
                    one_extra_shield_text, one_extra_shield_text_font)
                TextRect.center = (325, (300 + extra_y))
                screen.blit(TextSurf, TextRect)
                extra_y = 20

        if triple_shield_max and quadruple_shield_max and not quintuple_shield_max:
            buy_text = pygame.font.Font(pacman_font_path, 60)
            TextSurf, TextRect = text_object('25000', buy_text)
            TextRect.center = (325, 370)
            screen.blit(TextSurf, TextRect)
            screen.blit(shield_image, (300, 215))
            one_extra_shield_text_list = ['Shield limit', 'is 5']
            extra_y = 0
            for one_extra_shield_text in one_extra_shield_text_list:
                one_extra_shield_text_font = pygame.font.Font(
                    pacman_font_path, 60)
                TextSurf, TextRect = text_object(
                    one_extra_shield_text, one_extra_shield_text_font)
                TextRect.center = (325, (300 + extra_y))
                screen.blit(TextSurf, TextRect)
                extra_y = 20

        if triple_shield_max and quadruple_shield_max and quintuple_shield_max:
            screen.blit(checkmark_image, (305, 360))
            screen.blit(shield_image, (300, 215))
            one_extra_shield_text_list = ['Shield limit', 'is 5']
            extra_y = 0
            for one_extra_shield_text in one_extra_shield_text_list:
                one_extra_shield_text_font = pygame.font.Font(
                    pacman_font_path, 60)
                TextSurf, TextRect = text_object(
                    one_extra_shield_text, one_extra_shield_text_font)
                TextRect.center = (325, (300 + extra_y))
                screen.blit(TextSurf, TextRect)
                extra_y = 20

        if not player_ai_shop_item:
            buy_text = pygame.font.Font(pacman_font_path, 60)
            TextSurf, TextRect = text_object('20000', buy_text)
            TextRect.center = (475, 370)
            screen.blit(TextSurf, TextRect)

            player_ai_text_font = pygame.font.Font(pacman_font_path, 60)
            TextSurf, TextRect = text_object("AI", player_ai_text_font)
            TextRect.center = (475, 300)
            screen.blit(TextSurf, TextRect)
            screen.blit(ai_image, (455, 225))

        if player_ai_shop_item:
            screen.blit(checkmark_image, (455, 360))
            player_ai_text_font = pygame.font.Font(pacman_font_path, 60)
            TextSurf, TextRect = text_object("AI", player_ai_text_font)
            TextRect.center = (475, 300)
            screen.blit(TextSurf, TextRect)
            screen.blit(ai_image, (455, 225))

        while 1:
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        startup_screen(sound_state, hard_mode, player_ai)
                if event.type == pygame.MOUSEBUTTONUP:
                    click_position = pygame.mouse.get_pos()
                    click_x = click_position[0]
                    click_y = click_position[1]

                    if (DISPLAY_WIDTH - 5 - back_button_image_size) < click_x < DISPLAY_WIDTH and \
                            (DISPLAY_HEIGHT - 5 - back_button_image_size) < click_y < DISPLAY_HEIGHT:
                        startup_screen(sound_state, hard_mode, player_ai)

                    if 100 < click_x < 250 and 350 < click_y < 400:

                        if one_extra_shield == 0:

                            if int(coins) >= 5000:

                                coins_file = open(coins_file_path, 'w')
                                coins_file.write(str(int(coins) - 5000))
                                coins_file.close()

                                with fileinput.FileInput(shopitems_file_path, inplace=True) as shop_file:
                                    for line in shop_file:
                                        print(line.replace(
                                            'one_extra_shield=0', 'one_extra_shield=1'), end='')

                                shop(sound_state, hard_mode, player_ai)

                        if one_extra_shield == 1 and two_extra_shields == 0:
                            if int(coins) >= 15000:
                                coins_file = open(coins_file_path, 'w')
                                coins_file.write(str(int(coins) - 15000))
                                coins_file.close()
                                with fileinput.FileInput(shopitems_file_path, inplace=True) as shop_file:
                                    for line in shop_file:
                                        print(line.replace(
                                            'two_extra_shields=0', 'two_extra_shields=1'), end='')

                                shop(sound_state, hard_mode, player_ai)
                    # coordinates for second shop slot
                    # if its clicked it does the same as shown above
                    if 250 < click_x < 400 and 350 < click_y < 400:
                        if triple_shield_max == 0:
                            if int(coins) >= 5000:
                                coins_file = open(coins_file_path, 'w')
                                coins_file.write(str(int(coins) - 5000))
                                coins_file.close()
                                with fileinput.FileInput(shopitems_file_path, inplace=True) as shop_file:
                                    for line in shop_file:
                                        print(line.replace(
                                            'triple_shield_max=0', 'triple_shield_max=1'), end='')

                                shop(sound_state, hard_mode, player_ai)

                        if triple_shield_max == 1 and quadruple_shield_max == 0:
                            if int(coins) >= 15000:
                                coins_file = open(coins_file_path, 'w')
                                coins_file.write(str(int(coins) - 15000))
                                coins_file.close()
                                with fileinput.FileInput(shopitems_file_path, inplace=True) as shop_file:
                                    for line in shop_file:
                                        print(line.replace(
                                            'quadruple_shield_max=0', 'quadruple_shield_max=1'), end='')

                                shop(sound_state, hard_mode, player_ai)

                        if triple_shield_max == 1 and quadruple_shield_max == 1 and quintuple_shield_max == 0:
                            if int(coins) >= 25000:
                                coins_file = open(coins_file_path, 'w')
                                coins_file.write(str(int(coins) - 25000))
                                coins_file.close()
                                with fileinput.FileInput(shopitems_file_path, inplace=True) as shop_file:
                                    for line in shop_file:
                                        print(line.replace(
                                            'quintuple_shield_max=0', 'quintuple_shield_max=1'), end='')

                                shop(sound_state, hard_mode, player_ai)

                    if 550 > click_x > 400 > click_y > 350:
                        if player_ai == 0:
                            if int(coins) >= 20000:
                                coins_file = open(coins_file_path, 'w')
                                coins_file.write(str(int(coins) - 20000))
                                coins_file.close()
                                with fileinput.FileInput(shopitems_file_path, inplace=True) as shop_file:
                                    for line in shop_file:
                                        print(line.replace(
                                            'ai=0', 'ai=1'), end='')

                                shop(sound_state, hard_mode, player_ai)

    # option menu

    def option_menu(sound_state, KONAMI_CODE_ACTIVE, hard_mode, player_ai):
        code = []
        index = 0

        shop_items_file = open(shopitems_file_path, 'r')
        shop_items_list = shop_items_file.read().splitlines()
        shop_items_file.close()
        player_ai_accessibly = int(
            ''.join(filter(str.isdigit, shop_items_list[5])))

        if not hard_mode:
            hard_mode_switch_color = red
        else:
            hard_mode_switch_color = green

        if not player_ai:
            ai_switch_color = red
        else:
            ai_switch_color = green

        game_over_text = pygame.font.Font(pacman_font_path, 80)
        TextSurf, TextRect = text_object('Hard mode', game_over_text)
        TextRect.center = (710, 15)
        screen.blit(TextSurf, TextRect)

        pygame.draw.rect(screen, hard_mode_switch_color, (700, 50, 20, 20), 0)
        for i in range(4):
            pygame.draw.rect(screen, black, (700 - i, 50 - i, 22, 22), 1)

        game_over_text = pygame.font.Font(pacman_font_path, 80)
        TextSurf, TextRect = text_object('AI', game_over_text)
        TextRect.center = (385, 15)
        screen.blit(TextSurf, TextRect)

        pygame.draw.rect(screen, ai_switch_color, (375, 50, 20, 20), 0)
        for i in range(4):
            pygame.draw.rect(screen, black, (375 - i, 50 - i, 22, 22), 1)

        if not player_ai_accessibly:
            screen.blit(lock_image, (375, 50))

        # draw images
        screen.blit(start_button, (50, 325))
        screen.blit(quit_button, (450, 325))

        if sound_state:
            screen.blit(sound_on_image,
                        (5, (DISPLAY_HEIGHT - sound_image_y_size)))
        if not sound_state:
            screen.blit(sound_off_image,
                        (5, (DISPLAY_HEIGHT - sound_image_y_size)))
        # while the options are loaded (True) check for key presses and mouse clicks
        while 1:
            pygame.display.update()

            key = pygame.key.get_pressed()
            # if key is space, load the game
            if key[pygame.K_SPACE]:
                game_loop(sound_state, KONAMI_CODE_ACTIVE,
                          hard_mode, player_ai)
            # if key is escape, quit the game
            if key[pygame.K_ESCAPE]:
                pygame.quit()
                quit()

            for event in pygame.event.get():
                # if X in top right corner gets clicked, quit the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == KONAMI_CODE[index]:
                        code.append(event.key)
                        index += 1
                        if code == KONAMI_CODE:
                            index = 0
                            KONAMI_CODE_ACTIVE = True
                    else:
                        code = []
                        index = 0

                if event.type == pygame.KEYUP:
                    # if s is pressed switch the sound state
                    if key[pygame.K_s]:
                        sound_state = not sound_state
                        startup_screen(sound_state, hard_mode, player_ai)
                    # if c is pressed go to controls page
                    if key[pygame.K_c]:
                        controls(sound_state, hard_mode, player_ai)
                    # if o is pressed go to objects page
                    if key[pygame.K_o]:
                        objects_page(sound_state, hard_mode, player_ai)
                    # if b is pressed go to shop page
                    if key[pygame.K_v]:
                        shop(sound_state, hard_mode, player_ai)
                    if key[pygame.K_h]:
                        hard_mode = not hard_mode
                        startup_screen(sound_state, hard_mode, player_ai)
                    if key[pygame.K_n]:
                        if player_ai_accessibly:
                            player_ai = not player_ai
                            startup_screen(sound_state, hard_mode, player_ai)

                # check for mouse clicks
                if event.type == pygame.MOUSEBUTTONUP:
                    # get click coordinates
                    click_position = pygame.mouse.get_pos()
                    click_x = click_position[0]
                    click_y = click_position[1]
                    # if coordinates are within an image go the that page
                    # controls
                    if (DISPLAY_WIDTH - 5 - controls_button_image_x_size) < click_x < DISPLAY_WIDTH and (
                            DISPLAY_HEIGHT - 5 - controls_button_image_y_size) < click_y < DISPLAY_HEIGHT:
                        controls(sound_state, hard_mode, player_ai)
                    # objects
                    if (DISPLAY_WIDTH - 5 - objects_button_image_x_size) < click_x < DISPLAY_WIDTH and (
                            DISPLAY_HEIGHT - 15 - controls_button_image_y_size - objects_button_image_y_size) < click_y < (
                            DISPLAY_HEIGHT - 15 - controls_button_image_y_size):
                        objects_page(sound_state, hard_mode, player_ai)
                    # shop
                    if (DISPLAY_WIDTH - 5 - shop_button_image_x_size) < click_x < DISPLAY_WIDTH and (
                            (
                                DISPLAY_HEIGHT - 25 - controls_button_image_y_size - objects_button_image_y_size - shop_button_image_y_size)
                            < click_y < (DISPLAY_HEIGHT - 25 - shop_button_image_y_size)):
                        shop(sound_state, hard_mode, player_ai)
                    # if sound switch is clicked, update image and reload page
                    if 5 < click_x < (5 + sound_image_x_size) and (
                            DISPLAY_HEIGHT - sound_image_y_size) < click_y < DISPLAY_HEIGHT:
                        if sound_state:
                            sound_state = False
                        elif not sound_state:
                            sound_state = True
                        startup_screen(sound_state, hard_mode, player_ai)
                    # start game
                    if 50 < click_x < (50 + start_button_x_size) and 325 < click_y < (325 + start_button_y_size):
                        game_loop(sound_state, KONAMI_CODE_ACTIVE,
                                  hard_mode, player_ai)
                    # quit game
                    if 450 < click_x < (450 + quit_button_x_size) and 325 < click_y < (325 + quit_button_y_size):
                        pygame.quit()
                        quit()

                    if 700 < click_x < 720 and 50 < click_y < 70:
                        hard_mode = not hard_mode
                        startup_screen(sound_state, hard_mode, player_ai)

                    if player_ai_accessibly:
                        if 375 < click_x < 395 and 50 < click_y < 70:
                            if player_ai_accessibly:
                                player_ai = not player_ai
                                startup_screen(
                                    sound_state, hard_mode, player_ai)

    # render text in given font

    def text_object(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    # animation if the highscore has been broken

    def highscore_animation(score, highscore):
        new_points = score - highscore + 1
        # the more points that have to be added to the old highscore the faster it adds them up
        for point in range(new_points):
            new_highscore = highscore + point

            if point <= 20:
                sleep_timer = 0.07
            elif point <= 100:
                sleep_timer = 0.03
            elif point <= 250:
                sleep_timer = 0.006
            elif point <= 400:
                sleep_timer = 0.001
            elif point <= 750:
                sleep_timer = 0.0002
            else:
                sleep_timer = 0
            # display the highscore
            highscore_text = pygame.font.Font(pacman_font_path, 90)
            TextSurf, TextRect = text_object(
                f'New Highscore: {new_highscore}', highscore_text)
            TextRect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))

            screen.fill(
                lightgrey, (0, ((DISPLAY_HEIGHT / 2) - 15), DISPLAY_WIDTH, 40))
            screen.blit(TextSurf, TextRect)

            time.sleep(sleep_timer)
            pygame.display.update()

        time.sleep(1)
        return

    # message display on crash

    def message_display(text, sound_state, score, highscore, KONAMI_CODE_ACTIVE, hard_mode, player_ai):
        game_over_text = pygame.font.Font(pacman_font_path, 120)
        TextSurf, TextRect = text_object(text, game_over_text)
        TextRect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 4))
        screen.blit(TextSurf, TextRect)

        if KONAMI_CODE_ACTIVE:
            screen.blit(pygame.transform.rotate(screen, 180), (0, 0))
            pygame.display.flip()

        pygame.display.update()
        # if score is higher then highscore, trigger the highscore animation
        if score > highscore:
            highscore_animation(score, highscore)
        # while the death sound is still playing, wait
        while mixer.music.get_busy():
            pass
        # if sound is off, wait 1 second before going back the startup screen
        if not sound_state:
            time.sleep(1)

        startup_screen(sound_state, hard_mode, player_ai)

    # what to do on crash

    def crash(sound_state, score, KONAMI_CODE_ACTIVE, hard_mode, player_ai):
        # get current highscore and check if new highscore has been reached
        highscore_file = open(highscore_file_path, 'r')
        highscore = int(highscore_file.read())
        highscore_file.close()

        if score > highscore:
            highscore_file = open(highscore_file_path, 'w')
            highscore_file.write(str(score))
            highscore_file.close()
        # add score to coins (1 score = 1 coin)
        coins_file = open(coins_file_path, 'r')
        coins = int(coins_file.read())
        coins_file.close()
        coins = coins + score
        coins_file = open(coins_file_path, 'w')
        coins_file.write(str(coins))
        coins_file.close()
        # if sound is on, stop the background music and play a random death sound
        if sound_state:
            mixer.music.stop()
            random_death_sound = random.randint(0, 4)
            mixer.music.load(death_sounds[random_death_sound])
            mixer.music.play()

        message_display('GAME OVER!', sound_state, score,
                        highscore, KONAMI_CODE_ACTIVE, hard_mode, player_ai)

    def ai(player_x, all_object_info, slow, speed):
        x_change = 0
        all_object_x = [0, DISPLAY_WIDTH]
        possible_gaps = []
        left_obj_gap_width = 0

        for object in all_object_info:
            all_object_x.append(all_object_info[object]["x"])
            all_object_x.sort()

        if len(all_object_x) == 8:
            j = 0

            for i in range(7):
                pixel_difference = all_object_x[i + 1] - all_object_x[i]

                if all_object_x[i] == 0:
                    left_obj_gap_width = 0
                elif all_object_x[i] == all_object_info["red"]["x"]:
                    left_obj_gap_width = all_object_info["red"]["width"]
                elif all_object_x[i] == all_object_info["blue"]["x"]:
                    left_obj_gap_width = all_object_info["blue"]["width"]
                elif all_object_x[i] == all_object_info["green"]["x"]:
                    left_obj_gap_width = all_object_info["green"]["width"]
                elif all_object_x[i] == all_object_info["yellow"]["x"]:
                    left_obj_gap_width = all_object_info["yellow"]["width"]
                elif all_object_x[i] == all_object_info["violet"]["x"]:
                    left_obj_gap_width = all_object_info["violet"]["width"]
                elif all_object_x[i] == all_object_info["cyan"]["x"]:
                    left_obj_gap_width = all_object_info["cyan"]["width"]

                if (pixel_difference - left_obj_gap_width - 10) > 70:
                    possible_gaps.append(j)
                    j += 1
                else:
                    j += 1

        def closest_gap_function(list_value): return abs(list_value - player_x)
        closest_gap = min(possible_gaps, key=closest_gap_function)

        if (all_object_x[closest_gap] + left_obj_gap_width + 2) < player_x and all_object_x[closest_gap + 1] > (
                player_x + 62):
            x_change = 0

        elif (all_object_x[closest_gap - 1] + left_obj_gap_width + 2) < player_x and all_object_x[closest_gap] > (
                player_x + 62):
            x_change = 0

        elif player_x < (all_object_x[closest_gap] + left_obj_gap_width + 2) and (
                player_x + 62) < all_object_x[closest_gap + 1]:
            if slow:
                x_change = 3
            elif speed:
                x_change = 8
            else:
                x_change = 6

        elif player_x > (all_object_x[closest_gap] + left_obj_gap_width + 2) and (
                player_x + 62) > all_object_x[closest_gap + 1]:
            if slow:
                x_change = -3
            elif speed:
                x_change = -8
            else:
                x_change = -6

        if player_x <= 0 and x_change == -6 or x_change == -3 or x_change == -8:
            x_change = 0

        if player_x >= (DISPLAY_WIDTH - player_square_size) and x_change == 6 or x_change == 3 or x_change == 8:
            x_change = 0

        return x_change

    # main game loop

    def game_loop(sound_state, KONAMI_CODE_ACTIVE, hard_mode, player_ai):
        # if sound is on, load in background music
        if sound_state:
            mixer.music.load(backgroundmusic_file_path)
            mixer.music.play(-1)

        # player starting position
        x = int(((DISPLAY_WIDTH / 2) - (player_square_size / 2)))
        y = int((DISPLAY_HEIGHT - player_square_size))

        x_change = 0
        # check if things have been bought in the shop
        shop_items_file = open(shopitems_file_path, 'r')
        shop_items_list = shop_items_file.read().splitlines()
        shop_items_file.close()
        one_extra_shield = int(
            ''.join(filter(str.isdigit, shop_items_list[0])))
        two_extra_shields = int(
            ''.join(filter(str.isdigit, shop_items_list[1])))
        triple_shield_max = int(
            ''.join(filter(str.isdigit, shop_items_list[2])))
        quadruple_shield_max = int(
            ''.join(filter(str.isdigit, shop_items_list[3])))
        quintuple_shield_max = int(
            ''.join(filter(str.isdigit, shop_items_list[4])))

        # if shield has been bought, start with extra shield
        shield = 0
        if one_extra_shield == 1:
            shield = 1
            if two_extra_shields == 1:
                shield = 2
        # if shield cap increase has been bought, increase max shields that can stack
        max_shields = 2
        if triple_shield_max == 1:
            max_shields = 3
            if quadruple_shield_max == 1:
                max_shields = 4
                if quintuple_shield_max == 1:
                    max_shields = 5

        speed_multiplier = 1

        if hard_mode:
            shield = 0
            max_shields = 0
            speed_multiplier = 1.35

        # slowdown and speedup is False by default
        slowdown_movement = False
        slowdown_movement_time = 500
        speedup_movement = False
        speedup_movement_time = 240
        # set score to 0
        score = 0
        # all the objects specs
        # width/height in pixels, random starting position and the speed in pixels per frame
        # so speed 6 is (speed times fps) 6 x 60 = 360 pixels per second
        shield_width = 50
        shield_height = 48
        shield_startX = random.randrange(0, (DISPLAY_WIDTH - shield_width))
        shield_startY = -500
        shield_speed = 6 * speed_multiplier

        slowdown_movement_width = 40
        slowdown_movement_height = 39
        slowdown_movement_startX = random.randrange(
            0, (DISPLAY_WIDTH - slowdown_movement_width))
        slowdown_movement_startY = -500
        slowdown_movement_speed = 13 * speed_multiplier

        speedup_movement_width = 40
        speedup_movement_height = 39
        speedup_movement_startX = random.randrange(
            0, (DISPLAY_WIDTH - speedup_movement_width))
        speedup_movement_startY = -500
        speedup_movement_speed = 7 * speed_multiplier

        bomb_width = 50
        bomb_height = 60
        bomb_startX = random.randrange(0, (DISPLAY_WIDTH - bomb_width))
        bomb_startY = -500
        bomb_speed = 5 * speed_multiplier

        red_object_width = 50
        red_object_height = 50
        red_object_startX = random.randrange(
            0, (DISPLAY_WIDTH - red_object_width))
        red_object_startY = -500
        red_object_speed = 7 * speed_multiplier

        blue_object_width = 20
        blue_object_height = 50
        blue_object_startX = random.randrange(
            0, (DISPLAY_WIDTH - blue_object_width))
        blue_object_startY = -500
        blue_object_speed = 10 * speed_multiplier

        green_object_width = 150
        green_object_height = 50
        green_object_startX = random.randrange(
            0, (DISPLAY_WIDTH - green_object_width))
        green_object_startY = -500
        green_object_speed = 4 * speed_multiplier

        yellow_object_width = 10
        yellow_object_height = 300
        yellow_object_startX = random.randrange(
            0, (DISPLAY_WIDTH - yellow_object_width))
        yellow_object_startY = -500
        yellow_object_speed = 5 * speed_multiplier

        violet_object_width = 75
        violet_object_height = 75
        violet_object_startX = random.randrange(
            0, (DISPLAY_WIDTH - violet_object_width))
        violet_object_startY = -500
        violet_object_speed = 6 * speed_multiplier

        cyan_object_width = 200
        cyan_object_height = 10
        cyan_object_startX = random.randrange(
            0, (DISPLAY_WIDTH - cyan_object_width))
        cyan_object_startY = -500
        cyan_object_speed = 3 * speed_multiplier

        exit_game = False
        # while playing the game (True) check for key presses and mouse clicks
        while not exit_game:
            red_info = {"x": red_object_startX,
                        "y": red_object_startY,
                        "width": red_object_width,
                        "object_speed": red_object_speed}

            blue_info = {"x": 0,
                         "y": 0,
                         "width": blue_object_width,
                         "object_speed": blue_object_speed}
            if score >= 100:
                blue_info = {"x": blue_object_startX,
                             "y": blue_object_startY,
                             "width": blue_object_width,
                             "object_speed": blue_object_speed}

            green_info = {"x": 0,
                          "y": 0,
                          "width": green_object_width,
                          "object_speed": green_object_speed}
            if score >= 10:
                green_info = {"x": green_object_startX,
                              "y": green_object_startY,
                              "width": green_object_width,
                              "object_speed": green_object_speed}

            yellow_info = {"x": 0,
                           "y": 0,
                           "width": yellow_object_width,
                           "object_speed": yellow_object_speed}
            if score >= 500:
                yellow_info = {"x": yellow_object_startX,
                               "y": yellow_object_startY,
                               "width": yellow_object_width,
                               "object_speed": yellow_object_speed}

            violet_info = {"x": 0,
                           "y": 0,
                           "width": violet_object_width,
                           "object_speed": violet_object_speed}
            if score >= 30:
                violet_info = {"x": violet_object_startX,
                               "y": violet_object_startY,
                               "width": violet_object_width,
                               "object_speed": violet_object_speed}

            cyan_info = {"x": 0,
                         "y": 0,
                         "width": cyan_object_width,
                         "object_speed": cyan_object_speed}
            if score >= 1000:
                cyan_info = {"x": cyan_object_startX,
                             "y": cyan_object_startY,
                             "width": cyan_object_width,
                             "object_speed": cyan_object_speed}

            all_object_info = {"red": red_info,
                               "blue": blue_info,
                               "green": green_info,
                               "yellow": yellow_info,
                               "violet": violet_info,
                               "cyan": cyan_info}

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        mixer.music.unload()
                        startup_screen(sound_state, hard_mode, player_ai)

                    if event.key == pygame.K_p:
                        paused = True
                        pause_menu(paused, sound_state)

                        if updated_sound_state:
                            sound_state = True
                            mixer.music.unpause()
                        elif not updated_sound_state:
                            sound_state = False
                            mixer.music.pause()

            # if slowdown has been picked up start a timer (slowdown is for 500/60 = 8,3 seconds)
            if slowdown_movement:

                if slowdown_movement_time == 0:
                    slowdown_movement_time = 500
                    slowdown_movement = False

                else:
                    slowdown_movement_time -= 1
            # if speedup has been picked up start timer (speedup is 240/60 = 4 seconds)
            if speedup_movement:

                if speedup_movement_time == 0:
                    speedup_movement_time = 500
                    speedup_movement = False

                else:
                    speedup_movement_time -= 1
            # check for movement and slowdown/speedup and set player movement speed
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                if slowdown_movement:
                    x_change = -3
                elif speedup_movement:
                    x_change = -8
                else:
                    x_change = -6

            if key[pygame.K_RIGHT]:
                if slowdown_movement:
                    x_change = 3
                elif speedup_movement:
                    x_change = 8
                else:
                    x_change = 6

            # if left and right is pressed it cancels out and the player stops moving
            if key[pygame.K_LEFT] and key[pygame.K_RIGHT] or not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
                x_change = 0
            # make player stop when hitting the edge of the screen
            if x <= 0:
                if x_change == -6 or x_change == -3 or x_change == -8:
                    x_change = 0

            if x >= (DISPLAY_WIDTH - player_square_size):
                if x_change == 6 or x_change == 3 or x_change == 8:
                    x_change = 0

            if player_ai:
                x_change = ai(x, all_object_info,
                              slowdown_movement, speedup_movement)

            x += x_change

            screen.fill(lightgrey)
            # draw the objects (power ups are images)
            objects(red_object_startX, red_object_startY,
                    red_object_width, red_object_height, red)
            red_object_startY += red_object_speed

            if score > 250 and not hard_mode:
                screen.blit(shield_image, (shield_startX, shield_startY))
                shield_startY += shield_speed

            if score > 400:
                screen.blit(slowdown_movement_image,
                            (slowdown_movement_startX, slowdown_movement_startY))
                slowdown_movement_startY += slowdown_movement_speed

            if score > 650 and not hard_mode:
                screen.blit(speedup_movement_image,
                            (speedup_movement_startX, speedup_movement_startY))
                speedup_movement_startY += speedup_movement_speed

            if score > 900:
                screen.blit(bomb_image, (bomb_startX, bomb_startY))
                bomb_startY += bomb_speed

            if score > 100:
                objects(blue_object_startX, blue_object_startY,
                        blue_object_width, blue_object_height, blue)
                blue_object_startY += blue_object_speed

            if score > 10:
                objects(green_object_startX, green_object_startY,
                        green_object_width, green_object_height, green)
                green_object_startY += green_object_speed

            if score > 500:
                objects(yellow_object_startX, yellow_object_startY,
                        yellow_object_width, yellow_object_height, yellow)
                yellow_object_startY += yellow_object_speed

            if score > 30:
                objects(violet_object_startX, violet_object_startY,
                        violet_object_width, violet_object_height, violet)
                violet_object_startY += violet_object_speed

            if score > 1000:
                objects(cyan_object_startX, cyan_object_startY,
                        cyan_object_width, cyan_object_height, cyan)
                cyan_object_startY += cyan_object_speed
            # check/update player state
            player(x, y, shield, slowdown_movement, speedup_movement)
            # update score
            blocks_dodged(score)
            # if objects are of the screen, make then reappear (the lower y, the longer before it is shown again)
            if score > 250 and not hard_mode:
                if shield_startY > DISPLAY_HEIGHT:
                    shield_startY = -8000
                    shield_startX = random.randrange(
                        0, (DISPLAY_WIDTH - shield_width))

            if score > 400:
                if slowdown_movement_startY > DISPLAY_HEIGHT:
                    slowdown_movement_startY = -3250
                    slowdown_movement_startX = random.randrange(
                        0, (DISPLAY_WIDTH - slowdown_movement_width))

            if score > 650 and not hard_mode:
                if speedup_movement_startY > DISPLAY_HEIGHT:
                    speedup_movement_startY = -6500
                    speedup_movement_startX = random.randrange(
                        0, (DISPLAY_WIDTH - speedup_movement_width))

            if score > 900:
                if bomb_startY > DISPLAY_HEIGHT:
                    bomb_startY = -12000
                    bomb_startX = random.randrange(
                        0, (DISPLAY_WIDTH - bomb_width))

            if red_object_startY > DISPLAY_HEIGHT:
                red_object_startY = (0 - red_object_height)
                red_object_startX = random.randrange(
                    0, (DISPLAY_WIDTH - red_object_width))
                score += 1
                while True:
                    for object in all_object_info:
                        if all_object_info[object]["x"] == red_object_startX:
                            red_object_startX += 1
                    break

            if score > 100:
                if blue_object_startY > DISPLAY_HEIGHT:
                    blue_object_startY = (0 - blue_object_height)
                    blue_object_startX = random.randrange(
                        0, (DISPLAY_WIDTH - blue_object_width))
                    score += 3
                    while True:
                        for object in all_object_info:
                            if all_object_info[object]["x"] == blue_object_startX:
                                blue_object_startX += 1
                        break

            if score > 10:
                if green_object_startY > DISPLAY_HEIGHT:
                    green_object_startY = (0 - green_object_height)
                    green_object_startX = random.randrange(
                        0, (DISPLAY_WIDTH - green_object_width))
                    score += 1
                    while True:
                        for object in all_object_info:
                            if all_object_info[object]["x"] == green_object_startX:
                                green_object_startX += 1
                        break

            if score > 500:
                if yellow_object_startY > DISPLAY_HEIGHT:
                    yellow_object_startY = (0 - yellow_object_height)
                    yellow_object_startX = random.randrange(
                        0, (DISPLAY_WIDTH - yellow_object_width))
                    score += 4
                    while True:
                        for object in all_object_info:
                            if all_object_info[object]["x"] == yellow_object_startX:
                                yellow_object_startX += 1
                        break

            if score > 30:
                if violet_object_startY > DISPLAY_HEIGHT:
                    violet_object_startY = (0 - violet_object_height)
                    violet_object_startX = random.randrange(
                        0, (DISPLAY_WIDTH - violet_object_width))
                    score += 2
                    while True:
                        for object in all_object_info:
                            if all_object_info[object]["x"] == violet_object_startX:
                                violet_object_startX += 1
                        break

            if score > 1000:
                if cyan_object_startY > DISPLAY_HEIGHT:
                    cyan_object_startY = (0 - cyan_object_height)
                    cyan_object_startX = random.randrange(
                        0, (DISPLAY_WIDTH - cyan_object_width))
                    score += 5
                    while True:
                        for object in all_object_info:
                            if all_object_info[object]["x"] == cyan_object_startX:
                                cyan_object_startX += 1
                        break

            # check for collision with objects, if object is a power up, give corresponding effect
            if y <= (shield_startY + shield_height):
                if shield_startX <= x <= (shield_startX + shield_width) \
                        or shield_startX <= (x + player_square_size) <= (shield_startX + shield_width) \
                        or x <= shield_startX and (shield_startX + shield_width) <= (x + player_square_size):

                    shield_startY += 1000
                    if shield < max_shields:
                        shield += 1

            if y <= (slowdown_movement_startY + slowdown_movement_height):
                if slowdown_movement_startX <= x <= (slowdown_movement_startX + slowdown_movement_width) \
                        or slowdown_movement_startX <= (x + player_square_size) <= (
                        slowdown_movement_startX + slowdown_movement_width) \
                        or x <= slowdown_movement_startX and (slowdown_movement_startX + slowdown_movement_width) <= (
                        x + player_square_size):
                    slowdown_movement_startY += 1000
                    slowdown_movement = True
                    speedup_movement = False

            if y <= (speedup_movement_startY + speedup_movement_height):
                if speedup_movement_startX <= x <= (speedup_movement_startX + speedup_movement_width) \
                        or speedup_movement_startX <= (x + player_square_size) <= (
                        speedup_movement_startX + speedup_movement_width) \
                        or x <= speedup_movement_startX and (speedup_movement_startX + speedup_movement_width) <= (
                        x + player_square_size):
                    speedup_movement_startY += 1000
                    speedup_movement = True
                    slowdown_movement = False

            if y <= (bomb_startY + bomb_height):
                if bomb_startX <= x <= (bomb_startX + bomb_width) \
                        or bomb_startX <= (x + player_square_size) <= (bomb_startX + bomb_width) \
                        or x <= bomb_startX and (bomb_startX + bomb_width) <= (x + player_square_size):
                    if shield >= 2:
                        shield -= 2
                    if shield < 2:
                        crash(sound_state, score, KONAMI_CODE_ACTIVE,
                              hard_mode, player_ai)

            if y <= (red_object_startY + red_object_height):
                if red_object_startX <= x <= (red_object_startX + red_object_width) \
                        or red_object_startX <= (x + player_square_size) <= (red_object_startX + red_object_width) \
                        or x <= red_object_startX and (red_object_startX + red_object_width) <= (x + player_square_size):

                    if shield == 0:
                        crash(sound_state, score, KONAMI_CODE_ACTIVE,
                              hard_mode, player_ai)
                    if shield > 0:
                        red_object_startY += 1000
                        shield -= 1

            if y < (blue_object_startY + blue_object_height):
                if blue_object_startX < x < (blue_object_startX + blue_object_width) \
                        or blue_object_startX < (x + player_square_size) < (blue_object_startX + blue_object_width) \
                        or x < blue_object_startX and (blue_object_startX + blue_object_width) < (x + player_square_size):

                    if shield == 0:
                        crash(sound_state, score, KONAMI_CODE_ACTIVE,
                              hard_mode, player_ai)
                    if shield > 0:
                        blue_object_startY += 1000
                        shield -= 1

            if y <= (green_object_startY + green_object_height):
                if green_object_startX <= x <= (green_object_startX + green_object_width) \
                        or green_object_startX <= (x + player_square_size) <= (green_object_startX + green_object_width):

                    if shield == 0:
                        crash(sound_state, score, KONAMI_CODE_ACTIVE,
                              hard_mode, player_ai)
                    if shield > 0:
                        green_object_startY += 1000
                        shield -= 1

            if y <= (yellow_object_startY + yellow_object_height):
                if yellow_object_startX <= x <= (yellow_object_startX + yellow_object_width) \
                        or yellow_object_startX <= (x + player_square_size) <= (yellow_object_startX + yellow_object_width) \
                        or x <= yellow_object_startX and (yellow_object_startX + yellow_object_width) <= (
                        x + player_square_size):

                    if shield == 0:
                        crash(sound_state, score, KONAMI_CODE_ACTIVE,
                              hard_mode, player_ai)
                    if shield > 0:
                        yellow_object_startY += 1000
                        shield -= 1

            if y <= (violet_object_startY + violet_object_height):
                if violet_object_startX <= x <= (violet_object_startX + violet_object_width) \
                        or violet_object_startX <= (x + player_square_size) <= (violet_object_startX + violet_object_width):

                    if shield == 0:
                        crash(sound_state, score, KONAMI_CODE_ACTIVE,
                              hard_mode, player_ai)
                    if shield > 0:
                        violet_object_startY += 1000
                        shield -= 1

            if y <= (cyan_object_startY + cyan_object_height):
                if cyan_object_startX <= x <= (cyan_object_startX + cyan_object_width) \
                        or cyan_object_startX <= (x + player_square_size) <= (cyan_object_startX + cyan_object_width):

                    if shield == 0:
                        crash(sound_state, score, KONAMI_CODE_ACTIVE,
                              hard_mode, player_ai)
                    if shield > 0:
                        cyan_object_startY += 1000
                        shield -= 1

            if KONAMI_CODE_ACTIVE:
                screen.blit(pygame.transform.rotate(screen, 180), (0, 0))
                pygame.display.flip()
            # update (show) it all to the screen
            pygame.display.update()
            clock.tick(FPS)

    startup_screen(sound, hard_mode_active, player_ai_active)


if __name__ == "__main__":
    program()

# quiting the code when quitting the game
pygame.quit()
quit()
