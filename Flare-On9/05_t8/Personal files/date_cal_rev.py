# Decompiled version (modified) of some_math_calculation() @ 0x00404570

import math

year = 2000

while True:
    day = 4
    month = 10

    year_final = year - 1
    if month > 2:
        year_final = year
    v4 = month + 12
    if month > 2:
        v4 = month

    systemtime_12 = (int(year_final//100//4 + day + int((year_final + 4716) * 365.25) - int(int(v4 + 1) * -30.6001) - year_final//100 + 2) - 1524.5 - 2451549.5) / 29.53
    v5 = math.floor(systemtime_12)
    result = int(round((systemtime_12 - v5) * 29.53))
    # print((systemtime_12 - v5) * 29.53)
    # print(result)

    if result == 0xF:
        print("Year: " + str(year))
        break
    else:
        year += 1