[![Download](https://api.bintray.com/packages/nickbruun/conan/hayai%3Anickbruun/images/download.svg)](https://bintray.com/nickbruun/conan/hayai%3Anickbruun/_latestVersion)

[![Build status](https://ci.appveyor.com/api/projects/status/github/nickbruun/conan-hayai?svg=true)](https://ci.appveyor.com/project/nickbruun/conan-hayai)

[![Build Status](https://travis-ci.org/nickbruun/conan-hayai.svg)](https://travis-ci.org/nickbruun/conan-hayai)

# conan-hayai

Conan package for [Hayai](https://github.com/nickbruun/hayai)

The packages generated with this **conanfile** can be found on [bintray](https://bintray.com/nickbruuny).

## Reuse the packages

### Basic setup

    $ conan install hayai/1.0.2@nickbruun/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    hayai/1.0.2@nickbruun/stable

    [options]
    hayai:shared=True # False
    # Take a look for all available options in conanfile.py

    [generators]
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake*
with all the paths and variables that you need to link with your dependencies.

Follow the Conan getting started: http://docs.conan.io
