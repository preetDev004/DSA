#
#   Author: Catherine Leung
#   These are the unit tests for functions and classes of assingment 1 Part B
#   To use this, run: python test_a1_partb.py

import unittest
from a1_partb import SortedList

class A1BTestCase(unittest.TestCase):
    """These are the test cases for functions and classes of a1"""
    
    def test_init_get_len_empty(self):
        my_list = SortedList()
        self.assertEqual(len(my_list), 0)
        self.assertEqual(my_list.is_empty(), True)
        self.assertEqual(my_list.get_front(), None)
        self.assertEqual(my_list.get_back(), None)
 
    def test_insert(self):
        my_list = SortedList()
        nn = my_list.insert(10)
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 1)
        self.assertNotEqual(my_list.get_front(), None)
        self.assertNotEqual(my_list.get_back(), None)
        self.assertEqual(my_list.get_front().get_data(), 10)
        self.assertEqual(my_list.get_back().get_data(), 10)
        self.assertEqual(nn.get_data(), 10)

        nn = my_list.insert(5)
        self.assertEqual(nn.get_data(), 5)
        self.assertEqual(nn.get_next().get_data(), 10)
        self.assertEqual(nn.get_next().get_previous(), nn)
        self.assertEqual(len(my_list), 2)
        self.assertEqual(my_list.get_front().get_data(), 5)
        self.assertEqual(my_list.get_back().get_data(), 10)
        self.assertEqual(nn.get_next().get_data(), 10)
        self.assertEqual(my_list.get_back().get_previous(), nn)


        nn = my_list.insert(15)
        self.assertEqual(len(my_list), 3)
        self.assertEqual(nn.get_data(), 15)
        self.assertEqual(nn.get_previous().get_data(), 10)
        self.assertEqual(nn.get_previous().get_next(), nn)
        self.assertEqual(my_list.get_front().get_data(), 5)
        self.assertEqual(my_list.get_front().get_next().get_data(), 10)
        self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 15)
        self.assertEqual(my_list.get_back().get_data(), 15)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 10)
        self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 5)

        nn = my_list.insert(12)
        self.assertEqual(len(my_list), 4)
        self.assertEqual(nn.get_data(), 12)
        self.assertEqual(nn.get_previous().get_data(), 10)
        self.assertEqual(nn.get_previous().get_next(), nn)
        self.assertEqual(nn.get_next().get_data(), 15)
        self.assertEqual(nn.get_next().get_previous(), nn)
        self.assertEqual(my_list.get_front().get_data(), 5)
        self.assertEqual(my_list.get_front().get_next().get_data(), 10)
        self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 12)
        self.assertEqual(my_list.get_front().get_next().get_next().get_next().get_data(), 15)
        self.assertEqual(my_list.get_back().get_data(), 15)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 12)
        self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 10)
        self.assertEqual(my_list.get_back().get_previous().get_previous().get_previous().get_data(), 5)



        nn = my_list.insert(7)
        self.assertEqual(len(my_list), 5)
        self.assertEqual(nn.get_data(), 7)
        self.assertEqual(nn.get_previous().get_data(), 5)
        self.assertEqual(nn.get_previous().get_next(), nn)
        self.assertEqual(nn.get_next().get_data(), 10)
        self.assertEqual(nn.get_next().get_previous(), nn)
        self.assertEqual(my_list.get_front().get_data(), 5)
        self.assertEqual(my_list.get_front().get_next().get_data(), 7)
        self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 10)
        self.assertEqual(my_list.get_back().get_data(), 15)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 12)
        self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 10)
        self.assertEqual(my_list.get_back().get_previous().get_previous().get_previous().get_data(), 7)

        my_data = [4,8,6,7,1,3,5,10,15,2,9]
        my_data2 = ["orange", "apple", "cherry", "banana", "mango","pear","plum"]

        first_list = SortedList()
        second_list = SortedList()

        for i in my_data:
            first_list.insert(i)

        for i in my_data2:
            second_list.insert(i)

        my_data.sort()
        my_data2.sort()
        curr = first_list.get_front()
        for i in my_data:
            self.assertNotEqual(curr,None)
            self.assertEqual(i,curr.get_data())
            curr = curr.get_next()

        self.assertEqual(len(first_list),len(my_data))

        curr = second_list.get_front()
        for i in my_data2:
            self.assertNotEqual(curr,None)
            self.assertEqual(i,curr.get_data())
            curr = curr.get_next()

        self.assertEqual(len(second_list),len(my_data2))

        curr = first_list.get_back()
        for i in reversed(my_data):
            self.assertNotEqual(curr,None)
            self.assertEqual(i,curr.get_data())
            curr = curr.get_previous()


        curr = second_list.get_back()
        for i in reversed(my_data2):
            self.assertNotEqual(curr,None)
            self.assertEqual(i,curr.get_data())
            curr = curr.get_previous()



    def test_erase(self):
        my_list = SortedList()

        my_data = [4,8,6,7,1, 3,5,10,15,2,9]
        for i in my_data:
            my_list.insert(i)

        my_data.sort()

        my_list.erase(my_list.get_front())
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 10)
        self.assertEqual(my_list.get_front().get_data(), 2)
        self.assertEqual(my_list.get_front().get_next().get_data(), 3)
        self.assertEqual(my_list.get_back().get_data(), 15)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 10)


        my_list.erase(my_list.get_back())
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 9)
        self.assertEqual(my_list.get_front().get_data(), 2)
        self.assertEqual(my_list.get_front().get_next().get_data(), 3)
        self.assertEqual(my_list.get_back().get_data(), 10)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 9)


        my_list.erase(my_list.get_front())
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 8)
        self.assertEqual(my_list.get_front().get_data(), 3)
        self.assertEqual(my_list.get_front().get_next().get_data(), 4)
        self.assertEqual(my_list.get_back().get_data(), 10)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 9)


        my_list.erase(my_list.get_back())
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 7)
        self.assertEqual(my_list.get_front().get_data(), 3)
        self.assertEqual(my_list.get_front().get_next().get_data(), 4)
        self.assertEqual(my_list.get_back().get_data(), 9)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 8)


        my_list.erase(my_list.get_front().get_next())
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 6)
        self.assertEqual(my_list.get_front().get_data(), 3)
        self.assertEqual(my_list.get_front().get_next().get_data(), 5)
        self.assertEqual(my_list.get_back().get_data(), 9)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 8)


        my_list.erase(my_list.get_back().get_previous())
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 5)
        self.assertEqual(my_list.get_front().get_data(), 3)
        self.assertEqual(my_list.get_front().get_next().get_data(), 5)
        self.assertEqual(my_list.get_back().get_data(), 9)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 7)


        my_data = [3,5,6,7,9]
        curr = my_list.get_front()
        for i in my_data:
            self.assertEqual(my_list.is_empty(), False)
            self.assertNotEqual(curr,None)
            self.assertEqual(i,curr.get_data())
            curr = curr.get_next()

        self.assertEqual(len(my_list),len(my_data))

        curr = my_list.get_back()
        for i in reversed(my_data):
            self.assertEqual(my_list.is_empty(), False)
            self.assertNotEqual(curr,None)
            self.assertEqual(i,curr.get_data())
            curr = curr.get_previous()



        my_list.erase(my_list.get_front().get_next())
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 4)
        self.assertEqual(my_list.get_front().get_data(), 3)
        self.assertEqual(my_list.get_front().get_next().get_data(), 6)
        self.assertEqual(my_list.get_back().get_data(), 9)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 7)



        my_list.erase(my_list.get_back().get_previous())
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 3)
        self.assertEqual(my_list.get_front().get_data(), 3)
        self.assertEqual(my_list.get_front().get_next().get_data(), 6)
        self.assertEqual(my_list.get_back().get_data(), 9)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 6)


        my_list.erase(my_list.get_front().get_next())
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 2)
        self.assertEqual(my_list.get_front().get_data(), 3)
        self.assertEqual(my_list.get_front().get_next(), my_list.get_back())
        self.assertEqual(my_list.get_back().get_data(), 9)
        self.assertEqual(my_list.get_back().get_previous(), my_list.get_front())


        my_list.erase(my_list.get_front().get_next())
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 1)
        self.assertEqual(my_list.get_front().get_data(), 3)
        self.assertEqual(my_list.get_back().get_data(), 3)


        my_list.erase(my_list.get_front())
        self.assertEqual(my_list.is_empty(), True)
        self.assertEqual(len(my_list), 0)
        self.assertEqual(my_list.get_front(), None)
        self.assertEqual(my_list.get_back(), None)


        with self.assertRaises(ValueError) as cm:
            my_list.erase(None)
        self.assertEqual(str(cm.exception), 'Cannot erase node referred to by None')






    def test_search(self):
        my_list = SortedList()
        my_data = [4,8,6,7,1, 3,5,10,15,2,9]
        for i in my_data:
            my_list.insert(i)

        my_data.sort()

        rc = my_list.search(55)
        self.assertEqual(rc, None)

        rc = my_list.search(0)
        self.assertEqual(rc, None)

        rc = my_list.search(12)
        self.assertEqual(rc, None)

        rc = my_list.search(13)
        self.assertEqual(rc, None)

        rc = my_list.search(-5)
        self.assertEqual(rc, None)


        rc = my_list.search(1)
        self.assertEqual(rc.get_data(), 1)
        self.assertEqual(rc.get_next().get_data(), 2)

        rc = my_list.search(15)
        self.assertEqual(rc.get_data(), 15)
        self.assertEqual(rc.get_previous().get_data(), 10)

        for i in range(1,10):
            rc = my_list.search(my_data[i])
            self.assertEqual(rc.get_data(), my_data[i])
            self.assertEqual(rc.get_previous().get_data(), my_data[i-1])
            self.assertEqual(rc.get_next().get_data(), my_data[i+1])








if __name__ == '__main__':
    unittest.main()
