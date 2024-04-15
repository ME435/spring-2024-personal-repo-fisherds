print("Learning about lambda")

def def_func():
    print("Line one")
    print("Line two")


def_func()
print(type(def_func))

def_lambda = lambda : print("Lambda function")
def_lambda2 = lambda a, b: print("Lambda function", a, b)


def_lambda()
print(type(def_lambda))

def_lambda2("Dave", "Fisher")


def my_real_function(a, b):
    print("Hello", a)
    print("Hello", b)

callback = lambda : my_real_function("Dave", "Fisher")

callback()
