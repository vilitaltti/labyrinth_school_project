from stack import Stack
import unittest

class TestStack(unittest.TestCase):

    def test_top_and_push(self):
        tmp = Stack()
        self.assertEqual(tmp.top(),None)
        tmp.push("test")
        self.assertEqual(tmp.top(),"test")
        self.assertEqual(tmp.list.head.get_data(),"test")


    def test_pop(self):
        tmp = Stack()
        tmp.push(1)
        tmp.push(2)
        self.assertEqual(tmp.pop(),2)
        self.assertEqual(tmp.pop(),1)

    def test_is_empty(self):
        tmp = Stack()
        self.assertTrue(tmp.is_empty())
        tmp.push(1)
        self.assertFalse(tmp.is_empty())

if __name__ == '__main__':
    unittest.main()
