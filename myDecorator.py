def greet(fx):
    def mfx(*args, **kwargs):
        print("Hello!!! You are using this function.")
        fx(*args, **kwargs)
        print("Thanks you for using this function")

    return mfx;


@greet
def Hello():
    print("Hello World")


def add(a, b):
    print(a + b)


def name():
    print("Hii My name is Akash")


Hello()

greet(name)()

greet(add)(3, 4)
