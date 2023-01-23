def is_leap_year(year=1):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


target = 2000
print(f'Is {target} leap year? {is_leap_year(target)}')

target = 2002
print(f'Is {target} leap year? {is_leap_year(target)}')

target = 2004
print(f'Is {target} leap year? {is_leap_year(target)}')