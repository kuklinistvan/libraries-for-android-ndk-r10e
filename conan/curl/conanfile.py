from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate

class CurlConan(AutotoolsTemplate):
    def set_name(self):
        self.name = "curl"

    def set_version(self):
        self.version = "7.71.1"

    def configure(self):        
        self.archive_url_prefix = "https://curl.haxx.se/download/"
        self.setup_template_vars()