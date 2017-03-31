import os
from parsenvy import parsenvy
import unittest


class BooleanTest(unittest.TestCase):

    def test_true(self):
        os.environ['BOOL_TRUE'] = 'true'
        self.assertTrue(parsenvy.bool('BOOL_TRUE'))

        os.environ['BOOL_1'] = '1'
        self.assertTrue(parsenvy.bool('BOOL_1'))

    def test_false(self):
        os.environ['BOOL_FALSE'] = 'false'
        self.assertFalse(parsenvy.bool('BOOL_FALSE'))

        os.environ['BOOL_0'] = '0'
        self.assertFalse(parsenvy.bool('BOOL_0'))

    def test_none(self):
        self.assertIsNone(parsenvy.bool('BOOL_NONE'))

    def test_default(self):
        self.assertTrue(parsenvy.bool('BOOL_NONE', True))

    def test_error(self):
        os.environ['BOOL_EMPTY'] = ''
        with self.assertRaises(TypeError):
            parsenvy.bool('BOOL_EMPTY')

        os.environ['BOOL_STR'] = 'nope'
        with self.assertRaises(TypeError):
            parsenvy.bool('BOOL_STR')


class IntTest(unittest.TestCase):

    def test_int(self):
        os.environ['INT_2'] = '2'
        self.assertEqual(parsenvy.int('INT_2'), 2)

    def test_none(self):
        self.assertIsNone(parsenvy.int('INT_NONE'))

    def test_default(self):
        self.assertEqual(parsenvy.int('INT_NONE', 3), 3)

    def test_error(self):
        os.environ['INT_EMPTY'] = ''
        with self.assertRaises(TypeError):
            parsenvy.int('INT_EMPTY')

        os.environ['INT_STR'] = 'nope'
        with self.assertRaises(TypeError):
            parsenvy.int('INT_STR')


class FloatTest(unittest.TestCase):

    def test_float(self):
        os.environ['FLOAT_1_23'] = '1.23'
        self.assertEqual(parsenvy.float('FLOAT_1_23'), 1.23)

    def test_none(self):
        self.assertIsNone(parsenvy.float('FLOAT_NONE'))

    def test_default(self):
        self.assertEqual(parsenvy.float('FLOAT_NONE', 1.23), 1.23)

    def test_error(self):
        os.environ['FLOAT_EMPTY'] = ''
        with self.assertRaises(TypeError):
            parsenvy.float('FLOAT_EMPTY')

        os.environ['FLOAT_STR'] = 'nope'
        with self.assertRaises(TypeError):
            parsenvy.float('FLOAT_STR')


class ListTest(unittest.TestCase):

    def test_list(self):
        os.environ['LIST_A_B_C'] = 'a,b,c'
        self.assertEqual(parsenvy.list('LIST_A_B_C'), ['a', 'b', 'c'])

    def test_none(self):
        self.assertIsNone(parsenvy.list('LIST_NONE'))

        os.environ['LIST_EMPTY'] = ''
        self.assertIsNone(parsenvy.list('LIST_EMPTY'))

    def test_default(self):
        self.assertEqual(parsenvy.list('LIST_NONE', [1, 2]), [1, 2])


class TupleTest(unittest.TestCase):

    def test_tuple(self):
        os.environ['TUPLE_HELLO_WORLD'] = 'hello,there,world'
        self.assertEqual(parsenvy.tuple('TUPLE_HELLO_WORLD'), ('hello', 'there', 'world'))

    def test_none(self):
        self.assertIsNone(parsenvy.tuple('TUPLE_NONE'))

        os.environ['TUPLE_EMPTY'] = ''
        self.assertIsNone(parsenvy.tuple('TUPLE_EMPTY'))

    def test_default(self):
        self.assertEqual(parsenvy.tuple('TUPLE_NONE', ('hello', 'there', 'world')), ('hello', 'there', 'world'))


class StringTest(unittest.TestCase):

    def test_list(self):
        os.environ['STR_HELLO'] = 'hello'
        self.assertEqual(parsenvy.str('STR_HELLO'), 'hello')
        os.environ['STR_EMPTY'] = ''
        self.assertEqual(parsenvy.str('STR_EMPTY'), '')

    def test_none(self):
        self.assertIsNone(parsenvy.str('STR_NONE'))

    def test_default(self):
        self.assertEqual(parsenvy.str('STR_NONE', 'hi'), 'hi')


class SetTest(unittest.TestCase):

    def test_set(self):
        os.environ['SET_A_B_C'] = 'a,b,c'
        self.assertEqual(parsenvy.set('SET_A_B_C'), set(['a', 'b', 'c']))

    def test_none(self):
        self.assertIsNone(parsenvy.set('SET_NONE'))

        os.environ['SET_EMPTY'] = ''
        self.assertIsNone(parsenvy.set('SET_EMPTY'))

    def test_default(self):
        self.assertEqual(parsenvy.set('SET_NONE', set([1, 2])), set([1, 2]))


class DictTest(unittest.TestCase):

    def test_dict(self):
        os.environ['DICT_A_1_B_2'] = 'a:1,b:2'
        self.assertEqual(parsenvy.dict('DICT_A_1_B_2'), {'a': '1', 'b': '2'})

    def test_none(self):
        self.assertIsNone(parsenvy.dict('DICT_NONE'))

    def test_default(self):
        self.assertEqual(parsenvy.dict('DICT_NONE', {'a': '1', 'b': '2'}), {'a': '1', 'b': '2'})

    def test_error(self):
        os.environ['DICT_EMPTY'] = ''
        with self.assertRaises(TypeError):
            parsenvy.dict('DICT_EMPTY')


if __name__ == '__main__':
    unittest.main()
