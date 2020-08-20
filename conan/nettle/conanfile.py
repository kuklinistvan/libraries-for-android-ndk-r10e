from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate

class ConanfileImpl(AutotoolsTemplate):
    def set_name(self):
        self.name = "nettle"

    def set_version(self):
        self.version = "3.5.1"

    def configure(self):
        self.archive_url_prefix = "https://ftp.gnu.org/gnu/nettle/"
        self.setup_template_vars()