# calculator
code-Nir Dushnitzky

the program itself is in main.py
the tests are in test_fun.py

you need to run main.py and it should activate the function "menu" that let you write input expression and get the answer.!!!!


האלגוריתם שלי בודק קודם כול בכמה בדיקות את הקלט ובמידת הצורך מחזיר שהקלט אינו נכון.
לאחר מכן הקוד שלי עובר באמצעות לולאה על הביטוי שהוכנס
ומעביר אותו ממחרוזת לרשימה

הפתירה שלי בנויה לפי עקרון מחסנית, כל פעם שאני עובר על תו סיגרת סוגריים אני פותר את הביטוי שבין שני הסוגריים 
ומחזיר שגיאה או את התוצאה בהתאם

פונקציית הפותר שלי מחזירה שני מצבים:

None התשובה או


מכיוון שפונקציות הבדיקה  שפועלות לפני הפותר שלי אינן מחזירות תשובה אלא גורמות ללואה של הכנסת המידע להמשיך לרוץ,יצרתי פונקצייה חדשה במיוחד עבור הפותר.

פונקציה זאת מחזירה שקר עבור קלט לא נכון של הפונקציות הנ"ל או את התשובה מהפותר

quick explanation to every class:

class InputCheck-get the string of the input and check if few rules are kept: not empty,less than max size,conatin legal tabs,and every brackets are needed.

class GetInput- the class ask for input from the user, send it to "InputCheck" and if legal tahn send it to "SolveTheInput".
In this class the input is changed(spaces are removed and minuses in row are removed or change to plus) and checked if expectation is thrown.

class OperatorsFun-get two numbers and operator and return the answer to the expression.

class SolveTheExpression-get list of numbers and operators and return a the answer to the expression. until the end of the solving, each time the sub expression is chosen by  the priority. 

class SolveTheInput- get the string of the input and create a list of the exercise and in the end return None or the answer. Here to protect the priority of brackets each time that the char ')' is reached the expression between the brackets are sent to the class "SolveTheExpression" and the answer is replaced with the expression.

def menu()- while the user dont enter "stop" when he is asked if he wants to continue, keep getting expression from him.

test_fun.py- has funtions of the tests.
