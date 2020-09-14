from setuptools import find_packages, setup

setup(name="calibration_tool", 
      packages=find_packages(),
      entry_points = {'console_scripts': ['calibrate=calibration_tool.calibrate:main']})
