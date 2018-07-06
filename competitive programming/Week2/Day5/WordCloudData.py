import unittest


class WordCloudData(object):
    def __init__(self, input_string):
        self.words_to_counts = {}
        temp = ""

        for i in input_string:
            i = i.lower()
            if (i in ["-", "'"]) or (i.isalnum()):
                temp += i
            else:
                temp += " "

        temp2 = ""

        for i in temp:
            if i == " ":
                if temp2 != "-" and temp2 != "":
                    if temp2 in self.words_to_counts.keys():
                        self.words_to_counts[temp2] += 1
                    else:
                        self.words_to_counts[temp2] = 1
                temp2 = ""
            else:
                temp2 += i

        if temp2 != "-" and temp2 != "":
            if temp2 in self.words_to_counts.keys():
                self.words_to_counts[temp2] += 1
            else:
                self.words_to_counts[temp2] = 1


# Tests

# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.

class Test(unittest.TestCase):
    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'i': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'strawberry': 1, 'short': 1, 'yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {"bakery": 1, "cakes": 1, "allie's": 1, "sasha's": 1}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)