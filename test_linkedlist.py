import unittest

from linkedlist import LinkedList
from linkedlist import LinkedListCell


class TestLinkedList(unittest.TestCase):
    
    def test_cell(self):
        tmp = LinkedListCell(1)
        self.assertEqual(tmp.get_data(),1)
        self.assertEqual(tmp.get_next(),None)
        self.assertEqual(tmp.get_previous(),None)
    
    def test_add_first(self):
        list1 = LinkedList()
        list1.add_first('b')
        self.assertEqual(list1.head.get_data(),'b')
        self.assertEqual(list1.tail.get_data(),'b')
        list1.add_first('a')
        self.assertEqual(list1.head.get_data(),'a')
        self.assertEqual(list1.tail.get_data(),'b')
        self.assertEqual(list1.head.get_next(),list1.tail)
        self.assertEqual(list1.tail.get_previous(),list1.head)
        self.assertEqual(list1.head.get_previous(),None)
        self.assertEqual(list1.tail.get_next(),None)

    def test_add_last(self):
        list1 = LinkedList()
        list1.add_last('a')
        self.assertEqual(list1.head.get_data(),'a')
        self.assertEqual(list1.tail.get_data(),'a')
        list1.add_last('b')
        self.assertEqual(list1.head.get_data(),'a')
        self.assertEqual(list1.tail.get_data(),'b')
        self.assertEqual(list1.head.get_next(),list1.tail)
        self.assertEqual(list1.tail.get_previous(),list1.head)
        self.assertEqual(list1.head.get_previous(),None)
        self.assertEqual(list1.tail.get_next(),None)
        

    def test_remove(self):
        list1 = LinkedList()
        list1.add_last('a')
        list1.add_last('b')
        list1.add_last('c')
        # a b c 
        self.assertEqual(list1.remove('a').get_data(),'a')
        self.assertEqual(list1.remove('a'),None)
        # b c 
        self.assertEqual(list1.head.get_data(),'b')
        self.assertEqual(list1.tail.get_data(),'c')
        self.assertEqual(list1.head.get_previous(),None)

        self.assertEqual(list1.remove('c').get_data(),'c')
        # b 
        self.assertEqual(list1.head.get_data(),'b')
        self.assertEqual(list1.tail.get_data(),'b')
        self.assertEqual(list1.head.get_previous(),None)
        self.assertEqual(list1.head.get_next(),None)

        list1.add_last('c')
        list1.add_first('a')
        # a b c 
        self.assertEqual(list1.remove('b').get_data(),'b')
        # a c 
        self.assertEqual(list1.head.get_data(),'a')
        self.assertEqual(list1.tail.get_data(),'c')
        self.assertEqual(list1.head.get_next(),list1.tail)
        self.assertEqual(list1.tail.get_previous(),list1.head)

if __name__ == '__main__':
    unittest.main()
