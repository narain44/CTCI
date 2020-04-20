import unittest

print ("Palindrome Permutation")


def check_palindrome_permutation(str1):
    print("Checking ", str1)
    char_count_list = [0 for _ in range(ord('z') - ord('a') + 1)]
    countodd = 0
    for character in str1:
        x = char_number(character)
        if x != -1:
            char_count_list[x] += 1
            if char_count_list[x] % 2 == 0:
                countodd -= 1
            else:
                countodd += 1

    return countodd <= 1


def char_number(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(c)
    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    else:
        return -1


class TestPalindromePermutation(unittest.TestCase):
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test(self):
        for [test_string, expected] in self.data:
            actual = check_palindrome_permutation(test_string)
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
