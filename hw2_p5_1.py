num = int(input("Input an integer number:"))
#輸入計算到第幾個費波那契數
k0 = 0
#第0項
k1 = 1
#第1項
k2 = 0
#第2項開始為0
i = 2
#從第二項開始套公式
while i <= num:
#根據餘數判斷哪兩項相加
	if (i % 3 == 2):
		k2 = k0 + k1
	elif (i % 3 == 0):
		k0 = k2 + k1
	elif (i % 3 == 1):
		k1 = k2 + k0
	i += 1
print("The " + str(num) + "-th Fibonacci sequence number is: ", end = "")
if (num % 3 == 0):
#若於數為0，則會停在k0
	print(k0)
elif (i % 3 == 1):
#若於數為1，則會停在k1
	print(k1)
elif (i % 3 == 2):
#若於數為2，則會停在k2
	print(k2)