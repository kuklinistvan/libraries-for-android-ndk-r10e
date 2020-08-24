from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate

class LibidnConan(AutotoolsTemplate):
    def set_name(self):
        self.name = "libidn2"

    def set_version(self):
        self.version = "2.0.5"

    def configure(self):
        self.archive_url_prefix = "https://ftp.gnu.org/gnu/libidn/"
        self.setup_template_vars()

    def package_info(self):
        self.cpp_info.libs = ["idn2"]