user_input = input("Enter the size of the grid: ")#使用者輸入
print(("_ _ _ _ _" + "\n") * int(user_input))#列印出對照使用者輸入的＿
coordinates_input = input("Enter the cell coordinates to edit: ")#使用者輸入
value_input = input("Enter the new value for the cell: ")#使用者輸入
if coordinates_input != "done":#當使用者輸入done，開始執行以下迴圈
	while coordinates_input != "done":
		print()
		coordinates_input = input("Enter the cell coordinates to edit: ")
		value_input = input("Enter the new value for the cell: ")
		continue
elif coordinates_input == "done":#當使用者不是輸入done，結束程式
	print()