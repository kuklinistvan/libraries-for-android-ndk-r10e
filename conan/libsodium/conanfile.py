from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate
from pykuklin.downloader import curl, Path
import os
from subprocess import call

class LibsodiumConan(AutotoolsTemplate):
    def set_name(self):
        self.name = "libsodium"

    def set_version(self):
        self.version = "1.0.18"

    def configure(self):
        self.setup_template_vars()
        self.topdir = "libsodium-stable"

    def source(self):
        tgz_name = "libsodium-{}-stable.tar.gz".format(self.version)
        target = Path(os.getcwd()) / tgz_name
        url = "https://download.libsodium.org/libsodium/releases/{t}".format(t=tgz_name)

        curl(url, target)
        assert 0 == call(['tar', 'xvf', str(target)])

    def package_info(self):
        self.cpp_info.libs = ["sodium"]