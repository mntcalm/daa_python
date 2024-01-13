import unittest
import e23

class Testswap(unittest.TestCase):
  def test_swap(self):
    self.assertEqual(e23.swap('abcd'), 'cdab')
  def test_swap1(self):
    self.assertEqual(e23.swap('efgh'), 'ghef')

  def test_swap_invalid(self):
    self.assertNotEqual(e23.swap('557777'), '2354')



class TestExample(unittest.TestCase):
  def test_average(self):
    self.assertEqual(e23.average(2, 5, 2), 3)

  def test_average1(self):
    self.assertEqual(e23.average(10, 5, 3), 'd')

class TestExample(unittest.TestCase):
  def test_average_invalid(self):
    self.assertNotEqual(e23.average(2, 2, 5), 17)

if __name__=='__main__':
    unittest.main()


