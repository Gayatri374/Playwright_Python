def my_deco(func):
    def wrapper():
        print('checking loggin in')
        login_in=True
        if login_in:
            func()
        else:
            print('access denied')
    return wrapper

@my_deco
def yes():
    print('user')

yes()