from conans import ConanFile, CMake, tools, AutoToolsBuildEnvironment
from pykuklin.downloader import get_downloader_available_in_current_environment, Path
from pykuklin.conan.tools import build_env_vars_set
import os
import shutil

downloader = get_downloader_available_in_current_environment()

class ConanFileImpl(ConanFile):
    name = "ulfius"
    version = "2.6.5"
    exports_sources = "0001-Orcania-Yder-from-scratch-bug.patch"
    
    requires = "gnutls/3.6.12", "libmicrohttpd/0.9.70", "jansson/2.12", "curl/7.71.1", "libidn2/2.0.5"
    # warning: not compatible with libmicrohttpd/0.9.71

    exports_sources = "*.patch"    
    generators = "cmake_find_package"
   

    def source(self):
        self.run("git clone https://github.com/babelouest/ulfius")
        os.chdir("ulfius")
        self.run("git checkout v2.6.5")
        self.run("patch < ../FindPackageOverrides.cmake.patch")

    def build(self):
        sf = "ulfius"
        cmake = CMake(self)
    
        with build_env_vars_set(self):
            cmake.definitions['CMAKE_IGNORE_PATH'] = '/usr/local/lib;/usr/lib;/lib'
            cmake.definitions['CMAKE_MODULE_PATH'] = os.getcwd()
            cmake.definitions['WITH_JOURNALD'] = 'Off'
            cmake.configure(source_folder=sf)
            cmake.build()

    def package(self):
        with tools.environment_append(self.env):
            cmake = CMake(self)
            cmake.install()
