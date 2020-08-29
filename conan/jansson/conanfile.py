from conans import ConanFile, CMake
from pykuklin.downloader import get_downloader_available_in_current_environment, Path
from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate

downloader = get_downloader_available_in_current_environment()

class ConanfileImpl(AutotoolsTemplate):
    def set_name(self):
        self.name = "jansson"

    def set_version(self):
        self.version = "2.12"

    def configure(self):
        self.archive_format_file_suffix = ".tar.bz2"
        self.archive_url_prefix = "http://digip.org/jansson/releases/"
        self.setup_template_vars()

