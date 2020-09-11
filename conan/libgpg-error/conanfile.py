from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate

class ConanfileImpl(AutotoolsTemplate):
    def set_name(self):
        self.name = "libgpg-error"

    def set_version(self):
        self.version = "1.39"

    def configure(self):
        self.archive_url_prefix = "https://gnupg.org/ftp/gcrypt/libgpg-error/"
        self.archive_format_file_suffix = ".tar.bz2"
        self.setup_template_vars()

    def package_info(self):
        self.cpp_info.libs = ["gpg-error"]
        self.cpp_info.sharedlinkflags = ["-lgpg-error"]