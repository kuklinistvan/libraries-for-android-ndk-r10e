from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate

class LibmicrohttpdConan(AutotoolsTemplate):

    def __init__(self, output, runner, display_name="", user=None, channel=None):
        super().__init__(output, runner, display_name, user, channel)
        self.add_fpic = True

    def set_name(self):
        self.name = "libmicrohttpd"

    def set_version(self):
        self.version = "0.9.70"

    def configure(self):
        self.configure_additional_args = ['--disable-examples', '--enable-static']
        self.archive_url_prefix = "https://ftp.gnu.org/gnu/libmicrohttpd/"
        self.setup_template_vars()

    def package_info(self):
        self.cpp_info.libs = ["microhttpd"]