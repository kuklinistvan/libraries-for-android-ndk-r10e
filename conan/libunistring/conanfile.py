from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate

class ConanfileImpl(AutotoolsTemplate):
    def set_name(self):
        self.name = "libunistring"

    def set_version(self):
        self.version = "0.9.10"

    def configure(self):
        self.archive_url_prefix = "https://ftp.gnu.org/gnu/libunistring/"
        self.setup_template_vars()

    def package_info(self):
        self.cpp_info.libs = ["unistring"]
