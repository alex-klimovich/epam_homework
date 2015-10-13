class Fake(object):
    def __call__(self, *args, **kwargs):
        return self

    def __getattr__(self, item):
        return self

    def __getitem__(self, item):
        return self


fake = Fake()
fake.non_existing_method('asdfa')
fake.attribute
fake[4]
fake['non existing key']
fake2 = fake.blablabla()
fake2.some_name()
fake2.whatever.again_whatever().and_again['yury'][1]
