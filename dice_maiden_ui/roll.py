def generate_roll_string(num_dice, num_dice_sides, base_modifier,
                         extra_modifier, advantage, disadvantage, critical_role):

    roll_format = "!roll {num_dice}d{num_dice_sides} {adv_dis}{modifier:+}"

    num_dice = _calculate_num_dice(num_dice, advantage, disadvantage, critical_role)
    adv_dis = _calculate_advantage_disadvantage(advantage, disadvantage)
    modifier = _calculate_modifier(base_modifier, extra_modifier)

    dice_roll = roll_format.format(num_dice=num_dice, num_dice_sides=num_dice_sides, adv_dis=adv_dis,
                                   modifier=modifier)

    return dice_roll


def _calculate_num_dice(num_dice, advantage, disadvantage, critical_role):
    if advantage or disadvantage:
        return 2

    if critical_role:
        return num_dice * 2

    return num_dice


def _calculate_advantage_disadvantage(advantage, disadvantage):
    if advantage:
        return 'd1 '

    if disadvantage:
        return 'kl1 '

    return ''


def _calculate_modifier(base_modifier, extra_modifier):
    return base_modifier + extra_modifier
