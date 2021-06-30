class Modifiers:
    def __init__(self, advantage, disadvantage, extra_modifier, critical_hit):
        self.advantage = advantage
        self.disadvantage = disadvantage
        self.extra_modifier = extra_modifier
        self.critical_hit = critical_hit

    def reset(self):
        self.advantage.set(False)
        self.disadvantage.set(False)
        self.extra_modifier.set(0)
        self.critical_hit.set(False)
