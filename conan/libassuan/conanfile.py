from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate

class ConanfileImpl(AutotoolsTemplate):
    def set_name(self):
        self.name = "libassuan"

    def set_version(self):
        self.version = "2.5.3"

    def configure(self):
        self.archive_url_prefix = "https://gnupg.org/ftp/gcrypt/libassuan/"
        self.archive_format_file_suffix = ".tar.bz2"
        self.setup_template_vars()

    def package_info(self):
        self.cpp_info.libs = ["assuan"]