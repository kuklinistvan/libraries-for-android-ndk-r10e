from conans import ConanFile, CMake
from pykuklin.downloader import get_downloader_available_in_current_environment, Path

downloader = get_downloader_available_in_current_environment()

class ConanFileImpl(ConanFile):
    name = "jansson"
    version = "2.12"

    def source(self):
        basename = "jansson-{}.tar.gz".format(self.version)
        url = "http://www.digip.org/jansson/releases/" + basename
        downloader(url, Path(basename))
        self.run("tar xvf " + str(basename))

    def build(self):
        sf = self.name + '-' + self.version

        cmake = CMake(self)
        cmake.configure(source_folder=sf)
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
