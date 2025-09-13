def my_deco(func):
    def wrapper():
        print('before')
        func()
        print('after')
    return wrapper

@my_deco
def hell():
    print('hello')

hell()
