from pykuklin.conan.templates.AutotoolsTemplate import AutotoolsTemplate

class ConanfileImpl(AutotoolsTemplate):  
    def set_name(self):
        self.name = "gnutls"

    def set_version(self):
        self.version = "3.6.12"

    def requirements(self):
        self.requires("gmp/[>= 6.2.0]")
        self.requires("nettle/[>= 3.5.1]")
        self.requires("libtasn1/[>= 4.16.0]")
        self.requires("libunistring/[>= 0.9.10]")

    def configure(self):
        self.archive_url_prefix = "https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/"
        self.archive_format_file_suffix = ".tar.xz"
        self.setup_template_vars()
        self.configure_additional_args = [
            '--without-p11-kit',
            '--disable-cxx',
            '--disable-tests',
            '--disable-guile',
            '--enable-local-libopts',
            '--disable-doc'
        ]