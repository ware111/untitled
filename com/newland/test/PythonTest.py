import unittest


def get_name(first, last, mimi):
    full_name = first+' ' + last + ' ' + mimi
    return full_name.title()


class NameTest(unittest.TestCase):
    def test_name(self):
        name = get_name('a', 'b', 'c')
        self.assertEqual(name, [1, 2])


unittest.main()