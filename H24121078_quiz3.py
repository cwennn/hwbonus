print("Welcome to the simple caculator programe!")
#當使用者打開時顯示字串Welcome to the simple caculator programe!
first=input("Enter the fisrt number: ")
#讓使用者輸入第一個數字
second=input("Enter the second number: ")
#讓使用者輸入第二個數字
select=input("Select an arithmetic operation (+, -, *, /): ")
#讓使用者輸入運算符號
if select == "+":
	result=float(first)+float(second)
#當運算符為+時，結果為第一個數字加第二個數字
	print("Result: ",result)
#印出運算結果
elif select == "-":
	result=float(first)-float(second)
#當運算符為-時，結果為第一個數字減第二個數字
	print("Result: ",result)
#印出運算結果
elif select == "*":
	result=float(first)*float(second)
#當運算符為*時，結果為第一個數字乘第二個數字
	print("Result: ",result)
#印出運算結果
elif select == "/":
	result=float(first)/float(second)
#當運算符為/時，結果為第一個數字除第二個數字
	print("Result: ",result)
#印出運算結果
want=input("Do you want to perform another calculation? (yes or no): ")
#當字串跳出Do you want to perform another calculation? (yes or no): 讓使用者輸入yes或no
if want=="yes":
	fisrt=input("Enter the fisrt number: ")
	second=input("Enter the second number: ")
	select=input("Select an arithmetic operation (+, -, *, /): ")
	result=float(first)+float(second)
	print("Result: ",result)
#當輸入者輸入要在執行另一個算式時，重複之前的動作
elif want=="no":
	print("Goodbye!")
#當輸入者輸入不要在執行另一個算式時，列印Goodbye!，並結束程式