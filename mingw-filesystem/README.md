Building the MinGW environment
==============================

Build order:

- mingw-filesystem
- mingw-binutils
- mingw-headers (bundle_dummy_pthread_headers=1)
- mingw-w64-tools
- mingw-gcc (bootstrap=1)
- mingw-crt (bootstrap=1)
- mingw-crt (bootstrap=0)
- mingw-winpthreads
- mingw-headers (bundle_dummy_pthread_headers=0)
- mingw-gcc (bootstrap=0)
- mingw-gdb
