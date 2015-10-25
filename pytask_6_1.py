from types import MethodType


class Creature(object):
    def __init__(self, genus):
        self.genus = genus

    def sound(self, msg):
        print "{0}: {1}".format(self.genus, msg)


class Man(Creature):
    def __init__(self, name):
        super(Man, self).__init__("man")
        self.name = name


class SingMixin(object):
    def sing(self):
        self.sound('La la li la, la la la!')


# --- my code begin ---
def make_with_mixin(self, Class):
    if not hasattr(self, 'sing'):
        print 'I cannot sing!'
    return type('', (Class, self), {})


Man.make_with_mixin = MethodType(make_with_mixin, Man)
# --- my code end ---

man = Man('Yury')
# I cannot sing!

"""
>>> man.sing()
Traceback (most recent call last):
  File "...", line 20, in <module>
    man.sing()
AttributeError: 'Man' object has no attribute 'sing'
"""

Singer = Man.make_with_mixin(SingMixin)
pavel = Singer("Pavel")
pavel.sing()
# man: La la li la, la la la!
