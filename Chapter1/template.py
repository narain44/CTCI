import unittest

def oneaway(str1,str2):
    print("Strings to compare :",str1,str2)


class TestOneAway(unittest.TestCase):
    dataT = (
        ("Pie","Pile"),
    )
    def test(self):
        for tupules in self.dataT:
            oneaway(*tupules)

if __name__=="__main__":
    unittest.main()