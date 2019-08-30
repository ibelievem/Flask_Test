class Foo(object):

    def __init__(self):
        print('sdfsdf')

    def __call__(self, *args, **kwargs):
        print('call')


# 执行init方法
obj = Foo()
# 执行call方法
obj()
