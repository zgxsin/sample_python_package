#!/usr/bin/env python
# coding=utf-8

# Project reference: https://medium.com/district-data-labs/how-to-develop-quality-python-code-8209af654d79.

# =============================================================================
# Below is the explanation of the project structure.
# =============================================================================
# The bin directory will contain any executable scripts you intend to build.

# The data folder contains additional data of your project.

# The docs directory contains the Sphinx documentation generator, Python documentation is written in restructuredText,
# a Markup language similar to Markdown and others. Run "sphinx-quickstart" inside docs folder to
# generate documentation.

# Data scientists also typically also have a fixtures directory in which to store data files.

# The src and tests directories are actually Python modules (packages) since they contain the
# __init__.py file. You'll put your code in foo and your tests in tests.

# When you finish your project, create your requirements.txt using "pip freeze > requirements.txt" in your project root.

# The setup.py script is a Python setuptools or distutils installation script and will allow you to configure your
# project for deployment. It will use the requirements.txt to specify the third party dependencies required to
# implement your project. Other developers will also use these files to create their development environments.

# Here is a tool to help you create the project template: https://github.com/cookiecutter/cookiecutter.

"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils.
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7.
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding.
# Python 3 only projects can skip this import.
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README.md file.
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install .
    #
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name='sample_python_package',  # Required

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.0',  # Required

    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description='A sample python project',  # Optional

    # This is an optional longer description of your project that represents
    # the body of text which users will see when they visit PyPI.
    #
    # Often, this is the same as your README.md, so you can just read it in from
    # that file directly (as we have already done above)
    #
    # This field corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional

    # Denotes that our long_description is in Markdown; valid values are
    # text/plain, text/x-rst, and text/markdown
    #
    # Optional if long_description is written in reStructuredText (rst) but
    # required for plain-text or Markdown; if unspecified, "applications should
    # attempt to render [the long_description] as text/x-rst; charset=UTF-8 and
    # fall back to text/plain if it is not valid rst" (see link below)
    #
    # This field corresponds to the "Description-Content-Type" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type='text/markdown',  # Optional (see note above)

    # This should be a valid link to your project's main homepage.
    #
    # This field corresponds to the "Home-Page" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#home-page-optional
    # todo
    url='https://github.com/pypa/sampleproject',  # Optional

    # This should be your name or the name of the organization which owns the
    # project.
    author='Guoxiang Zhou',  # Optional

    # This should be a valid email address corresponding to the author listed
    # above.
    author_email='harigxzhou@gmail.com',  # Optional

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a string of words separated by whitespace, not a list.
    keywords='sample setuptools development',  # Optional

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    # The keys to this dictionary are package names, and an empty package name stands for the root package.
    # The values are directory names relative to your distribution root
    # Additionally, check here: https://setuptools.readthedocs.io/en/latest/setuptools.html.
    # package_dir={'': 'sample_python_package'},  # Optional, tell distutils packages are under sample_python_package.

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    # find_packages() takes a source directory and two lists of package name patterns to exclude and include.
    # If omitted, the source directory defaults to the same directory as the setup script. Some projects use a src or
    # lib directory as the root of their source tree, and those projects would of course use "src" or "lib" as the
    # first argument to find_packages(). (And such projects also need something like package_dir={"": "src"} in their
    # setup() arguments, but that’s just a normal distutils thing.)
    # Additionally, check here: https://setuptools.readthedocs.io/en/latest/setuptools.html#using-find-packages.
    packages=find_packages(),  # Required, include all packages under current path.

    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers above, 'pip install' will check this
    # and refuse to install the project if the version does not match. If you
    # do not support Python 2, you can simplify this to '>=3.5' or similar, see
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    # Whereas install_requires defines the dependencies for a single project,
    # requirements.txt Files are often used to define the requirements for a complete Python environment.
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['coverage'],  # Optional

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sample_python_package[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    #
    # If using Python 2.6 or earlier, then these have to be included in
    # MANIFEST.in as well.
    # The below option will include fixtures/calories.csv under your package sample_python_package to
    # your installed package. Use this command to find where it is after you installing it:
    # sudo find / -type f -name calories.csv. fixtures/calories.csv should be located in your installed package.
    package_data={  # Optional
        'sample_python_package': ['fixtures/calories.csv'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data' Each (directory, files) pair in the
    # sequence specifies the installation directory and the files to install there. Use this command to find where it
    # is after you installing it: sudo find / -type d -name sample_python_project_data.
    data_files=[('sample_python_project_data', ['data/sample_data_file.txt'])],  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
        'console_scripts': [
            'sample_exec=sample_python_package.sample_exec:main',
        ],
    },

    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    # todo
    project_urls={  # Optional
        'Source': 'https://github.com/pypa/sampleproject/',
    },
)

# ======================================================================================
# Instruction for setup.py
# ======================================================================================
# Let's start with some definitions:
# Package - A folder/directory that contains __init__.py file.
# Module - A valid python file with .py extension.
# Distribution - How one package relates to other packages and modules.

# ===================Installation ======================================================
# https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives.
# setup.py is Python's answer to a multi-platform installer and is similar to Makefile.
# If you’re familiar with command line installations, then make && make install translates to
# python setup.py build && python setup.py install.
# Best practice: use pip. It only offers improvements over using python setup.py install.
# Refer to:
# https://stackoverflow.com/questions/15724093/difference-between-python-setup-py-install-and-pip-install/15731459.

# Run "pip install ." in your project root to install this
# package "sample-python-project". It will use setup.py to install this package. Run "pip show sample-python-project"
#  to verify the installation.

# ===================Distribution =======================================================
# 1. Before you begin, make sure you have the latest versions of setuptools and wheel:
# pip install --upgrade setuptools wheel. This will generate distribution archives in the dist directory.

# 2. To build a setuptools project, run this command from the same directory where setup.py is located:
# python setup.py sdist bdist_wheel

# 3. Before you upload the generated archives make sure you’re registered on https://test.pypi.org/account/register/.
# You will also need to verify your email to be able to upload any packages.
# You should install twine to be able to upload packages:You should install twine to be able to upload packages:
# pip install --upgrade twine

# 4. Now, to upload these archives, run:
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# 5. To install your newly uploaded package example_pkg, you can use pip:
# pip install --index-url https://test.pypi.org/simple/ sample_python_package

# 6. Follow the link below to upload a real package to the Python Package Index :
# https://packaging.python.org/tutorials/packaging-projects/#next-steps.


