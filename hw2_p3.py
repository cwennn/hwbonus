year = int(input("Please input Year:"))
#輸入年份
month = int(input("Please input month:"))
#輸入月份
leap = False
if (year % 4) == 0:
#計算是否為閏年
	if (year % 400) == 0:
		leap = True
	elif (year % 100) != 0:
		leap = True
c = year // 100
#取年份前兩位數
C = int(2 * (3 - (c % 4)))
#套公式
y = year % 100
#取年份後兩位數
Y = int(((y % 28) + ((y % 28) / 4)) % 7)
#套公式
if (leap == True) and (month <= 2):
#閏年且月份為1,2月則Y-1
	Y -= 1
M = int((3.4 + ((month - 3) % 12) * 2.6) % 7)
#套公式
if month <= 2:
#月份為1,2月份則M-1
	M -= 1
D = 1
#計算該年該月第一天
W = int((C + Y + M + D) % 7)
#計算該日為禮拜幾
print("Sun Mon Tue Wed Thu Fri Sat")
print("    " * W, end = "")
big = [1, 3, 5, 7, 8, 10, 12]
#大月
small = [4, 6, 9, 11]
#小月
day = 0
if month == 2:
#閏年2月29天
	if leap == True:
		day = 29
	else:
#平年2月28天
		day = 28
elif month in big:
#大月31天
	day = 31
elif month in small:
#小月30天
	day = 30
if W == 0:
	W = 7
for j in range(1, day + 1):
	if j <= 9:
		print("0" + str(j) + "  ", end = "")
#1到9號前面需要補0
	elif j <= day:
		print(str(j) + " ", end = "")
	if (j % 7) == (7 - W):
		print("")
















