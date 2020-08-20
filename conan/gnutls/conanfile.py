from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate

class ConanfileImpl(AutotoolsTemplate):
    # DEPENDENCIES

    def set_name(self):
        self.name = "gnutls"

    def set_version(self):
        self.version = "3.6.12"

    def configure(self):
        self.archive_url_prefix = "https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/"
        self.archive_format_file_suffix = ".tar.xz"
        self.setup_template_vars()
        self.configure_additional_args = [
            '--without-p11-kit',
            '--disable-cxx',
            '--disable-tests',
            '--disable-guile'
        ]