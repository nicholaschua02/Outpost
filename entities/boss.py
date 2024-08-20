# entities/boss.py

from entities.enemy import Enemy

class Boss(Enemy):
    def __init__(self, game, position):
        super().__init__(game, position)
        self.health = 200  # Boss has more health than regular enemies
        self.speed = game.settings.enemy_speed / 2  # Boss moves slower but is more powerful

    def update(self):
        # Boss-specific update logic (e.g., special abilities)
        super().update()

    def special_attack(self):
        # Boss can perform a special attack, affecting rooms or robots
        pass
