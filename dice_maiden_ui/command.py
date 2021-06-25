class Command:
    def __init__(self, json_command):
        self.name = json_command['name']
        self.num_dice = json_command['num_dice']
        self.num_dice_sides = json_command['num_dice_sides']
        self.modifier = json_command['modifier']

    def to_dice_maiden_roll(self):
        modifier_sign = '+' if self.modifier >= 0 else ''
        modifier_str = "{}{}".format(modifier_sign, self.modifier)

        return "!roll {}d{}{}".format(self.num_dice, self.num_dice_sides,  modifier_str)
