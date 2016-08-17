import unittest
from app import foo, bar


class AppTestCase(unittest.TestCase):

  def test_foo(self):
    self.assertEqual(foo(1, 2), 3)

  def test_bar(self):
    self.assertEqual(bar(1, 2), -1)


if __name__ == '__main__':
  unittest.main()