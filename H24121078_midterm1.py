i, j = 9, 9 #設定起始值
while i >= 1 and j >= 1 : #當i>=1時，迴圈可執行 #當j>=1時，迴圈可執行
		print(i, "x", j, "=", i * j, end = "\t") #9*9=81 
		print(i, "x", (j - 1), "=", i * (j - 1), end = "\t") #9*8=72
		print(i, "x", (j - 2), "=", i * (j - 2), end = "\n") #9*7=63
		i = i - 1 #i=8
	print() #列印空白行
	j = j - 3 #9-3=6
	i = 9 #設定新一輪迴圈的i值