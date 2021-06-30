from dice_maiden_ui.roll import generate_roll_string, _calculate_num_dice, _calculate_advantage_disadvantage


class TestGenerateRollString:
    def test_no_modifiers(self):
        expected = '!roll 1d20 +6'
        assert expected == generate_roll_string(1, 20, 6, 0, False, False, False)

    def test_advantage(self):
        expected = '!roll 2d20 d1 +6'
        assert expected == generate_roll_string(1, 20, 6, 0, True, False, False)

    def test_disadvantage(self):
        expected = '!roll 2d20 kl1 +6'
        assert expected == generate_roll_string(1, 20, 6, 0, False, True, False)

    def test_add_extra_modifier(self):
        expected = '!roll 1d20 +10'
        assert expected == generate_roll_string(1, 20, 6, 4, False,  False, False)

    def test_subtract_extra_modifer(self):
        expected = '!roll 1d20 +2'
        assert expected == generate_roll_string(1, 20, 6, -4, False, False, False)

    def test_critical_roll(self):
        expected = '!roll 4d8 +0'
        assert expected == generate_roll_string(2, 8, 0, 0, False,  False, True)

    def test_advantage_and_extra_modifiers(self):
        expected = '!roll 2d20 d1 +10'
        assert expected == generate_roll_string(1, 20, 6, 4, True, False, False)

    def test_disadvantage_and_extra_modifiers(self):
        expected = '!roll 2d20 kl1 +10'
        assert expected == generate_roll_string(1, 20, 6, 4, False, True, False)

    def test_critical_roll_and_extra_modifiers(self):
        expected = '!roll 2d8 +10'
        assert expected == generate_roll_string(1, 8, 4, 6, False, False, True)


class TestCalculateNumDice:
    def test_two_if_advantage(self):
        assert 2 == _calculate_num_dice(1, True, False, False)

    def test_two_if_disadvantage(self):
        assert 2 == _calculate_num_dice(1, False, True, False)

    def test_doubles_if_critical(self):
        assert 8 == _calculate_num_dice(4, False, False, True)

    def test_unmodified_if_all_false(self):
        assert 2 == _calculate_num_dice(2, False, False, False)


class TestCalculateAdvantageDisadvantage:
    def test_advantage(self):
        assert 'd1 ' == _calculate_advantage_disadvantage(True, False)

    def test_disadvantage(self):
        assert 'kl1 ' == _calculate_advantage_disadvantage(False, True)

    def test_empty_if_neither(self):
        assert '' == _calculate_advantage_disadvantage(False, False)
