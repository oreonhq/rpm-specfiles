%global source0_hash none

%global uvcommit af4172ec713ee986ba1a989b9e33993a07c60c9e
%global uvversion 1.48.0

%global llvmversion 18.1.7
%global llvmsoversion 18.1jl
%global llvmcommit julia-18.1.7-4

%global libwhichversion 1.2.0
%global libwhichcommit 99a0ea12689e41164456dba03e93bc40924de880

%global blastrampolineversion 5.15.0
%global blastrampolinecommit 072b5f67895bec0b92f8c83194567c1c48e9833d

%global libunwindversion 1.8.1

%global ittapiversion 3.24.0
%global ittapicommit 0014aec56fea2f30c1374f40861e1bccdd53d0cb

# Bundled as Julia carries patches which turn abort into an exception
# https://github.com/JuliaLang/julia/pull/31215
%global gmpversion 6.3.0

%global juliasyntaxcommit 46723f071d5b2efcb21ca6757788028afb91cc13
%global juliasyntaxhighlightingcommit b666d3c98cca30d20d1e6f98c0e12c9350ffbc4c

%global logocommit 168fb6c1164e341df360ed6ced519e1e0cb7de3a

# List all bundled libraries here
# OpenBLAS is excluded because we set a symlink to libopenblasp
%global _privatelibs lib(openblas_|openblas64_|ccalltest|llvmcalltest|LLVM-.*|uv|blastrampoline|unwind|gmp|gmpxx)\\.so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

# Some binaries confuse debuginfo check
%undefine _missing_build_ids_terminate_build

Name:           julia
Version:        1.12.1
Release:        2%{?dist}
Summary:        High-level, high-performance dynamic language for technical computing
# Julia itself is MIT
# libuv, libwhich, libblastrampoline and libunwind are MIT
# LLVM is Apache-2.0 WITH LLVM-exception
License:        MIT and Apache-2.0 WITH LLVM-exception
URL:            http://julialang.org/
Source0:        https://github.com/JuliaLang/julia/releases/download/v%{version}/julia-%{version}.tar.gz
# Julia currently uses a custom version of libuv, patches are not yet upstream
Source1:        https://api.github.com/repos/JuliaLang/libuv/tarball/%{uvcommit}#/libuv-%{uvcommit}.tar.gz
Source2:        https://api.github.com/repos/JuliaLang/llvm-project/tarball/%{llvmcommit}#/llvm-%{llvmcommit}.tar.gz
Source3:        https://api.github.com/repos/vtjnash/libwhich/tarball/%{libwhichcommit}#/libwhich-%{libwhichcommit}.tar.gz
Source4:        https://gmplib.org/download/gmp/gmp-%{gmpversion}.tar.bz2
Source5:        https://api.github.com/repos/JuliaLang/JuliaSyntax.jl/tarball/%{juliasyntaxcommit}#/JuliaSyntax-%{juliasyntaxcommit}.tar.gz
Source6:        https://raw.githubusercontent.com/JuliaLang/julia-logo-graphics/%{logocommit}/images/julia-logo-color.svg
Source7:        https://api.github.com/repos/staticfloat/libblastrampoline/tarball/%{blastrampolinecommit}#/blastrampoline-%{blastrampolinecommit}.tar.gz
Source8:        https://github.com/libunwind/libunwind/releases/download/v%{libunwindversion}/libunwind-%{libunwindversion}.tar.gz
Source9:        https://api.github.com/repos/intel/ittapi/tarball/%{ittapicommit}#/ittapi-%{ittapicommit}.tar.gz
Source10:       https://api.github.com/repos/JuliaLang/JuliaSyntaxHighlighting.jl/tarball/%{juliasyntaxhighlightingcommit}#/JuliaSyntaxHiglighting-%{juliasyntaxhighlightingcommit}.tar.gz
# https://gmplib.org/repo/gmp/rev/8e7bb4ae7a18
Patch0:         julia-gmp-6.3.0-c23.patch
# https://github.com/JuliaLang/julia/pull/59998
Patch1:         julia-avoid-hardcoding-paths-in-Profile.patch
Provides:       bundled(libuv) = %{uvversion}
Provides:       bundled(llvm) = %{llvmversion}
Provides:       bundled(libblastrampoline) = %{blastrampolineversion}
Provides:       bundled(libwhich) = %{libwhichversion}
Provides:       bundled(libunwind) = %{libunwindversion}
Provides:       bundled(ittapi) = %{ittapiversion}
Provides:       bundled(gmp) = %{gmpversion}
BuildRequires:  ca-certificates
BuildRequires:  desktop-file-utils
BuildRequires:  dSFMT-devel
BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel >= 6.0
# Needed for libgit2 test
BuildRequires:  hostname
BuildRequires:  ImageMagick
BuildRequires:  libatomic
BuildRequires:  libunwind-devel >= 1.8
BuildRequires:  openblas-devel
BuildRequires:  openblas-threads
BuildRequires:  openlibm-devel >= 0.4
BuildRequires:  libgit2-devel
# Needed for libgit2 test
BuildRequires:  openssl
BuildRequires:  libssh2-devel
BuildRequires:  openssl-devel
BuildRequires:  libcurl-devel
BuildRequires:  libcurl-full
BuildRequires:  libnghttp2-devel
BuildRequires:  curl-full
BuildRequires:  pcre2-devel
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mpfr-devel >= 4
# Needed to build gmp
BuildRequires:  m4
# Needed to build gmp with julia-gmp-6.3.0-c23.patch
BuildRequires: autoconf automake libtool
BuildRequires:  patchelf
BuildRequires:  perl
BuildRequires:  7zip-standalone
%if 0%{?__isa_bits} == 64
BuildRequires:  suitesparse64_-devel >= 7.6
%else
BuildRequires:  suitesparse-devel >= 7.6
%endif
BuildRequires:  utf8proc-devel >= 2.1
BuildRequires:  zlib-devel
Requires:       julia-common = %{version}-%{release}
Requires:       ca-certificates
# For terminfo files
Requires:       ncurses-base
Requires:       7zip-standalone
# Libraries used by CompilerSupportLibraries_jll and blastrampoline
# but not detected as they are dlopen()ed but not linked to
%if 0%{?__isa_bits} == 64
Requires:       libgfortran.so.5()(64bit)
Requires:       libgomp.so.1()(64bit)
Requires:       libopenblasp64_.so.0()(64bit)
Requires:       libquadmath.so.0()(64bit)
Requires:       suitesparse64_
%else
Requires:       libgfortran.so.5
Requires:       libgomp.so.1
Requires:       libopenblasp.so.0
Requires:       libquadmath.so.0
Requires:       suitesparse
%endif
# https://bugzilla.redhat.com/show_bug.cgi?id=1158026
# https://github.com/JuliaLang/julia/issues/30087
ExclusiveArch:  x86_64

%description
Julia is a high-level, high-performance dynamic programming language
for technical computing, with syntax that is familiar to users of
other technical computing environments. It provides a sophisticated
compiler, distributed parallel execution, numerical accuracy, and an
extensive mathematical function library. The library, largely written
in Julia itself, also integrates mature, best-of-breed C and Fortran
libraries for linear algebra, random number generation, signal processing,
and string processing.

This package only contains the essential parts of the Julia environment:
the julia executable and the standard library.

%package common
Summary:        Julia architecture-independent files
BuildArch:      noarch
Requires:       julia = %{version}-%{release}

%description common
Contains architecture-independent files required to run Julia.

%package doc
Summary:        Julia documentation and code examples
BuildArch:      noarch
Requires:       julia = %{version}-%{release}

%description doc
Contains the Julia manual, the reference documentation of the standard library
and code examples.

%package devel
Summary:        Julia development, debugging and testing files
Requires:       julia%{?_isa} = %{version}-%{release}

%description devel
Contains library symbolic links and header files for developing applications
linking to the Julia library, in particular embedding it, as well as
tests. This package is normally not
needed when programming in the Julia language, but rather for embedding
Julia into external programs or debugging Julia itself.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n julia-%{version}

# Need to reset time stamps set manually to their original values in the diff
# to prevent make from regenerating docs, which involves downloading files
patch -p1 -T < %PATCH1

mkdir -p deps/srccache stdlib/srccache

pushd deps/srccache
    # Julia downloads tarballs for external dependencies even when the folder is present:
    # we need to copy the tarball and let the build process unpack it
    # https://github.com/JuliaLang/julia/pull/10280
    cp -p %SOURCE1 .
    cp -p %SOURCE2 .
    cp -p %SOURCE3 .
    cp -p %SOURCE4 .
    cp -p %SOURCE5 .
    cp -p %SOURCE7 .
    cp -p %SOURCE8 .
    cp -p %SOURCE9 .
    cp -p %SOURCE10 .
popd

cp -p %SOURCE6 contrib/julia.svg

# Required so that the image is not optimized for the build CPU
# (i386 does not work yet: https://github.com/JuliaLang/julia/issues/7185)
# Without specifying MARCH, the Julia system image would only work on native CPU
# CPU targets reflect those used upstream at
# https://github.com/JuliaCI/julia-buildbot/blob/master/master/inventory.py
%ifarch %{ix86}
%global march MARCH=pentium4
%global cpu_target JULIA_CPU_TARGET="pentium4;sandybridge,-xsaveopt,clone_all"
%endif
%ifarch x86_64
%global march MARCH=x86-64
%global cpu_target JULIA_CPU_TARGET="generic;sandybridge,-xsaveopt,clone_all;haswell,-rdrnd,base(1)"
%endif
%ifarch %{arm}
# gcc and LLVM do not support the same targets
%global march MARCH=$(echo %build_cflags | grep -Po 'march=\\K[^ ]*')
%global cpu_target JULIA_CPU_TARGET="generic"
%endif
%ifarch armv7hl
%global march MARCH=$(echo %build_cflags | grep -Po 'march=\\K[^ ]*')
%global cpu_target JULIA_CPU_TARGET="armv7-a;armv7-a,neon;armv7-a,neon,vfp4"
%endif
%ifarch aarch64
%global march MARCH=armv8-a
%global cpu_target JULIA_CPU_TARGET="generic"
%endif
%ifarch ppc64le
%global march %{nil}
%global cpu_target JULIA_CPU_TARGET="pwr8"
%endif

# Use the non-threaded OpenBLAS library name internally to match what Julia uses so that
# libraries built using BinaryBuilder (like Arpack.jl) work
# We symlink it to libopenblasp below so that threads are used in the end
%if 0%{?__isa_bits} == 64
%global blas USE_BLAS64=1 OPENBLAS_SYMBOLSUFFIX=64_ LIBBLAS=-lopenblas64_ LIBBLASNAME=libopenblas64_ LIBLAPACK=-lopenblas64_ LIBLAPACKNAME=libopenblas64_
%else
%global blas LIBBLAS=-lopenblas LIBBLASNAME=libopenblas LIBLAPACK=-lopenblas LIBLAPACKNAME=libopenblas
%endif

%if 0%{?__isa_bits} == 64
%global suitesparse_lib SUITESPARSE_LIB="-lumfpack64_ -lcholmod64_ -lamd64_ -lcamd64_ -lcolamd64_ -lspqr64_"
%else
%global suitesparse_lib SUITESPARSE_LIB="-lumfpack -lcholmod -lamd -lcamd -lcolamd -lspqr"
%endif

%if 0%{?el7}
%global cmake CMAKE=cmake3
%else
%global cmake CMAKE=cmake
%endif

# About build, build_libdir and build_bindir, see https://github.com/JuliaLang/julia/issues/5063#issuecomment-32628111
%global commonopts USE_SYSTEM_LLVM=0 USE_SYSTEM_LIBUNWIND=0 USE_SYSTEM_PCRE=1 USE_SYSTEM_BLAS=1 USE_SYSTEM_LAPACK=1 USE_SYSTEM_GMP=0 USE_SYSTEM_MPFR=1 USE_SYSTEM_LIBSUITESPARSE=1 USE_SYSTEM_DSFMT=1 USE_SYSTEM_LIBUV=0 USE_SYSTEM_UTF8PROC=1 USE_SYSTEM_LIBGIT2=1 USE_SYSTEM_LIBSSH2=1 USE_SYSTEM_OPENSSL=1 USE_SYSTEM_CURL=1 USE_SYSTEM_PATCHELF=1 USE_SYSTEM_LIBM=0 USE_SYSTEM_OPENLIBM=1 USE_SYSTEM_ZLIB=1 USE_SYSTEM_P7ZIP=1 USE_SYSTEM_NGHTTP2=1 USE_SYSTEM_CSL=1 USE_SYSTEM_LIBBLASTRAMPOLINE=0 USE_SYSTEM_LIBWHICH=0 USE_BINARYBUILDER=0 USE_BINARYBUILDER_LLVM=0 WITH_TERMINFO=0 BUNDLE_DEBUG_LIBS=0 JULIA_SPLITDEBUG=1 TAGGED_RELEASE_BANNER="Fedora %{fedora} build" VERBOSE=1 %{march} %{cpu_target} %{blas} %{suitesparse_lib} prefix=%{_prefix} bindir=%{_bindir} libdir=%{_libdir} libexecdir=%{_libexecdir} datarootdir=%{_datarootdir} includedir=%{_includedir} sysconfdir=%{_sysconfdir} build_prefix=%{_builddir}/%{buildsubdir}/build%{_prefix} build_libdir=%{_builddir}/%{buildsubdir}/build%{_libdir} JULIA_CPU_THREADS=$(echo %{?_smp_mflags} | sed s/-j//)

make %{commonopts} -C deps extract-gmp
pushd deps/srccache/gmp-%{gmpversion}
    %patch -p1 0
    autoreconf -ifv
popd


%build
# LTO currently makes building blastrampoline and Julia itself fail
# It is not enabled upstream anyway
%global _lto_cflags %nil

# Workaround to build LLVM with GCC 15:
# https://github.com/JuliaLang/julia/issues/58478#issuecomment-3161411290
%global build_cxxflags %(echo "%{build_cxxflags} -include cstdint")

# Julia hardcodes the exact SOVERSION it uses when USE_SYSTEM_*=0
# https://github.com/JuliaLang/julia/pull/38347#discussion_r574819534
sed "s/libopenlibm.so.*\"/$(cd %{_libdir} && ls libopenlibm.so.?)\"/" -i stdlib/OpenLibm_jll/src/OpenLibm_jll.jl
sed "s/libgit2.so.*\"/$(cd %{_libdir} && ls -1 libgit2.so.?.? | sort -nr | head -n1)\"/" -i stdlib/LibGit2_jll/src/LibGit2_jll.jl
sed "/VersionNumber/s/v\".*\"/v\"$(pkg-config --modversion libgit2)\"/" -i stdlib/LibGit2_jll/test/runtests.jl

# Disable test that fails because Julia process doesn't error as expected
sed "s/mktempdir() do pfx/false \&\& mktempdir() do pfx/" -i Compiler/test/codegen.jl

# Increase tolerance as times on build machines are not very reliable
sed "s/after_comp - before_comp < 6_000_000_000/after_comp - before_comp < 600_000_000_000/" -i test/misc.jl

# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%ifarch %{arm} %{ix86}
%global build_cflags %(echo %{build_cflags} | sed 's/-g /-g1 /')
%global build_cxxflags %(echo %{build_cxxflags} | sed 's/-g /-g1 /')
%global build_ldflags %(echo %{build_ldflags} | sed 's/-g /-g1 /')
%endif

%ifarch %{ix86}
# Need to repeat -march here to override i686 from build_cflags
%global buildflags CFLAGS="%{build_cflags} -march=pentium4" CXXFLAGS="%{build_cxxflags} -march=pentium4" FFLAGS="%{build_fflags} -march=pentium4" LDFLAGS="%{build_ldflags}"
%else
%global buildflags CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" FFLAGS="%{build_fflags}" LDFLAGS="%{build_ldflags}"
%endif

# 7z currently fails when called from a symlink, use 7za instead
# https://bugzilla.redhat.com/show_bug.cgi?id=2373874
mkdir -p %{_builddir}/%{buildsubdir}/build/%{_bindir}/
ln -sf /usr/bin/7za %{_builddir}/%{buildsubdir}/build/%{_bindir}/7z

# Workaround LLVM being installed in lib and not found
mkdir -p %{_builddir}/%{buildsubdir}/build/%{_libdir}/
pushd %{_builddir}/%{buildsubdir}/build/%{_libdir}
    ln -sf ../lib/libLLVM.so.%{llvmsoversion} libLLVM.so.%{llvmsoversion}
popd

make %{?_smp_mflags} %{commonopts} release

# Now copy LLVM from lib to lib64
if [ "x%{_lib}" != xlib ] ; then
  rm -f %{_builddir}/%{buildsubdir}/build/%{_libdir}/libLLVM.so.%{llvmsoversion}
  cp -a %{_builddir}/%{buildsubdir}/build/usr/lib/* %{_builddir}/%{buildsubdir}/build/%{_libdir}
  rm -rf %{_builddir}/%{buildsubdir}/build/usr/lib/
  ln -sf %{_lib} %{_builddir}/%{buildsubdir}/build/usr/lib
fi

# Use CA certificates from ca-certificates
# (Mozilla certificates are not installed anyway when USE_SYSTEM_LIBGIT2=1)
# https://github.com/JuliaLang/julia/commit/5dc6201e8dccbf21aeeb1f79fef2d186c7800a4e#r47032178
ln -sf /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem %{_builddir}/%{buildsubdir}/build/%{_datarootdir}/julia/cert.pem

# Disable tests that require Internet access
sed "s/ipa = getipaddr()/error()/" -i test/choosetests.jl

# Too many threads/processes can trigger memory issues in cmdlineargs test
%ifarch %{ix86}
sed "s/cpu_threads = max(2\*cpu_threads, min(200, 10\*cpu_threads))/cpu_threads = 5/" -i test/cmdlineargs.jl
%endif

## Disable tests that fail on build machines (but not locally)
sed -i 's/skip_tests = Set()/skip_tests = Set(["loading", "cmdlineargs"])/' test/choosetests.jl

# Julia hardcodes the exact SOVERSION it uses when USE_SYSTEM_*=0
# https://github.com/JuliaLang/julia/pull/38347#discussion_r574819534
sed "s/@test vn == v\".*\"//" -i stdlib/PCRE2_jll/test/runtests.jl
sed "s/@test vn == v\".*\"//" -i stdlib/GMP_jll/test/runtests.jl
sed "s/@test vn == v\".*\"//" -i stdlib/MPFR_jll/test/runtests.jl
sed "s/@test VersionNumber\(.*\) == v\".*\"//" -i stdlib/Zlib_jll/test/runtests.jl
sed "s/@test VersionNumber(unsafe_string(info.version_str)) == v\".*\"//" -i stdlib/nghttp2_jll/test/runtests.jl
sed "s/@test .*SuiteSparse_version.*==.*//" -i stdlib/SuiteSparse_jll/test/runtests.jl
sed "s/@test VersionNumber\(.*\) == v\".*\"//" -i stdlib/OpenSSL_jll/test/runtests.jl


%install
make %{commonopts} DESTDIR=%{buildroot} install

pushd %{buildroot}%{_libdir}/julia
    %if 0%{?__isa_bits} == 64
        rm -f libopenblas64_.so
        ln -s %{_libdir}/libopenblasp64_.so.0 libopenblas64_.so
        ln -s %{_libdir}/libopenblasp64_.so.0 libopenblas64_.so.0
        # Raise an error in case of changing files
        test -e %{_libdir}/libopenblasp64_.so.0

        # Julia creates unversioned symlinks to SuiteSparse libraries linking to libopenblas rather than libopenblas64_
        # and it does not create versioned symlinks needed to dlopen() libraries using their unsuffixed names
        for LIB in spqr umfpack colamd cholmod ccolamd camd amd suitesparseconfig btf klu ldl rbio
        do
            rm -f lib${LIB}.so
            LIBVER64=$(readelf -d %{_libdir}/lib${LIB}64_.so | sed -n '/SONAME/s/.*\(lib[^ ]*\.so\.[0-9]*\).*/\1/p')
            LIBVER=$(echo ${LIBVER64} | sed -n 's/64_//p')
            ln -s %{_libdir}/${LIBVER64} lib${LIB}.so
            ln -s %{_libdir}/${LIBVER64} ${LIBVER}
            # Raise an error in case of changing files
            test -e %{_libdir}/lib${LIB}.so
        done
    %else
        rm -f libopenblas.so
        ln -s %{_libdir}/libopenblasp.so.0 libopenblas.so
        ln -s %{_libdir}/libopenblasp.so.0 libopenblas.so.0
        # Raise an error in case of changing files
        test -e %{_libdir}/libopenblasp.so.0
    %endif
popd

# Prevent find-debuginfo from touching precompiled caches as it
# changes checksums, which invalidates them
chmod -x %{buildroot}%{_datarootdir}/julia/compiled/*/*/*.so

# Prevent find-debuginfo from touching these libraries as it somehow corrupts them,
# giving "object has no loadable segments" when starting Julia
chmod -x %{buildroot}%{_libdir}/julia/libjulia-internal*
chmod -x %{buildroot}%{_libdir}/julia/libjulia-codegen*

# Prevent find-debuginfo from touching sysimage as debugging information is needed
# for stacktraces in Julia code, which makes tests fail
chmod -x %{buildroot}%{_libdir}/julia/sys.so

cp -p CONTRIBUTING.md LICENSE.md NEWS.md README.md %{buildroot}%{_docdir}/julia/

pushd %{buildroot}%{_libdir}/julia
    # Some Julia packages rely on being able to use libjulia, but we only
    # ship %%{_libdir}/libjulia.so in the -devel package
    ln -s ../libjulia.so.1.*.* libjulia.so
    # Raise an error in case of failure
    realpath -e libjulia.so

    # Needed when USE_SYSTEM_CSL=1
    # https://github.com/JuliaLang/julia/issues/39637
    ln -sf %{_libdir}/libgcc_s.so.1 libgcc_s.so.1
    # Raise an error in case of changing files
    test -e %{_libdir}/libgcc_s.so.1
popd

# Use CA certificates from ca-certificates
# (Mozilla certificates are not installed anyway when USE_SYSTEM_LIBGIT2=1)
# https://github.com/JuliaLang/julia/commit/5dc6201e8dccbf21aeeb1f79fef2d186c7800a4e#r47032178
ln -sf /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem %{buildroot}%{_datarootdir}/julia/cert.pem

# Install .desktop file and icons
mkdir -p %{buildroot}%{_datarootdir}/icons/hicolor/scalable/apps/
mkdir -p %{buildroot}%{_datarootdir}/icons/hicolor/16x16/apps/
mkdir -p %{buildroot}%{_datarootdir}/icons/hicolor/24x24/apps/
mkdir -p %{buildroot}%{_datarootdir}/icons/hicolor/32x32/apps/
mkdir -p %{buildroot}%{_datarootdir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}%{_datarootdir}/icons/hicolor/256x256/apps/
cp -p contrib/julia.svg %{buildroot}%{_datarootdir}/icons/hicolor/scalable/apps/%{name}.svg
magick contrib/julia.svg -scale 16x16 -extent 16x16 -gravity center -background transparent \
    %{buildroot}%{_datarootdir}/icons/hicolor/16x16/apps/%{name}.png
magick contrib/julia.svg -scale 24x24 -extent 24x24 -gravity center -background transparent \
    %{buildroot}%{_datarootdir}/icons/hicolor/24x24/apps/%{name}.png
magick contrib/julia.svg -scale 32x32 -extent 32x32 -gravity center -background transparent \
    %{buildroot}%{_datarootdir}/icons/hicolor/32x32/apps/%{name}.png
magick contrib/julia.svg -scale 48x48 -extent 48x48 -gravity center -background transparent \
    %{buildroot}%{_datarootdir}/icons/hicolor/48x48/apps/%{name}.png
magick contrib/julia.svg  -scale 256x256 -extent 256x256 -gravity center -background transparent \
    %{buildroot}%{_datarootdir}/icons/hicolor/256x256/apps/%{name}.png
desktop-file-validate %{buildroot}%{_datarootdir}/applications/%{name}.desktop


%check
# Run tests within Julia from the buildroot as it is closer to a test of the final install
# In particular it ensures the libopenblas64_.so symlink created above is used,
# which isn't the case with the directory layout of the build directory
# JULIA_TEST_USE_MULTIPLE_WORKERS=true enables running tests in parallel despite net_on=false
JULIA_TEST_USE_MULTIPLE_WORKERS=true %{buildroot}%{_bindir}/julia -e "Base.runtests()"


%files
%dir %{_docdir}/julia/
%{_docdir}/julia/LICENSE.md
%doc %{_docdir}/julia/CONTRIBUTING.md
%doc %{_docdir}/julia/NEWS.md
%doc %{_docdir}/julia/README.md
%{_bindir}/julia
%{_libdir}/julia/
%{_libexecdir}/julia/
%exclude %{_libdir}/julia/*debug*
%{_libdir}/libjulia.so.*
%{_datarootdir}/julia/compiled/*/*/*.ji
%{_datarootdir}/julia/compiled/*/*/*.so
%{_mandir}/man1/julia.1*
%{_datarootdir}/metainfo/julia.appdata.xml
%{_datarootdir}/applications/%{name}.desktop
%{_datarootdir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datarootdir}/icons/hicolor/16x16/apps/%{name}.png
%{_datarootdir}/icons/hicolor/24x24/apps/%{name}.png
%{_datarootdir}/icons/hicolor/32x32/apps/%{name}.png
%{_datarootdir}/icons/hicolor/48x48/apps/%{name}.png
%{_datarootdir}/icons/hicolor/256x256/apps/%{name}.png

%files common
%dir %{_datarootdir}/julia/
%{_datarootdir}/julia/*.jl
%{_datarootdir}/julia/base/
%{_datarootdir}/julia/Compiler/
%{_datarootdir}/julia/juliac/
%{_datarootdir}/julia/stdlib/
%{_datarootdir}/julia/base.cache
%{_datarootdir}/julia/cert.pem
# files in testhelpers/ subdirectory are needed to precompile sysimages
%{_datarootdir}/julia/test/

%dir %{_sysconfdir}/julia/
%config(noreplace) %{_sysconfdir}/julia/startup.jl

%files doc
%doc %{_docdir}/julia/

%files devel
%{_libdir}/libjulia.so
%{_libdir}/julia/libjulia-internal.so
%{_libdir}/julia/libjulia-codegen.so
%{_libdir}/julia/libccalltest.so.debug
%{_includedir}/julia/

%post
/sbin/ldconfig
/bin/touch --no-create %{_datarootdir}/icons/hicolor &>/dev/null || :
exit 0

%changelog
%autochangelog

