from setuptools import setup, find_packages

setup(
    name='pynocle',
    version='0.2dev',
    description="Software metrics for your python code",
    long_description=open('README.txt').read(),
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='coverage cyclomatic complexity',
    author='Rob Galanakis',
    author_email='rob.galanakis@gmail.com',
    url="http://code.google.com/p/pynocle/",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'coverage',
    ],
    entry_points="""
    [console_scripts]
    pynocle = pynocle.pynocle:main
   """,
)
