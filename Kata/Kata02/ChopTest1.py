import unittest


# http://codekata.com/kata/kata02-karate-chop/
class ChopTest1(unittest.TestCase):

  def chop(self, index, array):
    return 0

  def test_chop(self):
    self.assertEquals(-1, self.chop(3, []))
    self.assertEquals(-1, self.chop(3, [1]))
    self.assertEquals(0,  self.chop(1, [1]))
    self.assertEquals(0,  self.chop(1, [1, 3, 5]))
    self.assertEquals(1,  self.chop(3, [1, 3, 5]))
    self.assertEquals(2,  self.chop(5, [1, 3, 5]))
    self.assertEquals(-1, self.chop(0, [1, 3, 5]))
    self.assertEquals(-1, self.chop(2, [1, 3, 5]))
    self.assertEquals(-1, self.chop(4, [1, 3, 5]))
    self.assertEquals(-1, self.chop(6, [1, 3, 5]))
    self.assertEquals(0,  self.chop(1, [1, 3, 5, 7]))
    self.assertEquals(1,  self.chop(3, [1, 3, 5, 7]))
    self.assertEquals(2,  self.chop(5, [1, 3, 5, 7]))
    self.assertEquals(3,  self.chop(7, [1, 3, 5, 7]))
    self.assertEquals(-1, self.chop(0, [1, 3, 5, 7]))
    self.assertEquals(-1, self.chop(2, [1, 3, 5, 7]))
    self.assertEquals(-1, self.chop(4, [1, 3, 5, 7]))
    self.assertEquals(-1, self.chop(6, [1, 3, 5, 7]))
    self.assertEquals(-1, self.chop(8, [1, 3, 5, 7]))


