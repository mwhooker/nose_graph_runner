import gevent

from nose.plugins import Plugin
from nose import suite
from topsort import topsort_levels
from unittest import TestCase



class GraphRunner(Plugin):
    name = 'graphrunner'

    def wantMethod(self, method):
        if method.__name__ in ('pre', 'post'):
            return True

    def prepareTest(self, test):

        def find_tests(tests):

            for t in tests:
                if type(t.context) == type(TestCase) \
                   and issubclass(t.context, TestCase):
                    yield t
                else:
                    for t2 in find_tests(t):
                        yield t2

        tests = list(find_tests(test))
        graph_tests = [test for test in tests if 
                       hasattr(test.context, 'pre') and
                       hasattr(test.context, 'post')]
        normal_tests = set(tests) - set(graph_tests)

        """
        test_order = {}
        for x in graph_tests[0]:
            test_order[x.test._testMethodName] = x
        run_order = (test_order['pre'], test_order['post'])

        return suite.ContextSuite(run_order)
        """

        return suite.ContextSuite(normal_tests + [self.order_tests(graph_tests)])
    
    def order_tests(self, tests):
        dependency_pairs = []

        for klass in classes:
            if not len(klass.depends):
                dependency_pairs.append((None, klass))
                continue
            for key in klass.depends:
                dependency_pairs.append((klass.depends[key], klass))

        self.run_levels = filter(all, topsort_levels(dependency_pairs))
        pass
