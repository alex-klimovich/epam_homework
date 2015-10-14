class API(object):
    def __init__(self):
        self.func_doc = {}

    def __get__(self, instance, owner):
        for inst in (instance, owner):
            if inst is None:
                continue
            for meth in inst.__dict__:
                if not meth.startswith('_'):
                    if callable(meth):
                        self.func_doc[meth] = inst.__dict__[meth].__doc__
                    else:
                        self.func_doc[meth] = type(inst.__dict__[meth]).__name__
        return '\n'.join([(k + ' : ' + v) for k, v in self.func_doc.items()])


class Foo(object):
    __doc__ = API()

    def __init__(self, x):
        self.x = x

    def meth(self, y):
        """Multiplies two values self.x and y."""
        return self.x * y


print Foo.__doc__
foo = Foo(10)
print foo.__doc__
