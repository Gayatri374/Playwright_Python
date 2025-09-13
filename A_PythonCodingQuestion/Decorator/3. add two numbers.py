def add_num(func):
    def wrapper(a,b):
        print('adding')
        result=func(a,b)
        print(f'Result {result}')
        return result
    return wrapper


@add_num
def add(x,y):
    return x+y

add(10,23)