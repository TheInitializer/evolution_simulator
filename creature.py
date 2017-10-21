class Creature:
    def __init__(self, mutability_chance, max_health, min_health,
                 regen_speed, speed, strength, init_x, init_y):
        self.mutability_chance = mutability_chance
        self.max_health = max_health
        self.min_health = min_health
        self.regen_speed = regen_speed
        self.speed = speed
        self.strength = strength

        self.pos = (init_x, init_y)

    def sayHi(self):
        print("hi")
