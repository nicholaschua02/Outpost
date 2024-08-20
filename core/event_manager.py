# core/event_manager.py

from entities.boss import Boss

class EventManager:
    def __init__(self, game):
        self.game = game

    def update(self):
        # Handle boss waves every 5 waves
        if self.game.wave_manager.wave_number % 5 == 0 and not self.game.wave_manager.enemies:
            self.spawn_boss()

    def spawn_boss(self):
        # Spawn a boss enemy at a specific location
        boss = Boss(self.game, (100, 100))  # Placeholder spawn position
        self.game.wave_manager.enemies.append(boss)
