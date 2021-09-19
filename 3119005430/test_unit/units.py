import pytest
from main.main import Main

class Test_unit(unittest.TestCase):

    # 测试orig.txt与orig_0.8_add.txt
    def test1(self):
        Main('../main/texts/orig.txt', '../main/texts/orig_0.8_add.txt', '../result.txt')

    # 测试orig.txt与orig_0.8_del.txt
    def test2(self):
        Main('../main/texts/orig.txt', '../main/texts/orig_0.8_del.txt', '../result.txt')

    # 测试orig.txt与orig_0.8_dis_1.txt
    def test3(self):
        Main('../main/texts/orig.txt', '../main/texts/orig_0.8_dis_1.txt', '../result.txt')

    # 测试orig.txt与orig_0.8_dis_10.txt
    def test4(self):
        Main('../main/texts/orig.txt', '../main/texts/orig_0.8_dis_10.txt', '../result.txt')

    # 测试orig.txt与orig_0.8_dis_15.txt
    def test5(self):
        Main('../main/texts/orig.txt', '../main/texts/orig_0.8_dis_15.txt', '../result.txt')


if __name__ == '__main__':
    unittest.main()
