h1=input("Input the height of the 1st ball:",)
m1=input("Input the mass of the 1st ball:")
m2=input("Input the mass of the 2nd ball:")
#讓使用者輸入資訊：第一顆球的高度，第一顆球的重量，第二顆球的重量
g=9.8
#指定變數g的值
U1=(float(m1))*(float(g))*(float(h1))
#定義一號球的位能公式
v1=((float(U1)*2)/(float(m1)))**(1/2)
#U1=mgh=E1=(1/2)(m1)(v1)**2
print("The velocity of the 1st ball after slide:",float(v1))
#列印出一號球的速度
v2=(((float(U1)*2)/float(m2)))**(1/2)
#E1=E2=(1/2)(m2)(v2)**2=U1
print("The velocity of the 2nd ball after collision:",float(v2))
#列印出二號球的速度