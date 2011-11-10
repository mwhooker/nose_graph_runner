from unittest import TestCase

class Test(TestCase):

    def test_first(self):
        self.assertTrue(True)


class TestA(TestCase):

    def pre(self):
        self.foo = True

    def post(self):
        pass


class TestB(TestCase):

    def pre(self):
        self.bar = True
        pass

    def post(self):
        pass


class TestC(TestCase):

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
