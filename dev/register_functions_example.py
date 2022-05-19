

def tag(tags):
    """
    Add attrs to a function
    compile-time decorator
    """
    def wrapper(func):
        # if args:
        #     func._action = args
        # else:
        #     func._action = (func.__name__,)
        # if hasattr(func, 'runcount'):
        #     func.runcount += 1
        for key, val in tags.items():
            setattr(func, key, val)
        return func

    return wrapper

# def keepcount(func):
#     """
#     Count how many times the function has been called
#     must be tagged with 'runcount' attribute/
#     runtime decorator
#     """
#     def count(*args, **kwargs):
#         func.runcount += 1
#         func(*args, **kwargs)
#     return count 


# @keepcount
@tag({'tag': 'thisistheone', 'runcount': 0})
def hello(name='world'):
    print(f"hello {name}")
hello.runcount = 0

try:
    print(hello.tag)
    print(hello.runcount)
except:
    pass

hello('jason')
print(hello.runcount)
hello('chad')
print(hello.runcount)
hello('world')
