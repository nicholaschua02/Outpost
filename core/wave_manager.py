# core/wave_manager.py

import pygame
from entities.enemy import Enemy

class WaveManager:
    def __init__(self, game):
        self.game = game
        self.wave_number = 1
        self.enemies = []
        self.time_since_last_wave = 0

    def update(self):
        # Manage wave spawning
        self.time_since_last_wave += 1 / self.game.settings.fps
        if self.time_since_last_wave >= self.game.settings.time_between_waves:
            self.spawn_wave()
            self.time_since_last_wave = 0

        for enemy in self.enemies:
            enemy.update()

    def spawn_wave(self):
        # Spawn a new wave of enemies
        for _ in range(self.wave_number * 5):  # Example: Increase number of enemies per wave
            enemy = Enemy(self.game, (50, 50))  # Placeholder spawn position
            self.enemies.append(enemy)
        self.wave_number += 1
