from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate

class CurlConan(AutotoolsTemplate):
    def configure(self):
        self.name = "curl"
        self.version = "7.71.1"
        self.archive_url_prefix = "https://curl.haxx.se/download/"
        self.setup_template_vars()