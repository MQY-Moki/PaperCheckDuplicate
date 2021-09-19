import pytest
from main.main import Main

# 测试orig.txt与orig_0.8_add.txt
def test_1():
    Main('../main/texts/orig.txt', '../main/texts/orig_0.8_add.txt', '../result.txt')

# 测试orig.txt与orig_0.8_del.txt
def test_2():
    Main('../main/texts/orig.txt', '../main/texts/orig_0.8_del.txt', '../result.txt')

# 测试orig.txt与orig_0.8_dis_1.txt
def test_3():
     Main('../main/texts/orig.txt', '../main/texts/orig_0.8_dis_1.txt', '../result.txt')

# 测试orig.txt与orig_0.8_dis_10.txt
def test_4():
    Main('../main/texts/orig.txt', '../main/texts/orig_0.8_dis_10.txt', '../result.txt')

# 测试orig.txt与orig_0.8_dis_15.txt
def test_5():
    Main('../main/texts/orig.txt', '../main/texts/orig_0.8_dis_15.txt', '../result.txt')

# 测试orig_0.8_dis_15.txt与orig_0.8_dis_10.txt
def test_6():
    Main('../main/texts/orig_0.8_dis_15.txt','../main/texts/orig_0.8_dis_10.txt','../result.txt')

# 测试orig_0.8_dis_10.txt与orig_0.8_dis_1.txt
def test_7():
    Main('../main/texts/orig_0.8_dis_10.txt','../main/texts/orig_0.8_dis_1.txt','../result.txt')

# 测试orig_0.8_dis_15.txt与orig_0.8_dis_1.txt
def test_8():
    Main('../main/texts/orig_0.8_dis_15.txt','../main/texts/orig_0.8_dis_1.txt','../result.txt')

#测试orig_0.8_dis_10.txt与orig_0.8_del.txt
def test_9():
    Main('../main/texts/orig_0.8_dis_10.txt','../main/texts/orig_0.8_del.txt','../result.txt')

#测试文件路径错误
@pytest.mark.xfail(2 > 1, reason="标注为预期失败")
def test_10():
    Main('../main/texts/orig_0.8_dis_10.txt','../main/orig_0.8_del.txt','../result.txt')
    raise FileNotFoundError("文件路径错误！")
    assert 0


if __name__ == '__main__':
    pytest.main("-s main.py")
