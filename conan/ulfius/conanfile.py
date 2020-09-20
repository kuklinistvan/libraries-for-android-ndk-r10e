from conans import ConanFile, CMake, tools, AutoToolsBuildEnvironment
from pykuklin.downloader import get_downloader_available_in_current_environment, Path
from pykuklin.conan.tools import build_env_vars_set
from pykuklin.shellutils import working_directory
import os
import shutil

downloader = get_downloader_available_in_current_environment()

class ConanFileImpl(ConanFile):
    name = "ulfius"
    version = "2.6.5"
    
    requires = "gnutls/3.6.12", "libmicrohttpd/0.9.70", "jansson/2.12", "curl/7.71.1", "libidn2/2.0.5"
    # warning: not compatible with libmicrohttpd/0.9.71

    exports_sources = "*.patch"    
    generators = "cmake_find_package"

    settings = "os", "compiler", "build_type", "arch"
   

    def source(self):
        self.run("git clone https://github.com/babelouest/ulfius")
        with working_directory("ulfius"):
            self.run("git checkout v2.6.5")
            self.run("patch < ../0001-FindPackageOverrides.cmake.patch")
            self.run("patch < ../0002-FixModulePath.patch")

    def build(self):
        sf = "ulfius"
        cmake = CMake(self)
        cmake.definitions['CMAKE_MODULE_PATH'] = os.getcwd()
    
        with build_env_vars_set(self, libs_as_ldflags=True):
            cmake.definitions['CMAKE_IGNORE_PATH'] = '/usr/local/lib;/usr/lib;/lib'
            cmake.definitions['WITH_JOURNALD'] = 'Off'
            cmake.definitions['BUILD_STATIC'] = 'On'
            cmake.configure(source_folder=sf)
            cmake.build()

    def package(self):
        with tools.environment_append(self.env):
            cmake = CMake(self)
            cmake.install()
