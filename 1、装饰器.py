# __author__: xws    
# time: 2019/9/3 12:32


# 1、装饰器
import functools


def auth(func):
    # @functools.wraps(func)
    def inner(*args,**kwargs):
        print("前")
        ret=func(*args,**kwargs)
        print("后")
        return ret
    return inner


@auth
def index():
    print("index")


# 打印函数名
print(index.__name__)



# print(index)
# 没使用装饰器
# <function index at 0x000001DC81ABE9D8>

# 使用装饰器后
# <function auth.<locals>.inner at 0x000002E78504EA60>


# 2、endpoint 默认是函数名

# 3、装饰器的先后顺序
