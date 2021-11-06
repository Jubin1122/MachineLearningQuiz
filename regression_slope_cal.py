'''
Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15

Compute the slope of the line of regression obtained 
while treating Physics as the independent variable. 
Compute the answer correct to three decimal places.

'''

# Using numpy module
'''
import numpy as np

def slope_cal(x,y):
    xs = np.array(x, dtype=np.float64)
    ys = np.array(y, dtype=np.float64)

    x_mean = xs.mean()
    y_mean = ys.mean()

    b1_num = ((xs - x_mean) * (ys - y_mean)).sum()
    b1_den = ((xs-x_mean)**2).sum()

    b1 = b1_num/b1_den

    bo = y_mean -(b1*x_mean)

    reg_line = 'y = {} + β{}'.format(bo, round(b1,3))

    return reg_line
'''
# Without numpy module

def slope_cal(x,y):
    x_mean = sum(x)/len(x)
    y_mean = sum(y)/len(y)

    x = [round(a-x_mean,3) for a in x]
    y = [round(a-y_mean,3) for a in y]

    b1_num = sum([x*y for x,y in zip(x,y)])
    b1_den = sum([a**2 for a in x])

    b1 = b1_num/b1_den
    

    return round(b1,3)


x = [15,12,8,8,7,7,7,6,5,3]
y = [10,25,17,11,13,17,20,13,9,15]
print(slope_cal(x,y))