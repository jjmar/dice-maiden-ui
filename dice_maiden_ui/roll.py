def calculate_num_dice(num_dice, advantage, disadvantage, critical_role):
    if advantage or disadvantage:
        return 2

    if critical_role:
        return num_dice * 2

    return num_dice


def calculate_advantage_disadvantage(advantage, disadvantage):
    if advantage:
        return 'd1'

    if disadvantage:
        return 'kl1'

    return ''


def calculate_modifier(base_modifier, extra_modifier):
    return base_modifier + extra_modifier


def calculate_dice_roll(num_dice, num_dice_sides, base_modifier,
                        extra_modifier, advantage, disadvantage, critical_role):

    roll_format = "!roll {num_dice}d{num_dice_sides} {adv_dis} {modifier:+}"

    num_dice = calculate_num_dice(num_dice, advantage, disadvantage, critical_role)
    adv_dis = calculate_advantage_disadvantage(advantage, disadvantage)
    modifier = calculate_modifier(base_modifier, extra_modifier)

    dice_roll = roll_format.format(num_dice=num_dice, num_dice_sides=num_dice_sides, adv_dis=adv_dis,
                                   modifier=modifier)

    return dice_roll


def generate_roll_string(command, modifier):
    return calculate_dice_roll(command['num_dice'], command['num_dice_sides'], command['modifier'],
                               modifier.extra_modifier.get(), modifier.advantage.get(),
                               modifier.disadvantage.get(), modifier.critical_hit.get())
