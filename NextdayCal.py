def cal_leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def cal_next_day(m, d, y):

    M = int(m)
    D = int(d)
    Y = int(y)
    ND = 0
    NM = 0
    NY = 0

    if M < 1 or M >12 or D < 1 or D > 31 or Y < 1812 or Y > 2012:
        return "incorrect"

    else:
        if M == 1:
            if D > 31:
                return "incorrect"
            if D == 31:
                ND = 1
                NM = 2
                NY = Y
            else:
                ND = D+1
                NM = M
                NY = Y
        elif M == 2:
            if cal_leap(Y):
                if D > 29:
                    return "incorrect"
                if D == 29:
                    ND = 1
                    NM = 3
                    NY = Y
                else:
                    ND = D+1
                    NM = M
                    NY = Y
            else:
                if D > 28:
                    return "incorrect"
                if D == 28:
                    ND = 1
                    NM = 3
                    NY = Y
                else:
                    ND = D+1
                    NM = M
                    NY = Y
        elif M == 3:
            if D > 31:
                return "incorrect"
            if D == 31:
                ND = 1
                NM = 4
                NY = Y
            else:
                ND = D+1
                NM = M
                NY = Y
        elif M == 4:
            if D > 30:
                return "incorrect"
            if D == 30:
                ND = 1
                NM = 5
                NY = Y
            else:
                ND = D+1
                NM = M
                NY = Y
        elif M == 5:
            if D > 31:
                return "incorrect"
            if D == 31:
                ND = 1
                NM = 6
                NY = Y
            else:
                ND = D+1
                NM = M
                NY = Y
        elif M == 6:
            if D > 30:
                return "incorrect"
            if D == 30:
                ND = 1
                NM = 7
                NY = Y
            else:
                ND = D+1
                NM = M
                NY = Y
        elif M == 7:
            if D > 31:
                return "incorrect"
            if D == 31:
                ND = 1
                NM = 8
                NY = Y
            else:
                ND = D+1
                NM = M
                NY = Y
        elif M == 8:
            if D > 31:
                return "incorrect"
            if D == 31:
                ND = 1
                NM = 9
                NY = Y
            else:
                ND = D+1
                NM = M
                NY = Y
        elif M == 9:
            if D > 30:
                return "incorrect"
            if D == 30:
                ND = 1
                NM = 10
                NY = Y
            else:
                ND = D+1
                NM = M
                NY = Y
        elif M == 10:
            if D > 31:
                return "incorrect"
            if D == 31:
                ND = 1
                NM = 11
                NY = Y
            else:
                ND = D+1
                NM = M
                NY = Y
        elif M == 11:
            if D > 30:
                return "incorrect"
            if D == 30:
                ND = 1
                NM = 12
                NY = Y
            else:
                ND = D+1
                NM = M
                NY = Y
        elif M == 12:
            if D > 31:
                return "incorrect"
            if D == 31:
                ND = 1
                NM = 1
                NY = Y+1
            else:
                ND = D+1
                NM = M
                NY = Y
    ans = str(NM)+str(ND)+str(NY)
    return (ans)