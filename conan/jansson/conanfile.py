from conans import ConanFile, CMake, AutoToolsBuildEnvironment
from pykuklin.downloader import get_downloader_available_in_current_environment, Path
from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate
from pykuklin.conan.tools import build_env_vars_set

downloader = get_downloader_available_in_current_environment()

class ConanfileImpl(AutotoolsTemplate):
    fpic_env = {'CXXFLAGS': '-fPIC', 'CFLAGS': '-fPIC'}

    def set_name(self):
        self.name = "jansson"

    def set_version(self):
        self.version = "2.12"

    def configure(self):
        with build_env_vars_set(self, additional_vars_to_merge=self.fpic_env):
            self.archive_format_file_suffix = ".tar.bz2"
            self.archive_url_prefix = "http://digip.org/jansson/releases/"
            self.setup_template_vars()

    def package(self):       
        autotools = AutoToolsBuildEnvironment(self)

        with build_env_vars_set(self, append_libdirs_to_rpath = True, additional_vars_to_merge=self.fpic_env):
            autotools.configure(configure_dir=self.topdir, args=self.configure_additional_args)
            autotools.make(target=self.topdir)
            autotools.install()

