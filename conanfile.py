#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires

base = python_requires("boost_base/1.69.0@bincrafters/stable")


class BoostParameterPythonConan(base.BoostBaseConan):
    name = "boost_parameter_python"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_parameter_python"
    lib_short_names = ["parameter_python"]
    header_only_libs = ["parameter_python"]
    b2_requires = [
        "boost_mpl",
        "boost_parameter",
        "boost_preprocessor",
        "boost_python"
    ]

    def package_info_additional(self):
        self.info.options["boost_python"].python_version = "any"
