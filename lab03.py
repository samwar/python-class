__author__ = 'samu6978'

x = 4
print x
print int(5)
y = [1,2,3]
print y.count(3)
y.index(1)

foo = {1:'foo', 2:'bar', 3:'baz'}
for x in foo.iteritems():
    print x
print y
y.extend([4,5])
print y
y.append([4,5])
print y

z = "foo"
# z.ap("bar")
# z.ex
z += "bar"
print z