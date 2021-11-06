# Stock Predictions

'''
Input Format

The input of each turn will consist of multiple lines. All money values are doubles to two decimal places, all other numbers are integers.

The first line contains three space separated numbers m k d.

m - the amount of money you could spend that day.
k - the number of different stocks available for buying or selling.
d - the number of remaining days for trading stocks.
k lines follow, each in the following format: name owned prices

name - the name of the stock (a string).
owned - the number of shares you own of that stock.
prices - 5 space separated numbers representing the stock's price for the last 5 days. These are ordered from oldest to newest, so the last number is the current stock price.

Output Format

The output for each turn should also contain multiple lines:

Output N for the number of transactions you wish to make. Output 0 if you are not making any transactions that day.

If you are making transactions, output N lines containing the name of the stock (case sensitive), BUY or SELL, and the number of shares you wish to buy or sell.

Sample Input

90 2 400
iStreet 10 4.54 5.53 6.56 5.54 7.60
HR 0 30.54 27.53 24.42 20.11 17.50
Sample Output

2
iStreet SELL 10
HR BUY 5

'''

import numpy as np
import math
def printTransactions(m, k, d, name, owned, prices):
    slope_list=[]
    for i in range(k):
        x=np.array([1.0,2.0,3.0,4.0,5.0])
        y= np.array(prices[i])
        A = np.vstack([x, np.ones(len(x))]).T
        slope, constat = np.linalg.lstsq(A, y)[0]
        slope_list.append(slope)
        
    sort_slope = sorted(slope_list)
    amount_remaining= m
    trans={}
    for j in reversed(range(k)):
        index_slope = slope_list.index(sort_slope[j])
        if sort_slope[j]<=0 and amount_remaining>=prices[index_slope][-1]:
            #print prices[index_slope][-1]
            num_stock =math.floor(amount_remaining/prices[index_slope][-1])
            amount_remaining = amount_remaining - prices[index_slope][-1]*num_stock
            trans[name[index_slope]] = names[index_slope]+' BUY ' + str(int(num_stock))
            
        
    for j in range(k):
        index_slope = slope_list.index(sort_slope[j])
        if sort_slope[j]>0 and owned[index_slope]>0:
            trans[name[index_slope]] = names[index_slope]+' SELL ' + str(owned[index_slope]) 
            
    print(len(trans.keys()))
    for x in trans:
        print(trans[x])
        
if __name__ == '__main__':
    m, k, d = [float(i) for i in input().strip().split()]
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for data in range(k):
        temp = input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])

    printTransactions(m, k, d, names, owned, prices)

