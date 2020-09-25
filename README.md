# Conan libraries for Android NDK r10e

As an effort to support reusing old Android devices, I'm publishing my package recipe archive.

As of writing, it contains only the library [Ulfius 2.6.5](https://github.com/babelouest/ulfius) and all of its intermediate dependencies. With this bundle I was able to compile a simple test program and run from ADB shell that creates a REST API from my phone. I was also able to forward this API to my machine through ADB.

## Architectures

I'm targeting ARM CPUs without a dedicated FPU (also called sometimes "soft float" CPUs). In theory, you can recompile these libraries against other versions of NDK as well.
