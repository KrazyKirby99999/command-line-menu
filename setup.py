from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='Command Line Menu',
      version='0.2.2',
      description='A simple module to create a menu for command line programs.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/KrazyKirby99999/command-line-menu',
      author='KrazyKirby99999',
      author_email='krazykirby99999@gmail.com',
      license='GNU AGPLv3',
      packages=setuptools.find_packages(),
      zip_safe=False,
      python_requires='>=3.4',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU AGPLv3 License",
        "Operating System :: OS Independent",
    ],
      )