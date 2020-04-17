import unittest
from collections import Counter

print('Problem: Is a string a permutation of another')
CBLUE   = '\33[34m'
masterString = 'AmazonWebServices'
stringToMatch = 'WebServicesAmazon'

print("Checking String {}{} is a permuation of {}{}".format(CBLUE, stringToMatch,masterString,CBLUE))

def check_permutation(string1, string2):
    if(len(string1) != len(string2)):
        return False
    counter = Counter()
    for c in string1:
        counter[c] += 1
    for c in string2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True


class Test(unittest.TestCase):
    dataT = (("AWS","WAS"),("blue","uleb"))
    dataF = (("AWSA","WAS"),("blue","ulxy"))
    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()