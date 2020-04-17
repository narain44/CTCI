# EXAMPLE
# Input: "Mr 3ohn Smith 13
# Output: "Mr%203ohn%20Smith"

import unittest
print('Problem: URLify a string URL')


def urlifysimple(stringURL,length):
    encodedURL = ''
    for characterIndex in range(0,length) :
        if (stringURL[characterIndex] == ' '):
            encodedURL += '%20'
        else:
            encodedURL += stringURL[characterIndex]
    print("urlifysimple Returning ",encodedURL)
    return encodedURL

def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1
    print("urlify Returning ", string)
    return string


class Test(unittest.TestCase):
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def testURL(self):
        for [test_string, length, expected] in self.data:
            actual = urlifysimple(test_string,length)
            self.assertEqual(actual, ''.join(expected))
            # ''.Join is called to convert expected char list to string
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
