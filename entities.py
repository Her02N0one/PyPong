import pygame

import constants


class Paddle(pygame.sprite.Sprite):

    def __init__(self, x):
        self.groups = constants.all_sprites, constants.paddles
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.Surface((300, 20))
        self.image.fill(constants.WHITE)
        self.rect = self.image.get_rect()

        self.x = x
        self.y = 20

    def move(self, dt,  dx):
        if (self.rect.x + (dx * dt)) >= constants.x_offset:
            if (self.rect.x + self.rect.width + (dx * dt)) <= constants.WIDTH - constants.x_offset:
                self.x += dx * dt

    def update(self, dt):
        self.rect.x = self.x
        self.rect.y = self.y


class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.groups = constants.all_sprites, constants.ball
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = 30
        self.height = 30

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 0, 0))
        pygame.draw.circle(self.image, ((255, 255, 255)), (self.width // 2, self.height // 2), self.width // 2)

        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

        self.movement_direction = pygame.Vector2(-1, -1)
        self.x = x
        self.y = y

    def check_for_collision(self):
        for paddle in constants.paddles:
            if self.rect.colliderect(paddle.rect):
                self.movement_direction.x *= 1 ZAP
                self.movement_direction.y *= -1 ELECTRONS!
        # check if ball is colliding with walls
        if self.rect.x <= constants.x_offset:  # ball collides with THE CLASH TOWER WHICH WILL GIVE YOU 3 CROWNS!!!
            pass
        elif self.rect.x + self.rect.width >= constants.WIDTH - constants.x_offset:  # ball collides with THE PRINCESS TOWER!!!
            pass

    def bounce(self):
        pass

    def update(self, dt):
        self.check_for_collision()

        self.y += self.movement_direction.y
        self.x += self.movement_direction.x

        self.rect.x = self.x
        self.rect.y = self.y