from unittest import TestCase

class TestNode(TestCase):

    methods = ('pre', 'post')
    def __init__(self, method):

        super(TestNode, self).__init__(method)

    def __call__(self, *args, **kwargs):
        print "__call__"

        super(TestNode, self).__call__(*args, **kwargs)

    def pre(self, **kwargs):
        raise NotImplementedError

    def post(self):
        raise NotImplementedError

class Test(TestNode):

    def test_first(self):
        self.assertTrue(True)


class TestA(TestNode):

    def pre(self):
        self.foo = True

    def post(self):
        pass


class TestB(TestNode):

    def pre(self):
        self.bar = True
        pass

    def post(self):
        pass


class TestC(TestNode):

    depends = {
        'a': TestA,
        'b': TestB
    }

    def pre(self, a, b):
        self.assertTrue(isinstance(a, TestA))
        self.assertTrue(isinstance(b, TestB))
        self.assertTrue(a.foo)
        self.assertTrue(b.bar)

    def post(self):
        pass
