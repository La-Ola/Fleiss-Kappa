import math

line1 = [468,6,14,0,0,0]
line2 = [5,84,171,124,10,14]
line3 = [39,106,1580,318,63,1]
line4 = [0,285,1492,2653,692,730]
line5 = [0,16,62,110,221,25]
line6 = [0,8,45,184,39,423]

x1 = line1[0]+line2[0]+line3[0]+line4[0]+line5[0]+line6[0]
x2 = line1[1]+line2[1]+line3[1]+line4[1]+line5[1]+line6[1]
x3 = line1[2]+line2[2]+line3[2]+line4[2]+line5[2]+line6[2]
x4 = line1[3]+line2[3]+line3[3]+line4[3]+line5[3]+line6[3]
x5 = line1[4]+line2[4]+line3[4]+line4[4]+line5[4]+line6[4]
x6 = line1[5]+line2[5]+line3[5]+line4[5]+line5[5]+line6[5]

ytotal = [sum(line1), sum(line2), sum(line3), sum(line4), sum(line5), sum(line6)]
xtotal = [x1, x2, x3, x4, x5, x6]

p1 = round(xtotal[0]/(6*ytotal[0]),3)
p2 = round(xtotal[1]/(6*ytotal[1]),3)
p3 = round(xtotal[2]/(6*ytotal[2]),3)
p4 = round(xtotal[3]/(6*ytotal[3]),3)
p5 = round(xtotal[4]/(6*ytotal[4]),3)
p6 = round(xtotal[5]/(6*ytotal[5]),3)

a = round((1/(ytotal[0]*(ytotal[0]-1)))*(pow(line1[0],2)+pow(line1[1],2)+pow(line1[2],2)+pow(line1[3],2)+pow(line1[4],2)+pow(line1[5],2)-ytotal[0]),3)
b = round((1/(ytotal[1]*(ytotal[1]-1)))*(pow(line2[0],2)+pow(line2[1],2)+pow(line2[2],2)+pow(line2[3],2)+pow(line2[4],2)+pow(line2[5],2)-ytotal[1]),3)
c = round((1/(ytotal[2]*(ytotal[2]-1)))*(pow(line3[0],2)+pow(line3[1],2)+pow(line3[2],2)+pow(line3[3],2)+pow(line3[4],2)+pow(line3[5],2)-ytotal[2]),3)
d = round((1/(ytotal[3]*(ytotal[3]-1)))*(pow(line4[0],2)+pow(line4[1],2)+pow(line4[2],2)+pow(line4[3],2)+pow(line4[4],2)+pow(line4[5],2)-ytotal[3]),3)
e = round((1/(ytotal[4]*(ytotal[4]-1)))*(pow(line5[0],2)+pow(line5[1],2)+pow(line5[2],2)+pow(line5[3],2)+pow(line5[4],2)+pow(line5[5],2)-ytotal[4]),3)
f = round((1/(ytotal[5]*(ytotal[5]-1)))*(pow(line6[0],2)+pow(line6[1],2)+pow(line6[2],2)+pow(line6[3],2)+pow(line6[4],2)+pow(line6[5],2)-ytotal[5]),3)


PBarE = (p1**2) + (p2**2) + (p3**2) + (p4**2) + (p5**2) + (p6**2)
PBar = round(((1/6)*(a+b+c+d+e+f)),4)

kappa = round((PBar - PBarE)/(1 - PBarE),4)

print(kappa)
