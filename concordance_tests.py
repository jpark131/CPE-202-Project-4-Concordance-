import unittest
import filecmp
from concordance import *

class TestList(unittest.TestCase):

   def test_01(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file1.txt")
       conc.write_concordance("file1_con.txt")
       self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))

   def test_02(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file2.txt")
       conc.write_concordance("file2_con.txt")
       self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))

   def test_03(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("declaration.txt")
       conc.write_concordance("declaration_con.txt")
       self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))

   def test_DNE(self):
       conc = Concordance()
       with self.assertRaises(FileNotFoundError):
           conc.load_stop_table("dne.txt")
       with self.assertRaises(FileNotFoundError):
           conc.load_concordance_table("dne.txt")

   def test_empty_file(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("empty_file.txt")
       conc.write_concordance("empty_con.txt")
       self.assertTrue(filecmp.cmp("empty_con.txt", "empty_sol.txt"))

   def test_single_word(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("hello_file.txt")
       conc.write_concordance("hello_con.txt")
       self.assertTrue(filecmp.cmp("hello_con.txt", "hello_sol.txt"))

   def test_diff_cases(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("up_file.txt")
       conc.load_concordance_table("down_file.txt")
       conc.write_concordance("up_con.txt")
       conc.write_concordance("down_con.txt")
       self.assertTrue(filecmp.cmp("up_con.txt", "down_con.txt"))

if __name__ == '__main__':
   unittest.main()
