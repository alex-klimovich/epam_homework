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


man = Man('Yury')
# I cannot sing!
man.sing()
# Traceback (most recent call last):
#   File "...", line 20, in <module>
#     man.sing()
# AttributeError: 'Man' object has no attribute 'sing'
Singner = Man.make_with_mixin(SingMixin)
pavel = Singner("Pavel")
pavel.sing()
# man: La la li la, la la la!
# ------------------------------------------------------------------------------
