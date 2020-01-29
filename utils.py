import pygame

import constants


class StateStack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, state):
        if self.isEmpty() is not True:
            self.top().on_leave()
        self.items.append(state)
        self.top().on_enter()

    def pop(self):
        self.top().on_leave()
        self.items.pop()
        if self.isEmpty() is not True:
            self.top().on_enter()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()


class State:

    def __init__(self, state_data: dict):
        self.state_data = state_data
        self.screen = state_data["screen"]
        self.states = state_data["states"]

        self.mousePos = pygame.Vector2()
        self.quit = False
        self.target = None

    def get_quit(self):
        return self.quit

    def end_state(self):
        self.quit = True

    def on_enter(self):
        """
        Runs once every time the class enters top of the stack
        """
        pass

    def on_leave(self):
        """
        Runs once every time the class leaves top of the stack
        """
        pass

    def update_events(self, dt, event):
        assert 0, "update_input not implemented"

    def update_input(self, dt):
        assert 0, "update_input not implemented"

    def update(self, dt):
        assert 0, "update not implemented"

    def render(self, target=None):
        assert 0, "render not implemented"
