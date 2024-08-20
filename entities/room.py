# entities/room.py

import pygame

class Room:
    def __init__(self, game, room_type, position):
        self.game = game
        self.room_type = room_type
        self.position = pygame.Vector2(position)
        
        # Placeholder for room appearance
        self.image = pygame.Surface((60, 60))
        self.image.fill((0, 0, 255))  # Blue square for the room

    def update(self):
        # Logic for room function (e.g., resource generation, defense)
        pass

    def draw(self, screen):
        screen.blit(self.image, self.position)
