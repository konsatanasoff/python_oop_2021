import unittest

from lab.List.extended_list import IntegerList


class IntegerListTests(unittest.TestCase):
    def _test_integerListInit_whenNotOnlyIntegers_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            IntegerList(1, 2, 3, True, 5)

        self.assertIsNotNone(context.exception)

    def test_integerListInit_whenOnlyIntegers_shouldStoreThem(self):
        values = [1, 2, 3, 4, 5]
        integer_list = IntegerList(*values)

        self.assertListEqual(values, integer_list.get_data())

    def test_integerListAdd_whenValueIsInteger_shouldBeAdded(self):
        integer_list = IntegerList()
        integer_list.add(1)

        self.assertListEqual([1], integer_list.get_data())

    def test_integerListAdd_whenValueNotInteger_shouldRaiseException(self):
        integer_list = IntegerList()

        with self.assertRaises(Exception) as context:
            integer_list.add({})

        self.assertIsNotNone(context.exception)

    def test_integerListRemoveIndex_whenIndexIsValid_shouldRemoveAndReturnElement(self):
        integer_list = IntegerList(1, 2, 3, 4, 5)
        returned = integer_list.remove_index(3)

        self.assertListEqual([1, 2, 3, 5], integer_list.get_data())
        self.assertEqual(4, returned)

    def test_integerListRemoveIndex_whenIndexIsInvalid_shouldRaiseException(self):
        integer_list = IntegerList(1, 2, 3, 4, 5)

        with self.assertRaises(Exception) as context:
            integer_list.remove_index(len(integer_list.get_data()))

        self.assertIsNotNone(context.exception)

    def test_integerListGet_whenIndexIsValid_shouldReturnElement(self):
        integer_list = IntegerList(1, 2, 3, 4, 5)

        self.assertEqual(1, integer_list.get(0))

    def test_integerListGet_whenIndexIsInvalid_shouldRaiseException(self):
        integer_list = IntegerList(1, 2, 3, 4, 5)

        with self.assertRaises(Exception) as context:
            integer_list.get(len(integer_list.get_data()))

        self.assertIsNotNone(context.exception)

    def test_integerListInsert_whenIndexIsValid_shouldInsertIt(self):
        integer_list = IntegerList(1, 2, 3, 4, 5)

        integer_list.insert(0, 0)
        self.assertEqual(0, integer_list.get_data()[0])

    def test_integerListInsert_whenIndexIsInvalid_shouldRaiseException(self):
        integer_list = IntegerList(1, 2, 3, 4, 5)

        with self.assertRaises(Exception) as context:
            integer_list.insert(15, 0)

        self.assertIsNotNone(context.exception)

    def test_integerListInsert_whenElementIsInteger_shouldInsertIt(self):
        integer_list = IntegerList(1, 2, 3, 4, 5)

        integer_list.insert(0, 0)
        self.assertEqual(0, integer_list.get_data()[0])

    def test_integerListInsert_whenElementIsNotInteger_shouldRaiseException(self):
        integer_list = IntegerList(1, 2, 3, 4, 5)

        with self.assertRaises(Exception) as context:
            integer_list.insert(0, "invalid")

        self.assertIsNotNone(context.exception)

    def test_integerListGetBiggest_shouldReturnBiggestElement(self):
        integer_list = IntegerList(1, 2, 3, 4, 5)

        self.assertEqual(5, integer_list.get_biggest())

    def test_integerListGetIndex_shouldReturnElementIndex(self):
        integer_list = IntegerList(1, 2, 3, 4, 5)

        self.assertEqual(0, integer_list.get_index(1))


if __name__ == '__main__':
    unittest.main()
