

def getBondPrice(face, couponRate, m, yc):
    coupon = face * couponRate
    bondPrice = 0
    for t, y in enumerate(yc, start=1):
        if t == m:
            cashflow = coupon + face
        else:
            cashflow = coupon
        pv = cashflow / (1 + y)**t
        bondPrice += pv
    return bondPrice