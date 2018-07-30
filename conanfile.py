#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from conans import ConanFile, CMake, tools


class HayaiConan(ConanFile):
    name = 'hayai'
    version = '1.0.2'
    license = 'https://github.com/nickbruun/hayai/blob/master/LICENSE.md'
    url = 'https://github.com/nickbruun/conan-hayai'
    homepage = 'https://github.com/nickbruun/hayai'
    description = 'C++ benchmarking framework'
    author = 'nickbruun <nick@bruun.co>'
    settings = 'os', 'compiler', 'build_type', 'arch'
    options = {'shared': [True, False], 'fPIC': [True, False]}
    default_options = 'shared=False', 'fPIC=True'
    exports_sources = ["CMakeLists.txt"]
    generators = 'cmake'
    build_subfolder = 'build_subfolder'
    source_subfolder = 'source_subfolder'

    def configure(self):
        if self.settings.compiler == "Visual Studio":
            self.options.remove("fPIC")

    def source(self):
        tools.get('{0}/archive/v{1}.tar.gz'.format(self.homepage, self.version))
        extracted_dir = self.name + '-' + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy("LICENSE.md", dst="licenses", src=self.source_subfolder)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.env_info.CMAKE_PREFIX_PATH.append(os.path.join(self.package_folder, "lib", "CMake"))
