import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_rehash_helper(self):
        ht = HashTable(7)
        ht.hash_table[3] = ('lol', [5])
        ht.num_items += 1
        ht.hash_table[4] = ('lmao', [5])
        ht.num_items += 1
        ht.rehash_helper2([('cat', [5])])
        self.assertEqual(ht.get_num_items(), 3)
        self.assertEqual(ht.get_index('cat'), 0)

if __name__ == '__main__':
   unittest.main()