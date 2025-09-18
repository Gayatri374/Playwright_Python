try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Always runs")



try:
    a=12/0
except ZeroDivisionError:
    print('na')
finally:
    print('mm')