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

הקוד שלי מחזיר:
None
במידה שהביטוי אינו נכון או שהפותר שלי אינו מסוגל לפתור.

או:
את התוצאה הסופית אם הבטוי הינו נכון.
מכיוון שהפונקציות שפועלות לפני הפותר שלי ובדקות על הקלט אינן מחזירות תשובה אלא גורמות ללואה של הכנסת המידע להשמיך לרוץ,יצרתי פונקצייה חדשה במיוחד עבור הפותר.
פונקציה זאת מחזירה שקר עבור קלט לא נכון של הפונקציות הנ"ל או את התשובה מהפותר
