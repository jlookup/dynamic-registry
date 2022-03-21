
# actions = {
#     "get": {},
# }

# def class_register(cls):
#     cls._propdict = {}
#     for methodname in dir(cls):
#         method = getattr(cls, methodname)
#         if hasattr(method, '_prop'):
#             cls._propdict.update(
#                 {cls.__name__ + '.' + methodname: method._prop})
#         if hasattr(method, '_action'):
#             for action in getattr(method, '_action'):
#                 actions[action].update({cls: method})
           
#     return cls

# def register_action(*args):
#     def wrapper(func):
#         func._action = args
#         return func
#     return wrapper

# def register(*args):
#     def wrapper(func):
#         func._prop = args
#         return func
#     return wrapper

# def register_action(*args):
#     def wrapper(func):
#         func._action = args
#         return func
#     return wrapper

# @class_register
# class MyClass(object):

#     @register('actions')
#     @register_action('get')
#     def get_file(self, arg1, arg2):
#         pass

#     @register('prop3', 'prop4')
#     def connect(self, arg1, arg2):
#         pass

# myclass = MyClass()
# print(myclass._propdict)
# print(actions)
# _ = ''
# # {'MyClass.my_other_method': ('prop3', 'prop4'), 'MyClass.my_method': ('prop1', 'prop2')}





from abc import ABC, abstractmethod

actions = {
    "connect": {},
    "navigate": {},
    "get": {},
}

class Actions:

    def __init__(self):
        self.connect = {}
        self.navigate = {}
        self.get = {}

actions_ = Actions()

def class_register(cls):
    """
    Add a method of a class to the action dict in the actions registry.

    Methods must be tagged with `_action` attr. 
    Value of `_action` is the name of the action dict.
    Use `@register_action` to tag methods.
    """
    cls._propdict = {}
    for methodname in dir(cls):
        method = getattr(cls, methodname)
        if hasattr(method, '_action'):
            for action in getattr(method, '_action'):
                actions[action].update({cls: method})
                getattr(actions_, action)[cls] = method
        # if hasattr(method, '_prop'):
        #     cls._propdict.update(
        #         {cls.__name__ + '.' + methodname: method._prop})  

    return cls
    
def register_action(*args):
    """
    Add a method of a class to the an action dict in the actions registry.

    Class must be decorated with `@class_register`.
    `@class_register` does the actual registration.
    This decorator tags the method with an `_action` attr
    so that it can be recognized by `@class_register`.

    Usage:
        if method name is the same as action name:
           `@register_action()`
        if not:
           `@register_action('action_name')`
    """
    def wrapper(func):
        if args:
            func._action = args
        else:
            func._action = (func.__name__,)
        return func
    return wrapper


class TransferJob:
    
    def __init__(self, db_connection, job_steps):
        self.db_connection = db_connection
        self.job_steps = job_steps

    def get_auth_string(self, auth_id):
        return self.db_connection.execute("sp_get_auth_string", auth_id)


class TransferJobStep:

    def __init__(self, transfer_job, subject, action, object, output, auth_id):
        self.transfer_job = transfer_job
        self.subject = subjects[subject](self, auth_id)
        self.action = self.subject.actions[action] 
        self.object = object
        self.output = output 


class Filesystem(ABC):

    def __init__(self, job_step, auth_id):
        self.job_step = job_step
        self.auth_id = auth_id
        self.auth_string = self.get_auth_string(auth_id)

    def get_auth_string(self):
        return self.job_step.transfer_job.get_auth_string(self.auth_id)

    @abstractmethod
    def connect(self): ... 

    @abstractmethod
    def navigate(self): ...

    @abstractmethod
    def get_file(self): ...


@class_register        
class FilesystemSharepoint(Filesystem):

    def __init__(self, job_step, auth_id):
        self.job_step = job_step
        self.auth_id = auth_id
        # self.auth_string = self.get_auth_string(auth_id)

    def _get_auth_string(self):
        return self.job_step.parent.get_auth_string(self.auth_id)

    @register_action('connect')
    def connect(self):
        if self.auth_string is None:
            self.auth_string = self.get_auth_string()
        
        # custom code for each file system here

    @register_action()
    def navigate(self):
        pass

    @register_action('get')
    def get_file(self, file_name):
        return ('got it')


s = FilesystemSharepoint('step1', 1)
print(actions)
print(actions_.get)

_ = ''








