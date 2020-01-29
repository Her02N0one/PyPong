import pygame

from constants import *
import entities
import gui
import utils


class MainMenuState(utils.State):
    def __init__(self, state_data):
        super().__init__(state_data)
        self.buttons = dict()
        play_button_width = 550
        play_button_height = 200
        self.buttons["NEW_GAME"] = gui.Button(
            y=HEIGHT // 2 - play_button_height,
            x=WIDTH // 2 - (play_button_width // 2),
            width=play_button_width,
            height=play_button_height,
            font=large_font,
            text="START GAME",
            callback=(lambda: self.states.push(GameState(state_data))))
        # self.buttons["SETTINGS"] = gui.Button(
        #     y=190,
        #     text="Settings",
        #     callback=(lambda: self.states.push(SettingsState(state_data))))
        self.buttons["QUIT"] = gui.Button(
            y=430, text="Quit", callback=(lambda: self.end_state()))

    def on_enter(self):
        pass

    def on_leave(self):
        pass

    def update_input(self, dt):
        pass

    def update_events(self, dt, event):

        for key in self.buttons:
            self.buttons[key].update_events(dt, event)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        for key in self.buttons:
            self.buttons[key].update(dt)


    def render(self, target=None):

        if target is None:
            target = self.screen

        for key in self.buttons:
            self.buttons[key].render(target)


class GameState(utils.State):
    def __init__(self, state_data):
        super().__init__(state_data)
        self.player_paddle = entities.Paddle(20)
        self.ball = entities.Ball(WIDTH // 2, HEIGHT // 2)

    def on_enter(self):
        pass

    def on_leave(self):
        pass

    def update_events(self, dt, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.end_state()

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player_paddle.move(dt, -500)
        if keys[pygame.K_RIGHT]:
            self.player_paddle.move(dt, 500)

        all_sprites.update(dt)

    def render(self, target=None):
        if target is None:
            target = self.screen

        all_sprites.draw(target)


class SettingsState(utils.State):
    def __init__(self, state_data):
        super().__init__(state_data)
        self.buttons = dict()

        self.buttons["BACK"] = gui.Button(
            y=430, text="Back", callback=(lambda: self.end_state()))
        # self.slider = gui.Slider(initial_value=pygame.mixer.music.get_volume())

    def update_input(self, dt):
        pass

    def update_events(self, dt, event):

        for key in self.buttons:
            self.buttons[key].update_events(dt, event)

        # self.slider.update_events(dt, event)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        for key in self.buttons:
            self.buttons[key].update(dt)

        # self.slider.update(dt)
        # pygame.mixer.music.set_volume(self.slider.get_percent())

    def render(self, target=None):

        if target is None:
            target = self.screen

        for key in self.buttons:
            self.buttons[key].render(target)
        
        # self.slider.render(target)
