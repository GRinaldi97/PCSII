def is_leap(year):
    1900<=year<=(10**5)
    leap = False
    if year%4==0:
        if year%100!=0:
            leap=True
        else:
            leap=False
        if year%100==0 and year%400!=0:
            leap=False
        else: leap=True
        return leap
    else:
        leap=False
    return leap
