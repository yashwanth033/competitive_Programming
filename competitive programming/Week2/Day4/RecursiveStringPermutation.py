import unittest


def get_permutations(string):
    n = len(string)
    a = list(string)
    if (string == ''):
        return set([string])
    perms = set()
    permute(a, 0, n - 1, perms)
    return perms


def toString(List):
    return ''.join(List)


def permute(a, l, r, perms):
    if l == r:
        perms.add(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r, perms)
            a[l], a[i] = a[i], a[l]


# Tests

class Test(unittest.TestCase):
    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)