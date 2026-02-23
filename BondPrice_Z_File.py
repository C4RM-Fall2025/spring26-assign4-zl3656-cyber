

def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    bondPrice = 0
    for t, y in zip(times, yc):
        if t == times[-1]:
            cashflow = coupon + face
        else:
            cashflow = coupon
        pv = cashflow / (1 + y)**t
        bondPrice += pv
    return bondPrice