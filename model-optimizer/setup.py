from setuptools import find_packages, setup

setup(name="mo", 
      packages=find_packages('', exclude=["extensions"]),
      entry_points = {'console_scripts': ['mo=mo.__main__:main']})
