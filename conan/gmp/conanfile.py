from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate

class ConanfileImpl(AutotoolsTemplate):
    def set_name(self):
        self.name = "gmp"

    def set_version(self):
        self.version = "6.2.0"

    def configure(self):
        self.archive_url_prefix = "https://gmplib.org/download/gmp/"
        self.setup_template_vars()
