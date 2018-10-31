def commission_cal(pLock,pStock,pBarrel):
    sumPrice = 0
    commission = 0.0
    checkQuantity = True
    lock = 45
    stock = 30
    barrel = 25

    pLock = int(pLock)
    pStock = int(pStock)
    pBarrel = int(pBarrel)

    if pLock < 70 :
        sumPrice = sumPrice + (pLock*lock)
    else :
        checkQuantity = False

    if pStock < 80 :
        sumPrice = sumPrice + (pStock*stock)
    else:
        checkQuantity = False

    if pBarrel < 90:
        sumPrice = sumPrice + (pBarrel*barrel)
    else:
        checkQuantity = False

    if sumPrice > 1000 :
        sumPrice = sumPrice - 1000
        commission = commission + ((1000/100)*10)
        if sumPrice > 800 :
            sumPrice = sumPrice - 800
            commission = commission + ((800/100)*15)
            commission = commission + ((sumPrice/100)*20)
        else:
            commission = commission + ((sumPrice/100)*15)
    else:
        commission = commission + ((sumPrice/100)*10)

    if checkQuantity == True :
        return (str(commission))
    else :
        return "invalid"
