class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value=0):
        if (self.get_num_items()+1)/self.table_size >= 0.5:
            self.rehash_helper()
        idx = self.horner_hash(key)
        i = 0
        if self.hash_table[idx] is None:
            self.hash_table[idx + (i ** 2)] = (key, [value])
            self.num_items += 1
            return
        res = 0
        while self.hash_table[idx + (i ** 2) - res][0] != key:
            i += 1
            if idx + (i ** 2) >= self.table_size:
                res = self.table_size
            if self.hash_table[idx + (i ** 2) - res] is None:
                self.hash_table[idx + (i ** 2) - res] = (key, [value])
                self.num_items += 1
                return
        self.hash_table[idx + (i ** 2) - res][1].append(value)


    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        i = 0
        hash = 0
        n = min(8,len(key))
        while i < n:
            hash += ord(key[i]) * (31**(n-1-i))
            i += 1
        return hash%self.table_size

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        i = self.get_index(key)
        if i is None:
            return False
        return True

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""
        i = self.horner_hash(key)
        j = 0
        res = 0
        while self.hash_table[i + (j ** 2) - res] is not None:
            if self.hash_table[i + (j ** 2) - res][0] == key:
                return i + (j**2) - res
            j += 1
            if i + (j ** 2) >= self.table_size:
                res = self.table_size
        return None

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        list = []
        for entry in self.hash_table:
            if entry is not None:
                key = entry[0]
                list.append(key)
        return list

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""
        i = self.get_index(key)
        if i is None:
            return None
        return self.hash_table[i][1]


    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.get_num_items()/self.table_size

    def rehash_helper(self):
        to_rehash = []
        for entry in self.hash_table:
            if entry is not None:
                to_rehash += [entry]
        self.table_size = (self.table_size * 2) + 1
        self.num_items = 0
        self.hash_table = [None] * self.table_size
        self.rehash_helper2(to_rehash)


    def rehash_helper2(self,to_rehash):
        for item in to_rehash:
            idx = self.horner_hash(item[0])
            i = 0
            if self.hash_table[idx] is None:
                self.hash_table[idx + (i ** 2)] = (item[0], item[1])
                self.num_items += 1
            res = 0
            while self.hash_table[idx + (i ** 2) - res][0] != item[0]:
                i += 1
                if idx + (i ** 2) >= self.table_size:
                    res = self.table_size
                if self.hash_table[idx + (i ** 2) - res] is None:
                    self.hash_table[idx + (i ** 2) - res] = (item[0], item[1])
                    self.num_items += 1


