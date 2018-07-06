import unittest


def sort_scores(unorderedScores, highestPossibleScore):
    tempArray=[0]*(highestPossibleScore+1)
    for i in range(0,len(unorderedScores)):
        tempArray[unorderedScores[i]]+=1

    index=0
    for i in range(highestPossibleScore,-1,-1):
        for j in range(0,tempArray[i]):
            unorderedScores[index]=i
            index+=1
    return unorderedScores


# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)