# blopex-python
BLOPEX: Block Locally Optimal Preconditioned Eigenvalue Xolvers in Python

General

The original https://bitbucket.org/joseroman/blopex Block Locally Optimal Preconditioned Eigenvalue Xolvers (BLOPEX) [1] is a package, written in C and MATLAB/OCTAVE, that includes an eigensolver implemented with the Locally Optimal Block Preconditioned Conjugate Gradient Method (LOBPCG) [2,3,4]. BLOPEX design is to have a single "abstract" code of LOBPCG and several interfaces to it from host packages, including MPI-based HYPRE and PETSc/SLEPc, all written in C.

There is a Python code https://github.com/scipy/scipy/blob/master/scipy/sparse/linalg/eigen/lobpcg/lobpcg.py but the multivector there is hard-coded to be in the format of https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html

The goal of the current blopex-python project is to create a Python version of BLOPEX with a similar design - a single "abstract" code of LOBPCG and several interfaces to it from host packages, including scipy, dask, and tensorflow, all written in Python. When completed, the corresponding files are to be included in the host packages, with the idea that the interface codes are maintained by the host developers, while the "abstract" code is maintained in blopex-python .

BLOPEX main features are: matrix-free iterative methods for computing several extreme eigenpairs of symmetric/Hermitian generalized eigenproblems; user-defined preconditioning; robustness with respect to random initial approximations; and apparently optimal convergence speed.

Related Projects

https://github.com/scipy/scipy/blob/master/scipy/sparse/linalg/eigen/lobpcg/lobpcg.py 

https://github.com/dask/dask-ml/issues/364

https://github.com/tensorflow/tensorflow/issues/21835

https://github.com/search?q=lobpcg

https://bitbucket.org/joseroman/blopex

References

    1. A. V. Knyazev, I. Lashuk, M. E. Argentati, and E. Ovchinnikov, Block Locally Optimal Preconditioned Eigenvalue Xolvers (BLOPEX) in hypre and PETSc, SIAM Journal on Scientific Computing 25(5): 2224-2239 (2007) DOI

    2. A. V. Knyazev, Toward the Optimal Preconditioned Eigensolver: Locally Optimal Block Preconditioned Conjugate Gradient Method, SIAM Journal on Scientific Computing 23(2): 517-541 (2001) DOI
    
    3. https://en.wikipedia.org/wiki/LOBPCG
    
    4. https://www.mathworks.com/matlabcentral/fileexchange/48-lobpcg-m

Code license: https://en.wikipedia.org/wiki/BSD_licenses#2-clause_license_(%22Simplified_BSD_License%22_or_%22FreeBSD_License%22)
