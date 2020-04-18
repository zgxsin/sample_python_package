from sample import dataset
import os


def main():
    """Entry point for the application script"""
    # Use absolute path for files, otherwise you can not find it after you install the package.
    path = os.path.join(os.path.dirname(__file__), 'fixtures/calories.csv')
    for row in dataset(path):
        print(row[0])