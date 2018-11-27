from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.stop_table = HashTable(191)
        try:
            inf = open(filename)
            for line in inf:
                word = line.rstrip()
                self.stop_table.insert(word)
        except FileNotFoundError:
            raise FileNotFoundError('File does not exist')
        inf.close()

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.concordance_table = HashTable(191)
        try:
            inf = open(filename)
            lnumb = 1
            for line in inf:
                newline = ''
                for char in line:
                    if char == "'":
                        newline += ''
                    elif char == ' ':
                        newline += ' '
                    elif char in string.punctuation:
                        newline += ' '
                    elif char in string.ascii_uppercase:
                        newline += chr(ord(char) + 32)
                    elif char in string.ascii_lowercase:
                        newline += char
                wordlist = newline.split()
                for word in wordlist:
                    if not self.stop_table.in_table(word):
                        self.concordance_table.insert(word, lnumb)
                lnumb += 1
        except FileNotFoundError:
            raise FileNotFoundError('File does not exist')
        inf.close()

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        out = open(filename, 'w')
        concord_list = []
        for entry in self.concordance_table.hash_table:
            if entry is not None:
                linenums = ''
                for num in entry[1]:
                    linenums += ' ' + str(num)
                concord_list.append(str(entry[0]) + ':' + linenums)
        concord_list.sort()
        if len(concord_list) == 0:
            return
        for entry in concord_list[:-1]:
            out.write(entry + '\n')
        out.write(concord_list[-1])
        out.close()
