import sys
from pybind11 import get_cmake_dir
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

example_module = [Pybind11Extension(
    'pbex',
    ["c/test_c.cpp"],
    define_macros = [('VERSION_INFO', '0.1')],
)]

setup(
    name='pbex',
    packages=['pbex_py'],
    package_dir={"":'./'},
    version='0.1',
    extras_require={"test": "pytest"},
    ext_modules=example_module,
    cmdclass={"build_ext": build_ext},
    
    zip_safe=False,
    python_requires=">=3.8",
)