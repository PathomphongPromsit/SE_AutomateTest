def commission_cal(pLock,pStock,pBarrel):
    sumPrice = 0.0
    commission = 0.0
    checkQuantity = True
    lock = 45.0
    stock = 30.0
    barrel = 25.0

    pLock = int(pLock)
    pStock = int(pStock)
    pBarrel = int(pBarrel)

    if pLock <= 70.0 :
        sumPrice = sumPrice + (pLock*lock)
    else :
        checkQuantity = False

    if pStock <= 80.0 :
        sumPrice = sumPrice + (pStock*stock)
    else:
        checkQuantity = False

    if pBarrel <= 90.0:
        sumPrice = sumPrice + (pBarrel*barrel)
    else:
        checkQuantity = False

    if sumPrice > 1000.0 :
        sumPrice = sumPrice - 1000.0
        commission = commission + ((1000.0/100.0)*10.0)
        if sumPrice > 800.0 :
            sumPrice = sumPrice - 800.0
            commission = commission + ((800.0/100.0)*15.0)
            commission = commission + ((sumPrice/100.0)*20.0)
        else:
            commission = commission + ((sumPrice/100.0)*15.0)
    else:
        commission = commission + ((sumPrice/100.0)*10.0)

    if checkQuantity == True :
        return (str(commission))
    else :
        return "invalid"
