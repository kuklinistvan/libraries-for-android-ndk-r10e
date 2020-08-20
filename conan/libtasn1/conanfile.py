from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate
import os

class GmpConan(AutotoolsTemplate):
    def set_name(self):
        self.name = "libtasn1"

    def set_version(self):
        self.version = "4.16.0"

    def configure(self):
        self.archive_url_prefix = "https://ftp.gnu.org/gnu/libtasn1/"
        self.setup_template_vars()

    def package(self):
        os.environ['CFLAGS'] = '-std=c99'
        super().package()