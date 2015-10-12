class Fake(object):
    """
    >>> fake = Fake()
    >>> fake.non_existing_method('asdfa')
    >>> fake.attribute
    >>> fake[4]
    >>> fake['non existing key']
    >>> fake2 = fake.blablabla()
    >>> fake2.some_name()
    >>> fake2.whatever.again_whatever().and_again['yury'][1]
    """
    pass
