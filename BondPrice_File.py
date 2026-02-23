

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy                     
    coupon = face * couponRate / ppy
    bondPrice = 0
    for t in range(1, n + 1):
        pv = coupon / (1 + y / ppy) ** t
        bondPrice += pv
    bondPrice += face / (1 + y / ppy) ** n
    return bondPrice