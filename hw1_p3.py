c=299792458
#指定變數c的值
v=input("Input velocity:")
#讓使用者輸入數字（表velocity）
r=1/((1-(float(v)**2)/(float(c)**2))**(1/2))
#定義如何算出the factor
print("Percentage of light speed=",float(v)/float(c))
#列印出Percentage of light speed
#定義Einstein's equation:travel_time=travel_distance/r
td_AC=4.3
td_BS=6.0
td_B=309
td_AG=2000000
#指定變數td_AC,td_BS,td_B,td_AG的值
print("Travel time to Alpha Centauri=",td_AC/r)
print("Travel time to Barnard's Star=",td_BS/r)
print("Travel time to Betelgeuse=",td_B/r)
print("Travel time to Andromeda Galaxy=",td_AG/r)
#列印出travel time