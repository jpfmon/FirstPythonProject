

def decorator1(function):
    print("Hello")
    def wrap():
        print("Before function")
        function()
        print("After function")
    return wrap

# @decorator1
def myfunc():
    print("This is my function")


print(1)
wrap = decorator1(myfunc)
print("2")
wrap()
print("3")
myfunc()