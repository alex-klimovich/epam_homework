import unittest


class LinterMeta(type):
    # def __new__(mcl, name, bases, nmspc):
    #     for meth_name, meth in nmspc.iteritems():
    #         if not meth_name.startswith('_') and callable(meth):
    #             if not hasattr(meth, '__doc__') or not meth.__doc__:
    #                 raise AttributeError("'%s' has no documentation sting." % meth_name)
    #
    #     return type.__new__(mcl, name, bases, nmspc)

    def __call__(cls, *args, **kwargs):
        for meth_name in cls.__dict__:
            meth = getattr(cls, meth_name)
            if not meth_name.startswith('_') and callable(meth):
                if not hasattr(meth, '__doc__') or not meth.__doc__:
                    raise AttributeError("'%s' has no documentation sting." % meth_name)
        return super(LinterMeta, cls).__call__(*args, **kwargs)


class Creature(object):
    __metaclass__ = LinterMeta

    def __init__(self, genus):
        self.genus = genus

    def sound(self, msg):
        print "{0}: {1}".format(self.genus, msg)


class TestLinterMeta(unittest.TestCase):
    def test_doc_string(self):
        with self.assertRaises(AttributeError) as ex:
            Creature('man')
        self.assertEqual(ex.exception.message, "'sound' has no documentation sting.")
