from functools import wraps, partial
from operator import add, iadd


# decorator approach
def add_factory(x):
    """
    >>> add5 = add_factory(5)
    >>> print add5(10)
    15
    >>> print add5.__name__
    add_factory
    """

    @wraps(add_factory)
    def wrapper(y):
        return x + y

    return wrapper


# partial apply approach
def add_factory_2(x):
    """
    >>> add5 = add_factory_2(5)
    >>> print add5(10)
    15
    """

    return partial(add, x)


# closure approach
def add_factory_3(x):
    """
    >>> add5 = add_factory_3(5)
    >>> print add5(10)
    15
    """

    l = [x]

    def wrapper(y):
        l.append(y)
        return sum(l)

    return wrapper


# using lambda
def add_factory_4(x):
    """
    >>> add5 = add_factory_4(5)
    >>> print add5(10)
    15
    """
    return lambda y: x + y


# using classes
class add_factory_5(object):
    """
    >>> add5 = add_factory_5(5)
    >>> print add5(10)
    15
    """

    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        return self.x + y


def coroutine(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator

    return wrapper


# using generators / coroutines
@coroutine
def add_factory_6(x):
    """
    >>> add5 = add_factory_6(5)
    >>> print add5.send(10)
    15
    """

    yield iadd(x, (yield))
