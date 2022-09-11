#include <pybind11/pybind11.h>

#define MAXINT 2147483647
#define MAXINT32 2147483647

unsigned c_func(int n)
{
int i,sum,num=0;

for(i=0; i<n; i++)
{
    sum+= i*i;
}
return sum;
}

namespace py = pybind11;


PYBIND11_MODULE(pbex, m) {
    m.def("c_func", &c_func);
}