

def getBondPrice_E(face, couponRate, yc):
    coupon = face * couponRate
    bondPrice = 0
    m = len(yc)
    for t, y in enumerate(yc, start=1):
        cashflow = coupon + face if t == m else coupon
        bondPrice += cashflow / (1 + y) ** t
    return bondPrice