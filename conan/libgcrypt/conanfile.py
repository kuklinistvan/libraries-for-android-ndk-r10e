from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate
from pykuklin.shellutils import working_directory, Path, shell

class ConanfileImpl(AutotoolsTemplate):
    requires = "libgpg-error/1.39"
    exports_sources = "have_pthread_yes.patch"

    def set_name(self):
        self.name = "libgcrypt"

    def set_version(self):
        self.version = "1.8.6"

    def source(self):
        super().source()

        with working_directory(Path(self.topdir)):
            # shell(["bash"])
            shell(['patch', '-i', '../have_pthread_yes.patch'])
            shell(['./autogen.sh'])
        
    def configure(self):
        self.archive_url_prefix = "https://gnupg.org/ftp/gcrypt/libgcrypt/"
        self.archive_format_file_suffix = ".tar.bz2"
        self.setup_template_vars()

    def package_info(self):
        self.cpp_info.libs = ["gcrypt"]

