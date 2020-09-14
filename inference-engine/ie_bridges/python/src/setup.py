import glob
from setuptools import setup, find_packages
try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False 
except ImportError:
    bdist_wheel = None

data = []
data += [_ for _ in glob.glob('../../*.so*')]
data += [_ for _ in glob.glob('../../../../../../temp/opencv*/lib/libopencv_*.so*')]
data += [_ for _ in glob.glob('../../../../../../temp/tbb/lib/libtbb.so.*')]
data += [_ for _ in glob.glob('../../*.xml')]

setup(name="openvino",
      packages=find_packages(),
      version = "0.9.0",
      package_data={
                'openvino.inference_engine': ['*.so'],
                'openvino.tools.statistics_collector': ['*.so'],
                },

      classifiers=[
          # https://pypi.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: C++',
          'Programming Language :: Cython',
          'Programming Language :: Other',  # R, Scala
          'Programming Language :: Perl',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: Implementation :: CPython',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      data_files=[('openvino', data)],
      cmdclass={'bdist_wheel': bdist_wheel},)
