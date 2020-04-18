import unittest


class InitializationTests(unittest.TestCase):

    def test_initialization(self):
        """
        Check the test suite runs by affirming 2+2=4
        """
        self.assertEqual(2 + 2, 4)

    def test_import(self):
        """
        Ensure the test suite can import our module
        """
        try:
            import sample_python_package
        except ImportError:
            self.fail("Was not able to import the src")

# Run this in the project root from terminal to test:
# "nosetests -v --with-coverage --cover-package=sample_python_package --cover-inclusive --cover-erase tests"
