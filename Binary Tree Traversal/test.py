import codewars_test as test
from main import pre_order, in_order, post_order, Node

@test.describe('Example Tests')
def example_tests():

    a = Node(5)
    b = Node(10)
    c = Node(2)
    d = Node("leaf")
    a.left = b
    a.right = c
    c.left = d

    @test.it('Pre-order Tests')
    def pre_order_tests():
        test.assert_equals(pre_order(a), [a.data, b.data, c.data, d.data])
        test.assert_equals(pre_order(b), [b.data])
        test.assert_equals(pre_order(c), [c.data, d.data])

    @test.it('In-order Tests')
    def in_order_tests():
        test.assert_equals(in_order(a), [b.data, a.data, d.data, c.data])
        test.assert_equals(in_order(b), [b.data])
        test.assert_equals(in_order(c), [d.data, c.data])

    @test.it('Post-order Tests')
    def post_order_tests():
        test.assert_equals(post_order(a), [b.data, d.data, c.data, a.data])
        test.assert_equals(post_order(b), [b.data])
        test.assert_equals(post_order(c), [d.data, c.data])

    @test.it('Empty Node Tests')
    def None_tests():
        test.assert_equals(pre_order(None), [])
        test.assert_equals(in_order(None), [])
        test.assert_equals(post_order(None), [])


