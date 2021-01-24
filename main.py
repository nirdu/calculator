import sys

# to check if the number is too large to be converted(if i cant use library it will just return as exception )
# or maybe float('inf')

# table of operators and their strength
OPERA_TABLE = {
    "+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "@": 5, "$": 5, "&": 5, "!": 6, "~": 6
}
# operators that only need one parameter from their right
OPERA_BEFORE = ('~')
# operators that only need one parameter from their left
OPERA_AFTER = ('!')
# all the chars (without the operators) that are legal in my code
LEGAL_TABS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'e', '.', '(', ')')
ARE_NOT_FOR_NUMBERS = ('(', ')')


class InputCheck:
    def __init__(self, input_string):
        self.input_string = input_string

    # check if the expression is empty
    def empty_input(self):
        if self.input_string is "":
            print("pls enter an expression(it is empty)")
            return False
        return True

    # check max length
    def max_len(self):
        max_length = 800
        if len(self.input_string) > max_length:
            print("the expression is too long for my calculator (i support ", max_length, " chars)")
            return False
        return True

    # check if the expression has illegal chars
    def legal_input(self):
        for char_in_exp in self.input_string:
            if char_in_exp not in LEGAL_TABS:
                if char_in_exp not in OPERA_TABLE.keys():
                    print("illegal char: ", char_in_exp)
                    return False
        return True

    # check if the expression has good brackets
    def check_bar(self):
        counter = 0
        counter_bar = 0
        size_of_express = len(self.input_string)
        flag_leg = False
        flag_end = False
        # go through all the expression
        for index_in_exp in range(0, size_of_express):
            if self.input_string[index_in_exp] is '(':
                counter = index_in_exp + 1
                while flag_end is False:
                    # reached the end without closing
                    if counter > (size_of_express - 1):
                        flag_end = True
                    # this brackets arent useless
                    elif self.input_string[counter].isdigit() or self.input_string[counter] in OPERA_TABLE.keys():
                        # is not in the outside brackets
                        if counter_bar is 0:
                            flag_end = True
                            flag_leg = True
                        # another brackets
                    elif self.input_string[counter] is '(':
                        counter_bar += 1
                        # end brackets
                    elif self.input_string[counter] is ')':
                        counter_bar -= 1
                        # the checked bracket is closed
                        if counter_bar is -1:
                            flag_end = True
                    counter += 1
                # not legal
                if flag_leg is False:
                    print("problem with the brackets in this expression")
                    return False
                # continue
                else:
                    flag_leg = False
                    flag_end = False
                    counter_bar = 0
        return True

    def check_string(self):
        return self.empty_input() and self.legal_input() and self.check_bar() and self.max_len()


class GetInput:

    # @staticmethod
    # remove the spaces from the expression
    def remove_spaces(self, stringToChange):
        stringToChange = stringToChange.replace(" ", "")
        return stringToChange

    # remove the double minuses from the expression
    def remove_minuses_son(self, express):
        while express.find("++") is not -1 or express.find("--") is not -1 or express.find("+-") is not -1:
            # remove double ++
            express = express.replace("++", "+")
            # two minus is plus
            express = express.replace("--", "+")
            #  minus plus  is minus
            express = express.replace("+-", "-")
            # RecursionError
            self.remove_minuses_son(express)
        return express

    # remove the double minuses from the expression
    def remove_minuses_father(self, express):
        express = self.remove_minuses_son(express)
        if express[0] is "+":
            express = express.replace(express[0], '', 1)
        return express

    # check if the character before the plus is not another number or chars that need the plus
    def condition_for_pluses(self, char_to_check):
        if char_to_check.isdigit() is False:
            if char_to_check not in OPERA_AFTER:
                if char_to_check is not 'e':
                    if char_to_check is not ')':
                        return True
        return False

    # check if the input is illegal because of the pluses
    def check_pluses(self, express):
        size_of_express = len(express)
        for index in range(0, size_of_express):
            if express[index] is '+':
                # the first character is +
                if index is 0:
                    return False
                else:
                    # useless character
                    if self.condition_for_pluses(express[index - 1]) is True:
                        return False
        return True

    # remove the pluses that were maybe created by the function remove_minuses
    def remove_pluses(self, express):
        size_of_express = len(express)
        for index in range(0, size_of_express - 1):
            # reached end
            if index < size_of_express:
                if express[index] is '+':
                    if index is 0:
                        # delete the + from the start
                        express = express[1:]
                        size_of_express = len(express)
                        index = index - 1
                    else:
                        if self.condition_for_pluses(express[index - 1]) is True:
                            # delete the new created +
                            express = express[:index] + express[index + 1:]
                            size_of_express = len(express)
                            index = index - 1
        return express

    def input_getter(self):
        # until the input is good
        while True:
            try:
                exp_input = input("Enter your expression:")
                # remove the spaces
                exp_input = self.remove_spaces(exp_input)
                # it is legal from the check functions in the class InputCheck
                if InputCheck(exp_input).check_string() is True:
                    # the pluses here are illegal
                    if self.check_pluses(exp_input) is False:
                        print("sorry wrong uses of + , the calculator doesnt support +number as number")
                    else:
                        exp_input = self.remove_minuses_father(exp_input)
                        exp_input = self.remove_pluses(exp_input)
                        return exp_input
            # out of memory exception
            except MemoryError:
                print("out of memory")
                print("please try again")
            except OverflowError as oe:
                print("After the Overflow error", oe)
                print("please try again")
            except RuntimeError:
                print("unexpected error")
                print("please try again")

    # use for tests
    def input_getter_for_test(self, x):
        # until the input is good
        try:

            exp_input = x
            # remove the spaces
            exp_input = self.remove_spaces(exp_input)
            # it is legal from the check functions in the class InputCheck
            if InputCheck(exp_input).check_string() is True:
                # the pluses here are illegal
                if self.check_pluses(exp_input) is False:
                    print("sorry wrong uses of + , the calculator doesnt support +number as number")
                else:
                    exp_input = self.remove_minuses_father(exp_input)
                    exp_input = self.remove_pluses(exp_input)
                    return exp_input
            # wrong input was found in the pre calculate input validators
            return False
        # out of memory exception
        except MemoryError:
            print("out of memory")
            print("please try again")
        except OverflowError as oe:
            print("After the Overflow error", oe)
            print("please try again")
        except RuntimeError:
            print("unexpected error")
            print("please try again")


class OperatorsFun:
    # check if the number is decimal
    def is_decimal(self, num):
        if ((num - int(num)) > 0) is True:
            return True
        return False

    # the size of the answer is too big for my calculator
    def too_long(self, num):
        if sys.float_info.max < num or -sys.float_info.max > num:
            return True
        return False

    def plus(self, op1, op2):
        if self.too_long(op1 + op2):
            print("the number is too long")
            return None
        return op1 + op2

    def minus(self, op1, op2):
        if self.too_long(op1 - op2):
            print("the number is too long")
            return None
        return op1 - op2

    def mul(self, op1, op2):
        if self.too_long(op1 * op2):
            print("the number is too long")
            return None
        return op1 * op2

    def dev(self, op1, op2):
        if op2 == 0:
            print("its illegal to divide by zero")
            return None
        if self.too_long(op1 / op2):
            print("the number is too long")
            return None
        return op1 / op2

    def mod(self, op1, op2):
        return op1 % op2

    def power(self, op1, op2):
        try:
            if self.too_long(op1 ** op2):
                print("the number is too long")
                return None
        except OverflowError as oe:
            print("the number is too long")
            return None
        # neg^dec is complex
        if self.is_decimal(op2) and op1 < 0:
            print("complex number are not supported :", op1, "^", op2, "is complex")
            return None
        return op1 ** op2

    # maximum
    def ma(self, op1, op2):
        if op1 > op2:
            return op1
        else:
            return op2

    # minimum
    def mi(self, op1, op2):
        if op1 < op2:
            return op1
        else:
            return op2

    def fact(self, op):
        if op < 0:
            print("cant factorial a negative number")
            return None
        if self.is_decimal(op):
            print("cant factorial a not neutral number")
            return None
        facto = 1
        # calculate the factorial
        for factor_mul_to in range(1, int(op) + 1):
            facto = facto * factor_mul_to
            if self.too_long(facto):
                print("the number is too long")
                return None
        return facto

    def neg(self, op):
        return op * -1

    # average
    def ave(self, op1, op2):
        return (op1 + op2) / 2

    def operators_func(self, ope, op1, op2):
        if ope is '+':
            return self.plus(op1, op2)
        elif ope is '-':
            return self.minus(op1, op2)
        elif ope is '*':
            return self.mul(op1, op2)
        elif ope is '/':
            return self.dev(op1, op2)
        elif ope is '^':
            return self.power(op1, op2)
        elif ope is '%':
            return self.mod(op1, op2)
        elif ope is '@':
            return self.ave(op1, op2)
        elif ope is '$':
            return self.ma(op1, op2)
        elif ope is '&':
            return self.mi(op1, op2)
        elif ope is '!':
            return self.fact(op1)
        elif ope is '~':
            return self.neg(op2)
        else:
            print("problem")
            return None
        '''
        return {
            '+': plus(op1, op2),
            '-': minus(op1, op2),
            '*': mul(op1, op2),
            '/': dev(op1, op2),
            '^': power(op1, op2),
            '%': mod(op1, op2),
            '@': ave(op1, op2),
            '$': ma(op1, op2),
            '&': mi(op1, op2),
            '!': fact(op1),
            '~': neg(op1)
        }.get(ope, None)  # the operator is not founded
        '''


class SolveTheExpression:
    def __init__(self, expression):
        self.expression = expression
        self.flag_err = False
        self.flag_end = False

    # find the index of the next operator to solve
    def find_index_Of_ope(self):
        max_str = -1
        index_temp = -1
        for operator_index in range(0, len(self.expression)):
            # its an operator
            if self.expression[operator_index] in OPERA_TABLE.keys():
                # find the max from the values
                if OPERA_TABLE.get(self.expression[operator_index]) > max_str:
                    max_str = OPERA_TABLE.get(self.expression[operator_index])
                    index_temp = operator_index

        return index_temp

        # algorithm: get sort list of indexes of operators from the one of the most priority  to least
        '''
        list_of_indexes = []
        max_str = -1
        counter = 0
        index_temp=0
        for op in express:
            if express[op] in OPERA_TABLE.keys():
                counter += 1
        while counter != 0:
            for op in range(0, len(express)):
                if express[op] in OPERA_TABLE.keys():
                    if OPERA_TABLE.get(express[op]) > max_str and op not in list_of_indexes:
                        max_str = OPERA_TABLE.get(express[op])
                        index_temp = op
            list_of_indexes.append(index_temp)
            counter -= 1
            max_str = -1
            index_temp=0

        return list_of_indexes
        '''

    # check if the member is a number
    def check_if_number(self, index_of_ope, add_index):
        if type(self.expression[index_of_ope + add_index]) == int:
            return True
        if type(self.expression[index_of_ope + add_index]) == float:
            return True
        return False

    # remove the exercise and put the answer
    def change_to_answer(self, index_of_ope, minus_index, temp_number, rang):
        for times_to_delete in range(0, rang):
            self.expression.pop(index_of_ope - minus_index)
        self.expression.insert(index_of_ope - minus_index, temp_number)

    def ope_in_last(self, index_of_ope):
        # its operator that only needs the number before him
        if self.expression[index_of_ope] in OPERA_AFTER:
            # the member before him is number
            if self.check_if_number(index_of_ope, -1) is True:
                # cant make it shorter
                temp_number = OperatorsFun().operators_func(self.expression[index_of_ope],
                                                            self.expression[index_of_ope - 1], 0)
                # problem during the calculating
                if temp_number is None:
                    return None
                self.change_to_answer(index_of_ope, 1, temp_number, 2)
            else:
                print("input was bad (operator was done without a number)")
                self.flag_err = True

        else:
            print("input was bad (operator was used without reason)")
            self.flag_err = True
        return 0

    def minus_in_first(self, index_of_ope):
        # there is a number after the minus
        if self.check_if_number(index_of_ope, 1) is True:
            # put the negtive number in the place of the minus number
            temp_number = OperatorsFun().minus(0, self.expression[index_of_ope + 1])
            self.change_to_answer(index_of_ope, 0, temp_number, 2)
        else:
            print("input was bad (sequence of operators)")
            self.flag_err = True

    # the condition in the while in the "tilda_counter" function
    def condition_to_stop_in_tilda(self, index_of_ope, counter_of_neg):
        if self.expression[index_of_ope + counter_of_neg] is '-':
            return True
        if self.expression[index_of_ope + counter_of_neg] is '~':
            return True
        return False

    # check which sign should the number after the tilda has
    def tilda_counter(self, index_of_ope):
        counter_of_neg = 0
        # while the operators are - or ~
        while self.condition_to_stop_in_tilda(index_of_ope, counter_of_neg) is True:
            counter_of_neg += 1
        # if there is a number after the operators
        if self.check_if_number(index_of_ope, counter_of_neg) is True:
            return counter_of_neg
        else:
            return -1

    def ope_before(self, index_of_ope):
        # its operator that only needs the number after him
        counter_of_neg = self.tilda_counter(index_of_ope)
        # check if it is legal (there was number after the operators)
        if counter_of_neg is -1:
            self.flag_err = True
        else:
            temp_number = self.expression[index_of_ope + counter_of_neg]
            # check which sign should the number have
            if counter_of_neg % 2 is 1:
                temp_number = OperatorsFun().minus(0, self.expression[index_of_ope + counter_of_neg])
            self.change_to_answer(index_of_ope, 0, temp_number, counter_of_neg + 1)
        return 0

    def ope_in_mid(self, index_of_ope):
        # the next member is minus
        if self.expression[index_of_ope + 1] is '-':
            # there is a number after the minus
            if self.check_if_number(index_of_ope, 2) is True:
                temp_number = OperatorsFun().minus(0, self.expression[index_of_ope + 2])
                self.change_to_answer(index_of_ope, -1, temp_number, 2)
            else:
                print("input was bad (sequence of operators)")
                self.flag_err = True
        if self.flag_err is False:
            # there is a number after the operator
            if self.check_if_number(index_of_ope, 1) is True:
                # cant make it shorter
                temp_number = OperatorsFun().operators_func(self.expression[index_of_ope],
                                                            self.expression[index_of_ope - 1],
                                                            self.expression[index_of_ope + 1])
                # problem during the calculating
                if temp_number is None:
                    return None
                self.change_to_answer(index_of_ope, 1, temp_number, 3)
            else:
                print("input was bad (sequence of operators)")
                self.flag_err = True
        return 0

    def solver(self):
        index_of_ope = 0
        temp_number = 0
        # run till the end
        while self.flag_err is False and self.flag_end is False:
            # the answer
            if len(self.expression) is 1:
                if self.check_if_number(0, 0) is True:
                    self.flag_end = True
                else:
                    print("sorry bad input ", self.expression, " cant be solved")
                    self.flag_err = True
            else:
                index_of_ope = self.find_index_Of_ope()
                # operator is not founded but there are more than one member in the list
                if index_of_ope is -1:
                    print("input was bad (two numbers without operator)")
                    self.flag_err = True
                # the operator in the last place
                elif index_of_ope is (len(self.expression) - 1):
                    if self.ope_in_last(index_of_ope) is None:
                        return None

                elif index_of_ope is 0:
                    # the first member in the list is minus
                    if self.expression[index_of_ope] is '-':
                        self.minus_in_first(index_of_ope)
                    # the first member in the list is operator that need a number after him
                    elif self.expression[index_of_ope] in OPERA_BEFORE:
                        if self.ope_before(index_of_ope) is None:
                            return None
                    else:
                        print("bad input, wrong use of operator in the expression:", self.expression)
                        return None
                # the operator is in the list of the expression and not in the last place
                else:
                    # the operator need a number after him
                    if self.expression[index_of_ope] in OPERA_BEFORE:
                        if self.ope_before(index_of_ope) is None:
                            return None
                    # the member before him is number
                    elif self.check_if_number(index_of_ope, -1) is True:
                        # its not a operator that only needs  the number before him
                        if self.expression[index_of_ope] not in OPERA_AFTER:
                            if self.ope_in_mid(index_of_ope) is None:
                                return None
                        #  its  a operator that only needs  the number before him
                        else:
                            # cant make it shorter
                            temp_number = OperatorsFun().operators_func(self.expression[index_of_ope],
                                                                        self.expression[index_of_ope - 1], 0)
                            # problem during the calculating
                            if temp_number is None:
                                return None
                            self.change_to_answer(index_of_ope, 1, temp_number, 2)
                    else:
                        print("input was bad (operator was used without reason)")
                        self.flag_err = True
        # it couldn't solve the expression
        if self.flag_err is True:
            return None
        return self.expression


class SolveTheInput:

    def __init__(self, expression):
        self.expression = expression
        self.list_of_express = []
        self.counter = 0

    # to solve the expression between the brackets
    def list_solve(self):
        if len(self.list_of_express) <= 0:
            print("bad input: the brackets arent good")
            return None

        len_of_sub_list = 0
        # get the whole expression that is between the brackets
        while self.list_of_express[len(self.list_of_express) - 1 - len_of_sub_list] != '(':
            if len(self.list_of_express) - len_of_sub_list <= 0:
                print("bad input: the brackets arent good")
                return None
            # next
            len_of_sub_list = len_of_sub_list + 1
        # get the sub expression(the one to solve now)
        temp_expr = self.list_of_express[len(self.list_of_express) - len_of_sub_list:len(self.list_of_express)]
        temp_answer = SolveTheExpression(temp_expr).solver()
        # problem in solving the expression
        if temp_answer is None:
            return None
        # delete from the list the expression
        for times_of_delete in range(0, len_of_sub_list + 1):
            self.list_of_express.pop(len(self.list_of_express) - 1)
        # add the answer
        self.list_of_express.append(temp_answer[0])
        return 0

    # check the number before convert
    def check_number(self, string_number):
        # check if there is e
        if string_number.count('e') > 1:
            print("bad input: " + string_number + " not possible ")
            return False
        elif string_number.count('e') == 1:
            if string_number.find('e') == 0 or string_number.find('e') == (len(string_number) - 1):
                print("bad input: " + string_number + "not possible ")
                return False

        # check if there is .
        if string_number.count('.') > 1:
            print("bad input: " + string_number + " not possible ")
            return False
        elif string_number.count('.') == 1:
            if string_number.find('.') == 0 or string_number.find('.') == (len(string_number) - 1):
                print("bad input: " + string_number + " not possible ")
                return False

        # check in the number is in possible length
        if sys.float_info.max < float(string_number):
            print("the number is too long")
            return False
        return True

    # convert the number
    def create_number_to_stack(self, string_number):
        try:
            return float(string_number)
        except ValueError:

            print("sorry " + string_number + " isn't a number")
            return None

    def check_in_create_number(self, counter2, size_of_express):
        if (self.counter + counter2) < size_of_express:
            if self.expression[self.counter + counter2] in LEGAL_TABS:
                if self.expression[self.counter + counter2] not in ARE_NOT_FOR_NUMBERS:
                    return True
        return False

    def condition_check_operator_in_e(self, counter2):
        if self.expression[self.counter + counter2 + 1] is '-':
            return True
        if self.expression[self.counter + counter2 + 1] is '+':
            return True
        return False

    def is_an_e(self, counter2, size_of_express):
        # if the char is e
        if self.expression[self.counter + counter2] is 'e':
            # and the next char is not the end
            if (self.counter + counter2 + 1) < size_of_express:
                # if the next char is plus or minus
                if self.condition_check_operator_in_e(counter2) is True:
                    # if the char after him is not the end
                    if (self.counter + counter2 + 2) < size_of_express:
                        if self.expression[self.counter + counter2 + 2].isdigit():
                            return True
            return None
        return False

    # get the number from the whole expression
    def number_in_express(self, size_of_express):
        counter2 = 0
        temp_the_number_string = ""
        temp_the_number = 0

        # while the chars are chars that are used for create number and it is not the end of the expression
        while self.check_in_create_number(counter2, size_of_express):
            # a number that contain 3
            if self.is_an_e(counter2, size_of_express) is not False:
                # the number can be created
                if self.is_an_e(counter2, size_of_express) is True:
                    for add_counter in range(0, 3):
                        temp_the_number_string += self.expression[self.counter + counter2]
                        counter2 += 1
                else:
                    print("sorry input is not good, the syntax of e is num1+/-num2  ")
                    return None
            else:
                temp_the_number_string += self.expression[self.counter + counter2]
                counter2 += 1
        # problem in creating the number
        if self.check_number(temp_the_number_string) is False:
            return None
        # create te number
        else:
            temp_the_number = self.create_number_to_stack(temp_the_number_string)
            if temp_the_number is None:
                print("problem in the input")
                return None
            else:
                self.list_of_express.append(temp_the_number)

        self.counter = self.counter + counter2 - 1
        return 0

    def create_stack(self):
        # print(express)
        print(self.expression)
        size_of_express = len(self.expression)

        while self.counter < size_of_express:
            # the char is (
            if self.expression[self.counter] is '(':
                self.list_of_express.append(self.expression[self.counter])
            # the char is )
            elif self.expression[self.counter] is ')':
                if self.list_solve() is None:
                    return None
            elif self.expression[self.counter].isdigit():
                if self.number_in_express(size_of_express) is None:
                    return None
            # the char is a an operator
            else:
                self.list_of_express.append(self.expression[self.counter])
            self.counter += 1
        # problem in solving the expression
        answer_of_the_express = SolveTheExpression(self.list_of_express).solver()
        if answer_of_the_express is None:
            return None
        return answer_of_the_express[0]


def menu():
    print("welcome to my calculator")
    flag_end = False
    # while the user didnt enter stop
    while flag_end is False:
        # get the expression
        express = GetInput().input_getter()
        print("the answer is :", SolveTheInput(express).create_stack())
        print()
        # get if the user want to continue
        try:
            end_input = input("enter stop to end the program :")
            if end_input == "stop":
                flag_end = True

            # out of memory exception
        except MemoryError:
            print("out of memory")
            print("please try again")
        except OverflowError as oe:
            print("After the Overflow error", oe)
            print("please try again")
        except RuntimeError:
            print("unexpected error")
            print("please try again")
        print()


if __name__ == '__main__':
    menu()
