from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='labdatautils',
      version='0.1',
      description=readme(),
      url='http://github.com/kjaanson/labdatautils',
      author='Kaur Jaanson',
      author_email='kjaanson@gmail.com',
      license='MIT',
      packages=['labdatautils'],
      install_requires=[
        'pandas',
        'ipywidgets'
      ],
      zip_safe=False,)
