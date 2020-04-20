import unittest

def oneaway(str1,str2):
    print("Strings to compare :",str1,str2)
    difference = len(str1) - len(str2)
    if(difference <0):
        difference = -difference

    if difference >1 :
        return False
    # for character
    # if difference == 0:

    return True

class TestOneAway(unittest.TestCase):
    dataT = (
        ("Pie","Pile"),
    )
    def test(self):
        for tupules in self.dataT:
            result=oneaway(*tupules)
            self.assertTrue(result)

if __name__=="__main__":
    unittest.main()