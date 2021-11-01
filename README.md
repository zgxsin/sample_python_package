# Sample Python Project

## Definitions
* Package      - A folder/directory that contains `__init__.py` file.
* Module       - A valid python file with `.py` extension.

## Project Structure
* `bin`

  The `bin` folder will contain any executable scripts you intend to build.
* `data`
  
  The `data` folder contains additional data of your project.
* `docs`
  
  The `docs` folder contains the Sphinx documentation generator, Python documentation is written in restructuredText,
  a Markup language similar to Markdown and others. Run `sphinx-quickstart` inside docs folder to
  generate documentation.
  
* `sample_python_package/fixtures`
  
  Data scientists typically have a `fixtures` folder in which to store data files.
  
* `sample_python_package` and `tests`

  The `sample_python_package` and `tests` folders are actually Python modules (packages) since they contain the
  `__init__.py` file. You'll put your code in `sample_python_package` and your tests in `tests`.
  
* `setup.py`
  
  The `setup.py` script is a Python setuptools or distutils installation script and will allow you to configure your
  project for deployment. It will use the `requirements.txt` to specify the third party dependencies required to
  implement your project. Other developers will also use these files to create their development environments. More detailed 
  explanation can be found within `setup.py`.
  
  
## Development
It is recommended to use python `virtualenv` to develop your python project.
Check here: [Manage_Python_Environment](https://www.guoxiang-zhou.xyz/2020/04/04/understand-python-environment-in-ubuntu-18-04/).
Check out this [tool](https://github.com/cookiecutter/cookiecutter) to create the project template.
When you finish your project, run the following command to automatically generate `requirements.txt`:
```
pip3 install pipreqs

pipreqs /path/to/project
```

## Installation
`setup.py` is Python's answer to a multi-platform installer and is similar to `Makefile`.
If you’re familiar with command line installations, then `make && make install` translates to
`python setup.py build && python setup.py install`. Best practice is to use `pip`. It only offers improvements over 
using `python setup.py install`. See the discussion 
[Difference between 'python setup.py install' and 'pip install'](https://stackoverflow.com/questions/15724093/difference-between-python-setup-py-install-and-pip-install/15731459).

Run `pip install .` in your project root to install this package `sample-python-project`. 
It will use `setup.py` to install it. Run `pip show sample-python-project` to verify the installation.

## Distribution
1. Before you begin, make sure you have the latest versions of setuptools and wheel:
`pip install --upgrade setuptools wheel`. This will generate distribution archives in the `dist` directory.

2. To build a setuptools project, run `python setup.py sdist bdist_wheel` from the same directory where `setup.py` is located.

3. Before you upload the generated archives make sure you’re registered on https://test.pypi.org/account/register/.
You will also need to verify your email to be able to upload any packages.
You should install twine to be able to upload packages: `pip install --upgrade twine`

4. Now, to upload these archives, run:
`twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

5. To install your newly uploaded package, you can use pip:
`pip install --index-url https://test.pypi.org/simple/ sample_python_package`

6. Follow the link below to upload a real package to the Python Package Index :
https://packaging.python.org/tutorials/packaging-projects/#next-steps.

## Tips
1. When importing your own defined module, always use the defined `top-level` package name. Otherwise,
your script (entry_point) will not work after installing the package. In our example,
the defined top-level package is `sample_python_package`, which contains `__init__.py`. You can observe that we use
`from sample_python_package.sample import dataset` in `sample_exec.py` instead of using `from sample import dataset`.

## References
1. [How to Develop Quality Python Code](https://medium.com/district-data-labs/how-to-develop-quality-python-code-8209af654d79).
2. https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives.