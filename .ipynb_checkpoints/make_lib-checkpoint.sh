#!/bin/bash
set -x
SO=pbex$(python3-config --extension-suffix)
# $ c++ -O3 -Wall -shared -std=c++11 -undefined dynamic_lookup $(python3 -m pybind11 --includes) cbind.cpp -o pbex$(python3-config --extension-suffix)
g++ -D_GLIBCXX_USE_CXX11_ABI=0 -O2 -Wall -shared -std=c++14 -fPIC $(python3 -m pybind11 --includes) cbind.cpp -o ${SO} -lLamTDMS -lrc101