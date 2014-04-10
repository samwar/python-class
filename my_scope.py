__author__ = 'samu6978'

my_x = 3


def my_fun():
    my_x = 33
    return my_x


print my_x
print my_fun()


def deco(fn):
    def deco1(fn1):
        print fn1()
    return deco1(fn)


print "deco globals:" + str(deco(globals()))
print "deco locals:" + str(deco(locals()))
print "deco my_fun: " + str(deco(my_fun()))
