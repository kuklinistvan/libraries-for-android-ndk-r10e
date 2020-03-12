# Static libraries for Android NDK r10e

As an effort to support reusing old Android devices, I'm publishing my package archive that can be installed on Arch Linux for development.

You can link your NDK-compiled programs and libraries against these libraries either statically or dynamically without compiling them first by hand, if you find what you're looking for among them.

As of writing, it contains only the library [Ulfius 2.6.5](https://github.com/babelouest/ulfius) and all of its intermediate dependencies. With this bundle I was able to compile a simple test program and run from ADB shell that creates a REST API from my phone. I was also able to forward this API to my machine through ADB.

From now on, when I'm compiling another library for old Android, I'm going to consider extending this archive of `PKGBUILD`s.

## Architectures

I'm targeting ARM CPUs without a dedicated FPU (also called sometimes "soft float" CPUs). In theory, you can recompile these libraries against other versions of NDK as well.

## Folder structure

Under `src/` the packages can be found and their `PKGBUILD` scripts. Under `pkgs/` there's a handy tool named `collect.sh` that moves all the built packages into that particular directory.