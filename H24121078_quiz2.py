shopping_amount=input("Enter the shopping amount: ")
#讓使用者輸入購物金額
membership_level=input("Enter the membership level (Regular or Gold): ")
#讓使用者輸入他們的會員級別，有Regular,Gold,Platinum
if 1000<shopping_amount<2000:
	if Regular:
		print("Regular",float(shopping_amount)*0.1)
	if Gold:
		print("Gold",float(shopping_amount)*0.15)
elif 2000<shopping_amount<3000:
	if Regular:
		print("Regular",float(shopping_amount)*0.15)
	if Gold:
		print("Gold",float(shopping_amount)*0.2)
else 3000<shopping_amount:
	if Regular:
		print("Regular",float(shopping_amount)*0.2)
	if Gold:
		print("Gold",float(shopping_amount)*0.25)
#輸出對應金額及級別所擁有的折扣後金額