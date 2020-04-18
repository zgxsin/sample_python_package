#!/usr/bin/env python

# The #! (pronounced "shebang") line must appear at the very beginning of an executable Python script with nothing
# before it. It will tell your computer that this is a Python file and execute the script correctly if run from
# the command line as a standalone app, i.e., run "./python_file.py" directly. This line doesn't need to appear
# in library modules, that is, Python code that you plan to import rather than execute.

# If you run "python python_file.py" or "python3 python_file.py", the shebang is not necessary.
# But it is good to keep it there. Yuo can also use "#!/usr/bin/env python3" to use python3 by default.

import csv
import os


def dataset(path):
    with open(path, 'rU') as data:
        reader = csv.reader(data)
        for row in reader:
            row[2] = int(row[2])
            yield row


# The if __name__ == '__main__': statement means that the code will only get executed if the code is run directly,
# not imported.
# It means that you can put test code inside your script as you're developing it without worrying that it
# will interfere with your project. Not only that, it documents to other developers how the code in that
# file should be used and provides a simple test to check to make sure that you're not creating errors.
if __name__ == '__main__':
    path = os.path.join(os.path.dirname(__file__), 'fixtures/calories.csv')
    for row in dataset(path):
        print(row[0])
