import random


class WanderingMonster:
    def __init__(self, x, y, monster_type, color, hp):
        self.x = x
        self.y = y
        self.monster_type = monster_type
        self.color = color
        self.hp = hp

    @staticmethod
    def random_spawn(occupied, forbidden, grid_w, grid_h):
        x = random.randint(0, grid_w - 1)
        y = random.randint(0, grid_h - 1)

        while (x, y) in occupied or (x, y) in forbidden:
            x = random.randint(0, grid_w - 1)
            y = random.randint(0, grid_h - 1)

        return WanderingMonster(x, y, "Goblin", [0, 255, 0], 20)

    @staticmethod
    def from_dict(data):
        return WanderingMonster(
            data["x"],
            data["y"],
            data["monster_type"],
            data["color"],
            data["hp"]
        )

    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y,
            "monster_type": self.monster_type,
            "color": self.color,
            "hp": self.hp
        }

    def move(self, occupied, forbidden, grid_w, grid_h):
        direction = random.choice(["up", "down", "left", "right"])

        new_x = self.x
        new_y = self.y

        if direction == "up":
            new_y -= 1
        elif direction == "down":
            new_y += 1
        elif direction == "left":
            new_x -= 1
        elif direction == "right":
            new_x += 1

        if new_x < 0 or new_x >= grid_w:
            return

        if new_y < 0 or new_y >= grid_h:
            return

        if (new_x, new_y) in occupied:
            return

        if (new_x, new_y) in forbidden:
            return

        self.x = new_x
        self.y = new_y
