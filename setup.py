#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from pathlib import Path
from typing import List

import numpy
from Cython.Build import cythonize
from setuptools import find_packages, setup
from setuptools.command.build_ext import build_ext
from setuptools.extension import Extension


def find_files(root: Path, ext: str) -> List[str]:
    """
    Search for files of given extension recursively within root
    """
    return [str(file) for file in Path(root).glob("*" + ext)]


class Build(build_ext):
    def build_extensions(self):
        if self.compiler.compiler_type in ["unix", "mingw32"]:
            for e in self.extensions:
                if e.name == "picoscenes":
                    e.extra_compile_args = ["-std=c++2a", "-Wno-attributes", "-O3"]
        if self.compiler.compiler_type in ["msvc"]:
            for e in self.extensions:
                if e.name == "picoscenes":
                    e.extra_compile_args = ["/std:c++latest"]
        super(Build, self).build_extensions()


pico_root = Path.cwd() / "rxs_parsing_core"
pico_generated = pico_root / "preprocess" / "generated"
pico_include = pico_root / "preprocess"
pico_source = find_files(pico_root, ".cxx") + find_files(pico_generated, ".cpp")
pico_extension = Extension(
    "picoscenes",
    ["./picoscenes.pyx"] + pico_source,
    include_dirs=[numpy.get_include(), str(pico_include)],
    define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
)


if not pico_root.is_dir():
    raise RuntimeError(
        f"Parsing core submodule {pico_root} is not a directory; "
        + "Did you initialize the submodule?"
    )

EXTENSIONS = [pico_extension]


setup(
    name="picoscenes",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["numpy"],
    python_requires=">=3",
    ext_modules=cythonize(
        EXTENSIONS, compiler_directives={"language_level": 3, "binding": False}
    ),
    cmdclass={"build_ext": Build},
)
