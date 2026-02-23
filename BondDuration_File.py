
def getBondDuration(y, face, couponRate, m, ppy=1):

    n = m * ppy
    coupon = face * couponRate / ppy
    bondPrice = 0
    weightedPV = 0
    for t in range(1, n + 1):
        cf = coupon
        if t == n:
            cf += face
        pv = cf / (1 + y/ppy)**t
        bondPrice += pv
        weightedPV += t * pv
    duration = weightedPV / bondPrice
    duration = duration / ppy
    return duration