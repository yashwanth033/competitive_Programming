import unittest


def is_single_riffle(half1, half2, shuffled_deck):
    half1Index = 0
    half2Index = 0
    half1MaxIndex = len(half1) - 1
    half2MaxIndex = len(half2) - 1
    for card in shuffled_deck:
        if (half1Index <= half1MaxIndex and card == half1[half1Index]):
            half1Index += 1
        elif (half2Index <= half2MaxIndex and card == half2[half2Index]):
            half2Index += 1
        else:
            return False
    return True


# Tests

class Test(unittest.TestCase):
    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)