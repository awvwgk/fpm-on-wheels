import sys

from skbuild import setup

setup(
    name="fpm",
    version="0.7.0",
    description="Fortran Package Manager",
    author="Fortran-lang",
    license="MIT",
    python_requires=">=3.7",
    cmake_args=(
        ["-G", "Visual Studio 16 2019"] if sys.platform == "win32" else ["-G", "Ninja"]
    ),
)
