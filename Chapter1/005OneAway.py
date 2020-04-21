import unittest


def one_away(str1, str2):
    print("Strings to compare :", str1, str2)
    if len(str1) == len(str2):
        return one_edit_replace(str1, str2)
    elif len(str1) == (len(str2) + 1):
        return one_edit_insert(str1, str2)
    elif (len(str1) + 1) == len(str2):
        return one_edit_insert(str2, str1)
    return False


def one_edit_replace(str1, str2):
    edited = False
    for index in range(0, len(str1)):
        if str1[index] != str2[index]:
            if edited:
                return False
            else:
                edited = True
    return True


def one_edit_insert(str1, str2):
    i = 0
    j = 0
    edited = False
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if edited:
                return False
            else:
                edited = True
                i += 1
        else:
            i += 1
            j += 1
    return True

class TestOneAway(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test(self):
        for [str1, str2, expected] in self.data:
            actual = one_away(str1, str2)
            self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
