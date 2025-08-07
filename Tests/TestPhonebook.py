import unittest
from main import Phonebook

class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.phonebook = Phonebook()

        test_entries = [
            ("John", "Doe", "555-1234", "New York", "NY"),
            ("Jane", "Smith", "555-5678", "Los Angeles", "CA"),
            ("Bob", "Johnson", "555-9012", "Chicago", "IL"),
            ("Alice", "Doe", "555-3456", "Miami", "FL"),
            ("Charlie", "Brown", "555-7890", "Seattle", "WA")
        ]

        for first, last, phone, city, state in test_entries:
            self.phonebook.add_entry(first, last, phone, city, state)

class TestSearchByLastName(TestPhonebook):
    def test_search_by_last_name_found_multiple(self):
        results = self.phonebook.search_by_last_name("Doe")

        self.assertEqual(len(results), 2)
        for result in results:
            self.assertEqual(result[1], "Doe")

        first_names = [result[0] for result in results]
        self.assertIn("John", first_names)
        self.assertIn("Alice", first_names)

    def test_search_by_last_name_not_found(self):
        results = self.phonebook.search_by_last_name("NonExistent")
        self.assertEqual(results, [])

    def test_search_by_last_name_found_single(self):
        results = self.phonebook.search_by_last_name("Smith")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], ("Jane", "Smith", "555-5678", "Los Angeles", "CA"))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    test_classes = [
        TestSearchByLastName
    ]

    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
