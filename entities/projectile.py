# entities/projectile.py

import pygame

class Projectile:
    def __init__(self, game, position, direction, speed, damage):
        self.game = game
        self.position = pygame.Vector2(position)
        self.direction = pygame.Vector2(direction).normalize()
        self.speed = speed
        self.damage = damage
        
        # Placeholder for projectile appearance
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 255, 0))  # Yellow projectile

    def update(self):
        # Move the projectile in its direction
        self.position += self.direction * self.speed
        
        # Check for collisions with enemies
        self.check_collisions()

    def check_collisions(self):
        # Example collision detection with enemies
        for enemy in self.game.wave_manager.enemies:
            if enemy.position.distance_to(self.position) < 10:  # Simple radius check
                enemy.health -= self.damage
                self.game.wave_manager.enemies.remove(enemy)
                break

    def draw(self, screen):
        screen.blit(self.image, self.position)
