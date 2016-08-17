import unittest
from app import foo, bar,baz


class AppTestCase(unittest.TestCase):

  def test_foo(self):
    self.assertEqual(foo(1, 2), 3)

  def test_bar(self):
    self.assertEqual(bar(1, 2), -1)

  def test_baz(self):
    self.assertEqual(baz(2, 2), 4)


if __name__ == '__main__':
  unittest.main()