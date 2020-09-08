# def foo1(foo=0):
#     print(foo)
#     foo += 1
#     print(foo)
#
# foo1()
#
# foo1()
#
# foo1(2)
#
# foo1()


# def foo2(foo=None):
#     if foo is None:
#         foo = []
#     print(foo)
#     foo.append(len(foo))
#     print(foo)
# f = []
# foo2()
#
# foo2()
#
# foo2(f)
#
# foo2()


# a = [1,2,3,4,5]
# b = ["uno","dos","tres","cuatro","cinco"]
# iterator = zip(a,b)
#
# print(list(iterator))
# for sample in iterator:
#     print("{:d} = {:s}".format(sample[0],sample[1]))
