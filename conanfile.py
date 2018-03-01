import os
from conans import ConanFile, CMake, tools


class HayaiConan(ConanFile):
    name = 'hayai'
    version = '1.0.2'
    license = 'https://github.com/nickbruun/hayai/blob/master/LICENSE.md'
    url = 'https://github.com/nickbruun/hayai'
    description = 'C++ benchmarking framework'
    settings = 'os', 'compiler', 'build_type', 'arch'
    options = {'shared': [True, False]}
    default_options = 'shared=False'
    generators = 'cmake'
    build_subfolder = 'build'
    source_subfolder = 'src'

    def source(self):
        source_url = 'https://github.com/nickbruun/hayai'
        tools.get('{0}/archive/v{1}.tar.gz'.format(source_url, self.version))
        extracted_dir = self.name + '-' + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_subfolder,
                        build_folder=self.build_subfolder)
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ['hayai_main']
