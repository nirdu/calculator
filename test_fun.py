import main
import pytest


def menu_for_test(x):
    # get the expression that need to be calculated
    express = main.GetInput().input_getter_for_test(x)
    # the pre validators found problem in the input
    if express is False:
        return None
    # get the answer (if it can be solved)
    return main.SolveTheInput(express).create_stack()


# blank input
def test_method1():
    x = ""
    assert menu_for_test(x) is None


# gibberish input
def test_method2():
    x = "21321dfdfdf"
    assert menu_for_test(x) is None


# spaces input
def test_method3():
    x = "      "
    assert menu_for_test(x) is None


# mistake 1 input
def test_method4():
    x = "2*^3"
    assert menu_for_test(x) is None


# mistake 2 input
def test_method5():
    x = "*2+3"
    assert menu_for_test(x) is None


# mistake 3 input
def test_method6():
    x = "2++2"
    assert menu_for_test(x) is None


# mistake 4 input
def test_method7():
    x = "2/7/"
    assert menu_for_test(x) is None


# mistake 5 input
def test_method8():
    x = "2458*&21"
    assert menu_for_test(x) is None


# mistake 6 input
def test_method9():
    x = "13!-+&2"
    assert menu_for_test(x) is None


# easy 1 input
def test_method10():
    x = "3^2"
    assert menu_for_test(x) == 9


# easy 2 input
def test_method11():
    x = "2*12"
    assert menu_for_test(x) == 24


# easy 3 input
def test_method12():
    x = "123-12"
    assert menu_for_test(x) == 111


# easy 4 input
def test_method13():
    x = "13+34-2"
    assert menu_for_test(x) == 45


# easy 5 input
def test_method14():
    x = "12^3*4"
    assert menu_for_test(x) == 6912


# easy 6 input
def test_method15():
    x = "13&4"
    assert menu_for_test(x) == 4


# easy 7 input
def test_method16():
    x = "-12%4"
    assert menu_for_test(x) == 0


# easy 8 input
def test_method17():
    x = "12+~4"
    assert menu_for_test(x) == 8


# easy 9 input
def test_method18():
    x = "15/5$3"
    assert menu_for_test(x) == 3


# easy 10 input
def test_method19():
    x = "15@5"
    assert menu_for_test(x) == 10


# easy 11 input
def test_method20():
    x = "13*4-3"
    assert menu_for_test(x) == 49


# easy 12 input
def test_method21():
    x = "12$4&-2"
    assert menu_for_test(x) == -2


# easy 13 input
def test_method22():
    x = "14^12/6"
    assert menu_for_test(x) == 9448985395882.666


# easy 14 input
def test_method23():
    x = "12!+~2"
    assert menu_for_test(x) == 479001598


# easy 15 input
def test_method24():
    x = "12-43+12*2/2"
    assert menu_for_test(x) == -19


# complex 1 input
def test_method25():
    x = "12+ (43*2) /2+(-2*(54))"
    assert menu_for_test(x) == -53


# complex 2 input
def test_method26():
    x = "(-1)+   -65*(2^2) -2+(2+(3&(12)))"
    assert menu_for_test(x) == -258


# complex 3 input
def test_method27():
    x = "~(123 @ ((145*2/4%6-6/7) @ (3^5 - 9000)))"
    assert menu_for_test(x) == 2109.839285714286


# complex 4 input
def test_method28():
    x = "5&6@(520/10)+~5^2+3$--4-4+(---(2+2)!)%6"
    assert menu_for_test(x) == 53.5


# complex 5 input
def test_method29():
    x = "24%12^2-7*9&      (2+3-4+6$22--8-~-9+8!)"
    assert menu_for_test(x) == -63


# complex 6 input
def test_method30():
    x = "----(8--8)$5+2%456+99*~(6+6)+2^(-(1+1))"
    assert menu_for_test(x) == -1169.75


# complex 7 input
def test_method31():
    x = "----~4+67 * 2-4522/221+(2&23 * 22%3^2)-7*2@4"
    assert menu_for_test(x) == 90.53846153846155


# complex 8 input
def test_method32():
    x = "005* 2^2&2-7&88+224@26-(43-44+66&2----45*(321&2))"
    assert menu_for_test(x) == 47


# complex 9 input
def test_method33():
    x = "----~4+67 * 2-4522/221+(2&23 * 22%3^2)-7*2@4"
    assert menu_for_test(x) == 90.53846153846155


# complex 10 input
def test_method34():
    x = "~(123 @ ((145*2/4%6-6/7) @ (3^5 - 9000)))"
    assert menu_for_test(x) == 2109.839285714286


# complex 11 input
def test_method35():
    x = "55%66$78^2+5----65^2*((3$5^7@555)+6^2&12^2)-2"
    assert menu_for_test(x) == 1.0874215407751212e+200


# complex 12 input
def test_method36():
    x = "( (1+(3+(5*7)-9)@4.56) * (2.5) ) / ~ (-5.12) "
    assert menu_for_test(x) == 8.681640625


# complex 13 input
def test_method37():
    x = "6!-41*(2+3%-3)+~5+~2-6@(9+1)"
    assert menu_for_test(x) == 623


# complex 14 input
def test_method38():
    x = "(--(--(--(--(4+4)))))"
    assert menu_for_test(x) == 8


# complex 15 input
def test_method39():
    x = "(1321*4-912^3/5)*(13--4$3)"
    assert menu_for_test(x) == -2578981967.2


# complex 16 input
def test_method40():
    x = "(12--(4^2+(-------5    +12!)))"
    assert menu_for_test(x) == 479001623


# complex 17 input
def test_method41():
    x = "1       2+23*5!+(12@3$-5)/1"
    assert menu_for_test(x) == 2779.5


# complex 18 input
def test_method42():
    x = "12.5655+3^3 -(100/10*20&7)"
    assert menu_for_test(x) == -30.4345


# complex 19 input
def test_method43():
    x = "~((88/23*2.2)^3&(5!+---6^3))"
    assert menu_for_test(x) == -1.5239066784713154e-89


# complex 20 input
def test_method44():
    x = "(1+2)^((-1+~2)*-1)!+(3-1)!"
    assert menu_for_test(x) == 731
