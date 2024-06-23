scale_value=input("Please input a Richter scale value: ")
#讓使用者輸入Richter的體重
print("Richter scale value: ",scale_value)
#列印出Richter的體重計數值
Joules=10**((1.5*(float(scale_value)))+4.8)
#定義Joules跟scale_value換算公式
tons_TNT=(4.184*(10**9))*(float(Joules))
#定義tons_TNT跟Joules換算公式
nutritious_lunches=2930200*(float(Joules))
#定義nutritious_lunches跟Joules換算公式
print("Equivalence in Joules: ",Joules)
#列印出換算後的Joules數值
print("Equivalence in tons of TNT: ",tons_TNT)
#列印出換算後的tons_TNT數值
print("Equivalence in the number of nutritious lunches: ",nutritious_lunches)
#列印出換算後的nutritious_lunche數值