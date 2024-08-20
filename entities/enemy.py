# entities/enemy.py

import pygame

class Enemy:
    def __init__(self, game, position):
        self.game = game
        self.position = pygame.Vector2(position)
        self.speed = game.settings.enemy_speed

        # Placeholder for enemy appearance
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))  # Red square for the enemy

    def update(self):
        # Basic movement towards the outpost (example logic)
        target = self.game.rooms[0].position  # Target the central hub
        direction = (target - self.position).normalize()
        self.position += direction * self.speed

    def draw(self, screen):
        screen.blit(self.image, self.position)
