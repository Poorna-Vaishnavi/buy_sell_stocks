def buy_sell(price):
    maxi=0
    for i in range(0,len(price)):
        for j in range(i+1,len(price)):
            remainder=price[j]-price[i]
            if remainder>maxi:
                maxi=remainder

    return maxi
price=(list(map(int,input().split()))) 
print(buy_sell(price))             