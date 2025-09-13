def access_decorator(func):
    def wrapper(name,role):
        print(f'Welcome {name}! as an {role}')
        return func(name,role)
    return wrapper



@access_decorator
def show_acces(name,role):
    return f"Access granted for {name} with {role}"

print(show_acces('Gayatri','QA'))
print(show_acces('Pavan','Marketing'))
