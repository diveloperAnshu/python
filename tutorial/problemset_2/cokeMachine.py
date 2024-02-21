money=50
while money >=0:
    print(f"Amount Due: {money}")
    temp=int(input("Insert Coin: "))
    if temp==25 or temp==10 or temp==5:
        money=money-temp
    if money<=0:
        print(f"Change Owed: {abs(money)}")
        break
