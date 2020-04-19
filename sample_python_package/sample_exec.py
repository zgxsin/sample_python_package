from sample_python_package.sample import dataset
import os


def main():
    """Entry point for the application script"""
    # Use absolute path for files, otherwise you can not find it after you install the package. In this case,
    # you might have some issue in developing your code before you install your package, since python will first find
    # modules and packages in current directly instead of the parent directory where sample_python_package is located.
    # I tested it in Pycharm, which can handle this issue. You don't need to do anything. But if you are running your
    # program in a virtualenv, there is a known issue: https://github.com/clj-python/libpython-clj/issues/2
    # =====================================Deprecated==================================================================
    # You can change PYTHONPATH in your environment to handle this issue. PYTHONPATH is an environment variable
    # which you can set to add additional directories where python will look for modules and packages.
    # For most installations, you should not set these variables since they are not needed for Python to run.
    # Python knows where to find its standard library. The only reason to set PYTHONPATH is to maintain directories of
    # custom Python libraries that you do not want to install in the global default location
    # (i.e., the site-packages directory). Here you can extend PYTHONPATH with the ../sample_python_package temporally
    #  for developing your package using this command: export PYTHONPATH="${PYTHONPATH}:/my/other/path"
    # =====================================Deprecated==================================================================

    # How to add parsers: https://docs.python.org/3/library/argparse.html#required
    path = os.path.join(os.path.dirname(__file__), 'fixtures/calories.csv')
    for row in dataset(path):
        print(row[0])