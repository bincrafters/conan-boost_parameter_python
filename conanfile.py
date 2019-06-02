#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires

base = python_requires("boost_base/2.0.0@bincrafters/testing")


class BoostParameterPythonConan(base.BoostBaseConan):
    name = "boost_parameter_python"
    version = "1.70.0"

    def package_info(self):
        super(BoostParameterPythonConan, self).package_info()
        self.info.options["boost_python"].python_version = "any"
