from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate

from conans import RunEnvironment
from conans.tools import environment_append

from conans.model.build_info import DepsCppInfo


class ConanfileImpl(AutotoolsTemplate):
    requires = "gmp/6.2.0", "nettle/3.5.1", "libtasn1/4.16.0", "libunistring/0.9.10"

    def set_name(self):
        self.name = "gnutls"

    def set_version(self):
        self.version = "3.6.12"

    def configure(self):
        self.archive_url_prefix = "https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/"
        self.archive_format_file_suffix = ".tar.xz"
        self.configure_additional_args += [
            '--without-p11-kit',
            '--disable-cxx',
            '--disable-tests',
            '--disable-guile',
            '--enable-local-libopts',
            '--disable-doc',
            '--with-included-unistring',
            '--with-pic'
        ]

        super().configure()

    def package(self):
        pkg_config_path = {
            'PKG_CONFIG_PATH':
                self.deps_cpp_info["nettle"].rootpath + "/lib/pkgconfig:" +
                self.deps_cpp_info["libtasn1"].rootpath + "/lib/pkgconfig"
        }

        with environment_append(RunEnvironment(self).vars), environment_append(pkg_config_path):
            super().package()
