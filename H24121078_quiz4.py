user_input = input("Enter a sequence of integers seperated by whitespace: ")
#使用者輸入串列
i = 0
for i in user_input:
	j = i + 1
	for j in user_input:
		j = j + 1
	i = i + 1
	print("Length: ",len(user_input))