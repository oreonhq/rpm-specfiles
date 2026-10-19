%global source0_hash 6e28d7cdd6dd513dd190e49bca3972e20fcf455090ccf2ef3f1a227614135d91
%global pybasever 3.6
%global pyshortver 36
Name: python%{pybasever}
Summary:        Version 3.6 of the Python interpreter
URL: https://www.python.org/
%global general_version %{pybasever}.15
%global upstream_version %{general_version}%{?prerel}
Version: %{general_version}%{?prerel:~%{prerel}}
Release:        1%{?dist}
License: LicenseRef-Callaway-Python AND LicenseRef-Callaway-MIT AND Apache-2.0 AND LicenseRef-Callaway-BSD AND ISC AND LicenseRef-Callaway-LGPLv2 AND MPL-2.0 AND (Apache-2.0 OR LicenseRef-Callaway-BSD)
%bcond_with main_python
%bcond_without flatpackage
%bcond_with rpmwheels
%ifarch %{ix86} x86_64
%bcond_without optimizations
%else
%bcond_with optimizations
%endif
%bcond_without tests
%if %{with flatpackage}
%bcond_with debug_build
%else
%bcond_without debug_build
%endif
%bcond_without gdb_hooks
%bcond_without gdbm
%bcond_without computed_gotos
%ifarch %{valgrind_arches}
%bcond_without valgrind
%else
%bcond_with valgrind
%endif
%if 0%{?fedora} >= 34 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%bcond_with legacy_archnames
%else
%bcond_without legacy_archnames
%endif
%global pkgname python%{pybasever}
%global pylibdir %{_libdir}/python%{pybasever}
%global dynload_dir %{pylibdir}/lib-dynload
%global ABIFLAGS_optimized m
%global ABIFLAGS_debug     dm
%global LDVERSION_optimized %{pybasever}%{ABIFLAGS_optimized}
%global LDVERSION_debug     %{pybasever}%{ABIFLAGS_debug}
%global platform_triplet_legacy %{_arch}-linux%{_gnu}
%global platform_triplet_upstream %{expand:%(echo %{platform_triplet_legacy} | sed -E \\
    -e 's/^arm(eb)?-linux-gnueabi$/arm\\1-linux-gnueabihf/' \\
    -e 's/^mips64(el)?-linux-gnu$/mips64\\1-linux-gnuabi64/' \\
    -e 's/^ppc(64)?(le)?-linux-gnu$/powerpc\\1\\2-linux-gnu/')}
%if %{with legacy_archnames}
%global platform_triplet %{platform_triplet_legacy}
%else
%global platform_triplet %{platform_triplet_upstream}
%endif
%global SOABI_optimized cpython-%{pyshortver}%{ABIFLAGS_optimized}-%{platform_triplet}
%global SOABI_debug     cpython-%{pyshortver}%{ABIFLAGS_debug}-%{platform_triplet}
%global bytecode_suffixes .cpython-%{pyshortver}*.pyc
%global libmpdec_version 2.4.2
%global py_SOVERSION 1.0
%global py_INSTSONAME_optimized libpython%{LDVERSION_optimized}.so.%{py_SOVERSION}
%global py_INSTSONAME_debug     libpython%{LDVERSION_debug}.so.%{py_SOVERSION}
%undefine py_auto_byte_compile
%if "%{_lib}" == "lib64"
%global wordsize 64
%else
%global wordsize 32
%endif
%undefine _include_frame_pointers
%if %{with gdbm}
%endif
%if %{with valgrind}
%endif
%if %{with rpmwheels}
%else
%endif
Source0:        https://www.python.org/ftp/python/%{general_version}/Python-%{general_version}.tar.xz
Source1: %{url}ftp/python/%{general_version}/Python-%{upstream_version}.tar.xz.asc
Source2: %{url}static/files/pubkeys.txt
Source8: check-pyc-timestamps.py
Source10: idle3.desktop
Source11: idle3.appdata.xml
Source101: pip-CVE-2007-4559.patch
Source102: setuptools-CVE-2024-6345.patch
Patch1: 00001-rpath.patch
Patch102: 00102-lib64.patch
Patch111: 00111-no-static-lib.patch
Patch132: 00132-add-rpmbuild-hooks-to-unittest.patch
Patch155: 00155-avoid-ctypes-thunks.patch
Patch160: 00160-disable-test_fs_holes-in-rpm-build.patch
Patch163: 00163-disable-parts-of-test_socket-in-rpm-build.patch
Patch170: 00170-gc-assertions.patch
Patch189: 00189-use-rpm-wheels.patch
%global pip_version 18.1
%global setuptools_version 40.6.2
Patch251: 00251-change-user-install-location.patch
Patch262: 00262-pep538_coerce_legacy_c_locale.patch
Patch292: 00292-restore-PyExc_RecursionErrorInst-symbol.patch
Patch294: 00294-define-TLS-cipher-suite-on-build-time.patch
Patch319: 00319-test_tarfile_ppc64.patch
Patch343: 00343-faulthandler-gcc10.patch
Patch353: 00353-architecture-names-upstream-downstream.patch
Patch358: 00358-align-allocations-and-pygc_head-to-16-bytes-on-64-bit-platforms.patch
Patch361: 00361-openssl-3-compatibility.patch
Patch375: 00375-fix-test_distance-to-enable-build-on-i686.patch
Patch378: 00378-support-expat-2-4-5.patch
Patch382: 00382-cve-2015-20107.patch
Patch386: 00386-cve-2021-28861.patch
Patch387: 00387-cve-2020-10735-prevent-dos-by-very-large-int.patch
Patch392: 00392-cve-2022-37454-fix-buffer-overflows-in-_sha3-module.patch
Patch394: 00394-cve-2022-45061-cpu-denial-of-service-via-inefficient-idna-decoder.patch
Patch397: 00397-pep-706-cve-2007-4559-filter-api-for-tarfile-extractall.patch
Patch399: 00399-cve-2023-24329.patch
Patch407: 00407-gh-99086-fix-implicit-int-compiler-warning-in-configure-check-for-pthread_scope_system.patch
Patch409: 00409-bpo-13497-fix-broken-nice-configure-test.patch
Patch410: 00410-bpo-42598-fix-implicit-function-declarations-in-configure.patch
Patch415: 00415-cve-2023-27043-gh-102988-reject-malformed-addresses-in-email-parseaddr-111116.patch
Patch419: 00419-gh-112769-test_zlib-fix-comparison-of-zlib_runtime_version-with-non-int-suffix-gh-112771-gh-112774.patch
Patch422: 00422-gh-115133-fix-tests-for-xmlpullparser-with-expat-2-6-0.patch
Patch423: 00423-bpo-33377-add-triplets-for-mips-r6-and-riscv.patch
Patch426: 00426-cve-2023-6597.patch
Patch427: 00427-zipextfile-tell-and-seek-cve-2024-0450.patch
Patch431: 00431-cve-2024-4032.patch
Patch435: 00435-gh-121650-encode-newlines-in-headers-and-verify.patch
Patch437: 00437-cve-2024-6232-remove-backtracking-when-parsing-tarfile-headers.patch
Patch443: 00443-gh-124651-quote-template-strings-in-venv-activation-scripts.patch
Patch444: 00444-security-fix-for-cve-2024-11168.patch
Patch446: 00446-Resolve-sinpi-name-clash-with-libm.patch
Patch450: 00450-cve-2025-0938-disallow-square-brackets-and-in-domain-names-for-parsed-urls.patch
Patch452: 00452-properly-apply-exported-cflags-for-dtrace-systemtap-builds.patch
Patch457: 00457-ssl-raise-oserror-for-err_lib_sys.patch
Patch465: 00465-tarfile-cves.patch
Patch467: 00467-tarfile-cve-2025-8194.patch
Patch473: 00473-cve-2026-0865.patch
Patch474: 00474-cve-2025-15366.patch
Patch475: 00475-cve-2025-15367.patch
Patch476: 00476-cve-2026-1299.patch
Patch471: 00471-cve-2025-12084.patch
Patch478: 00478-cve-2026-4519.patch
Provides:  python%{pyshortver} = %{version}-%{release}
Obsoletes: python%{pyshortver} < %{version}-%{release}
%if %{with main_python}
Provides: python(abi) = %{pybasever}
%else
%global __requires_exclude ^python\\(abi\\) = 3\\..+
%global __provides_exclude ^python\\(abi\\) = 3\\..+
%endif
%if %{without flatpackage}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: python%{pyshortver} = %{version}-%{release}
Obsoletes: python%{pyshortver}
Obsoletes: %{name} < 3.6.15-50
%if %{with main_python}
Recommends: python3-setuptools
Recommends: python3-pip
%endif
%global __requires_exclude ^/usr/bin/python3
# oreon:deps
BuildRequires:  /usr/bin/dtrace
BuildRequires:  /usr/sbin/ifconfig
BuildRequires:  autoconf
BuildRequires:  bluez-libs-devel
BuildRequires:  bzip2
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  gdbm-devel
BuildRequires:  git-core
BuildRequires:  glibc-all-langpacks
BuildRequires:  glibc-devel
BuildRequires:  gmp-devel
BuildRequires:  gnupg2
BuildRequires:  libGL-devel
BuildRequires:  libX11-devel
BuildRequires:  libappstream-glib
BuildRequires:  libffi-devel
BuildRequires:  libnsl2-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python-pip-wheel
BuildRequires:  python-setuptools-wheel
BuildRequires:  readline-devel
BuildRequires:  redhat-rpm-config
BuildRequires:  sqlite-devel
BuildRequires:  systemtap-sdt-devel
BuildRequires:  tar
BuildRequires:  tcl-devel
BuildRequires:  tix-devel
BuildRequires:  tk-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Python is an accessible, high-level, dynamically typed, interpreted programming
language, designed with an emphasis on code readability.
It includes an extensive standard library, and has a vast ecosystem of
third-party libraries.

The %{name} package provides the "python3" executable: the reference
interpreter for the Python language, version 3.
The majority of its standard library is provided in the %{name}-libs package,
which should be installed automatically along with %{name}.
The remaining parts of the Python standard library are broken out into the
%{name}-tkinter and %{name}-test packages, which may need to be installed
separately.

Documentation for Python is provided in the %{name}-docs package.

Packages containing additional libraries for Python are generally named with
the "%{name}-" prefix.

%package libs
Summary:        Python runtime libraries
%if %{with rpmwheels}
Requires: python-setuptools-wheel
Requires: python-pip-wheel
%else
Provides: bundled(python3dist(pip)) = 18.1
Provides: bundled(python3dist(appdirs)) = 1.4.3
Provides: bundled(python3dist(distlib)) = 0.2.7
Provides: bundled(python3dist(distro)) = 1.3
Provides: bundled(python3dist(html5lib)) = 1.0.1
Provides: bundled(python3dist(six)) = 1.11
Provides: bundled(python3dist(colorama)) = 0.3.9
Provides: bundled(python3dist(cachecontrol)) = 0.12.5
Provides: bundled(python3dist(msgpack-python)) = 0.5.6
Provides: bundled(python3dist(lockfile)) = 0.12.2
Provides: bundled(python3dist(progress)) = 1.4
Provides: bundled(python3dist(ipaddress)) = 1.0.22
Provides: bundled(python3dist(packaging)) = 18
Provides: bundled(python3dist(pep517)) = 0.2
Provides: bundled(python3dist(pyparsing)) = 2.2.1
Provides: bundled(python3dist(pytoml)) = 0.1.19
Provides: bundled(python3dist(retrying)) = 1.3.3
Provides: bundled(python3dist(requests)) = 2.19.1
Provides: bundled(python3dist(chardet)) = 3.0.4
Provides: bundled(python3dist(idna)) = 2.7
Provides: bundled(python3dist(urllib3)) = 1.23
Provides: bundled(python3dist(certifi)) = 2018.8.24
Provides: bundled(python3dist(setuptools)) = 40.4.3
Provides: bundled(python3dist(webencodings)) = 0.5.1
Provides: bundled(python3dist(setuptools)) = 40.6.2
Provides: bundled(python3dist(packaging)) = 16.8
Provides: bundled(python3dist(pyparsing)) = 2.2.1
Provides: bundled(python3dist(six)) = 1.10
Provides: bundled(python3dist(appdirs)) = 1.4.3
%endif
Provides: bundled(mpdecimal) = %{libmpdec_version}
Provides: bundled(libmpdec) = %{libmpdec_version}
Recommends: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: %{name} < 3.6.15-50
%description libs
This package contains runtime libraries for use by Python:
- the majority of the Python standard library
- a dynamically linked library for use by applications that embed Python as
  a scripting language, and by the main "python3" executable

%package devel
Summary: Libraries and header files needed for Python development
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: python-rpm-macros
Requires: (python-rpm-macros if rpm-build)
Requires: (python3-rpm-macros if rpm-build)
Requires: (python3-rpm-generators if rpm-build)
Provides: %{name}-2to3 = %{version}-%{release}
%if %{with main_python}
Provides: 2to3 = %{version}-%{release}
%endif
Conflicts: %{name} < %{version}-%{release}
Obsoletes: %{name} < 3.6.15-50
%description devel
This package contains the header files and configuration needed to compile
Python extension modules (typically written in C or C++), to embed Python
into other programs, and to make binary distributions for Python libraries.

It also contains the necessary macros to build RPM packages with Python modules
and 2to3 tool, an automatic source converter from Python 2.X.

%package idle
Summary: A basic graphical development environment for Python
Requires: %{name} = %{version}-%{release}
Requires: %{name}-tkinter = %{version}-%{release}
%if %{with main_python}
Provides: idle3 = %{version}-%{release}
%endif
Provides: %{name}-tools = %{version}-%{release}
Provides: %{name}-tools%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-tools < %{version}-%{release}
Obsoletes: %{name} < 3.6.15-50
%description idle
IDLE is Python’s Integrated Development and Learning Environment.

IDLE has the following features: Python shell window (interactive
interpreter) with colorizing of code input, output, and error messages;
multi-window text editor with multiple undo, Python colorizing,
smart indent, call tips, auto completion, and other features;
search within any window, replace within editor windows, and
search through multiple files (grep); debugger with persistent
breakpoints, stepping, and viewing of global and local namespaces;
configuration, browsers, and other dialogs.

%package tkinter
Summary: A GUI toolkit for Python
Requires: %{name} = %{version}-%{release}
Obsoletes: %{name} < 3.6.15-50
%description tkinter
The Tkinter (Tk interface) library is a graphical user interface toolkit for
the Python programming language.

%package test
Summary: The self-test suite for the main python3 package
Requires: %{name} = %{version}-%{release}
Obsoletes: %{name} < 3.6.15-50
%description test
The self-test suite for the Python interpreter.

This is only useful to test Python itself. For testing general Python code,
you should use the unittest module from %{name}-libs, or a library such as
%{name}-pytest or %{name}-nose.

%if %{with debug_build}
%package debug
Summary: Debug version of the Python runtime
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-test%{?_isa} = %{version}-%{release}
Requires: %{name}-tkinter%{?_isa} = %{version}-%{release}
Requires: %{name}-idle%{?_isa} = %{version}-%{release}
%description debug
python3-debug provides a version of the Python runtime with numerous debugging
features enabled, aimed at advanced Python users such as developers of Python
extension modules.

This version uses more memory and will be slower than the regular Python build,
but is useful for tracking down reference-counting issues and other bugs.

The bytecode format is unchanged, so that .pyc files are compatible between
this and the standard version of Python, but the debugging features mean that
C/C++ extension modules are ABI-incompatible and must be built for each version
separately.

The debug build shares installation directories with the standard Python
runtime, so that .py and .pyc files can be shared.
Compiled extension modules use a special ABI flag ("d") in the filename,
so extensions for both versions can co-exist in the same directory.
%endif # with debug_build

%else  # with flatpackage

%if %{with rpmwheels}
Requires: python-setuptools-wheel
Requires: python-pip-wheel
%else
# Versions of bundled libs are based on:
# https://github.com/pypa/pip/blob/18.1/src/pip/_vendor/vendor.txt and
# https://github.com/pypa/setuptools/blob/v40.6.2/pkg_resources/_vendor/vendored.txt
Provides: bundled(python3dist(pip)) = %{pip_version}
Provides: bundled(python3dist(appdirs)) = 1.4.3
Provides: bundled(python3dist(distlib)) = 0.2.7
Provides: bundled(python3dist(distro)) = 1.3
Provides: bundled(python3dist(html5lib)) = 1.0.1
Provides: bundled(python3dist(six)) = 1.11
Provides: bundled(python3dist(colorama)) = 0.3.9
Provides: bundled(python3dist(cachecontrol)) = 0.12.5
Provides: bundled(python3dist(msgpack-python)) = 0.5.6
Provides: bundled(python3dist(lockfile)) = 0.12.2
Provides: bundled(python3dist(progress)) = 1.4
Provides: bundled(python3dist(ipaddress)) = 1.0.22
Provides: bundled(python3dist(packaging)) = 18
Provides: bundled(python3dist(pep517)) = 0.2
Provides: bundled(python3dist(pyparsing)) = 2.2.1
Provides: bundled(python3dist(pytoml)) = 0.1.19
Provides: bundled(python3dist(retrying)) = 1.3.3
Provides: bundled(python3dist(requests)) = 2.19.1
Provides: bundled(python3dist(chardet)) = 3.0.4
Provides: bundled(python3dist(idna)) = 2.7
Provides: bundled(python3dist(urllib3)) = 1.23
Provides: bundled(python3dist(certifi)) = 2018.8.24
Provides: bundled(python3dist(setuptools)) = 40.4.3
Provides: bundled(python3dist(webencodings)) = 0.5.1

Provides: bundled(python3dist(setuptools)) = %{setuptools_version}
Provides: bundled(python3dist(packaging)) = 16.8
Provides: bundled(python3dist(pyparsing)) = 2.2.1
Provides: bundled(python3dist(six)) = 1.10
Provides: bundled(python3dist(appdirs)) = 1.4.3
%endif

# Provides for the bundled libmpdec
Provides: bundled(mpdecimal) = %{libmpdec_version}
Provides: bundled(libmpdec) = %{libmpdec_version}

# Provides of the subpackages contained in flatpackage
Provides: %{pkgname}-libs = %{version}-%{release}
Provides: %{pkgname}-devel = %{version}-%{release}
Provides: %{pkgname}-idle = %{version}-%{release}
Provides: %{pkgname}-tkinter = %{version}-%{release}
Provides: %{pkgname}-test = %{version}-%{release}
%if %{with debug_build}
Provides: %{pkgname}-debug = %{version}-%{release}
%endif

# The description for the flat package
%description
Python %{pybasever} package for developers.

This package exists to allow developers to test their code against an older
version of Python. This is not a full Python stack and if you wish to run
your applications with Python %{pybasever}, see other distributions
that support it, such as CentOS or RHEL with Software Collections
or older Fedora releases.

%endif # with flatpackage

# ======================================================
# The prep phase of the build:
# ======================================================

%prep

%gpgverify -k2 -s1 -d0
%autosetup -S git_am -N -n Python-%{upstream_version}

# Apply initial patches manually
%autopatch 1

%if "%{_lib}" == "lib64"
%autopatch 102
%endif

%autopatch 111
%autopatch 132
%autopatch 155
%autopatch 160
%autopatch 163
%autopatch 170

%if %{with rpmwheels}
%autopatch 189
rm Lib/ensurepip/_bundled/*.whl
%else
# Patch the bundled pip wheel for CVE-2007-4559
unzip -qq Lib/ensurepip/_bundled/pip-%{pip_version}-py2.py3-none-any.whl
patch -p1 < %{SOURCE101}
zip -rq Lib/ensurepip/_bundled/pip-%{pip_version}-py2.py3-none-any.whl pip pip-%{pip_version}.dist-info
rm -rf pip/ pip-%{pip_version}.dist-info/

# Patch the bundled setuptools wheel for CVE-2024-6345
unzip -qq Lib/ensurepip/_bundled/setuptools-%{setuptools_version}-py2.py3-none-any.whl
patch -p1 < %{SOURCE102}
zip -rq Lib/ensurepip/_bundled/setuptools-%{setuptools_version}-py2.py3-none-any.whl easy_install.py pkg_resources setuptools setuptools-%{setuptools_version}.dist-info
rm -rf easy_install.py pkg_resources/ setuptools/ setuptools-%{setuptools_version}.dist-info/
%endif

# Apply the remaining patches
%autopatch -m 190

# Remove bundled libraries to ensure that we're using the system copy.
rm -r Modules/expat
rm -r Modules/zlib

# Remove files that should be generated by the build
# (This is after patching, so that we can use patches directly from upstream)
rm configure pyconfig.h.in

# When we use the legacy arch names, we need to change them in configure.ac
%if %{with legacy_archnames}
sed -i configure.ac \
    -e 's/\b%{platform_triplet_upstream}\b/%{platform_triplet_legacy}/'
%endif

# ======================================================
# Configuring and building the code:
# ======================================================

%build

export HAS_GIT=not-found
autoconf
autoheader
topdir=$(pwd)
%if %{with computed_gotos}
%global computed_gotos_flag yes
%else
%global computed_gotos_flag no
%endif
%if %{with optimizations}
%global optimizations_flag "--enable-optimizations"
%else
%global optimizations_flag "--disable-optimizations"
%endif
export CFLAGS="%{extension_cflags}"
export CFLAGS_NODIST="%{build_cflags} -D_GNU_SOURCE -fPIC -fwrapv"
export CXXFLAGS="%{extension_cxxflags}"
export CPPFLAGS="$(pkg-config --cflags-only-I libffi)"
export OPT="%{extension_cflags}"
export LINKCC="gcc"
export CFLAGS="$CFLAGS $(pkg-config --cflags openssl)"
export LDFLAGS="%{extension_ldflags} $(pkg-config --libs-only-L openssl)"
export LDFLAGS_NODIST="%{build_ldflags} -g $(pkg-config --libs-only-L openssl)"
BuildPython() {
  ConfName=$1
  ExtraConfigArgs=$2
  MoreCFlags=$3
  ConfDir=build/$ConfName
  echo STARTING: BUILD OF PYTHON FOR CONFIGURATION: $ConfName
  mkdir -p $ConfDir
  pushd $ConfDir
  %global _configure $topdir/configure
%configure \
  --enable-ipv6 \
  --enable-shared \
  --with-computed-gotos=%{computed_gotos_flag} \
  --with-dbmliborder=gdbm:ndbm:bdb \
  --with-system-expat \
  --with-system-ffi \
  --enable-loadable-sqlite-extensions \
  --with-dtrace \
  --with-lto \
  --with-ssl-default-suites=openssl \
%if %{with valgrind}
  --with-valgrind \
%endif
  $ExtraConfigArgs \
  %{nil}
  %make_build EXTRA_CFLAGS="$CFLAGS $MoreCFlags" regen-importlib
  %make_build EXTRA_CFLAGS="$CFLAGS $MoreCFlags"
  popd
  echo FINISHED: BUILD OF PYTHON FOR CONFIGURATION: $ConfName
}
%if %{with debug_build}
BuildPython debug \
  "--without-ensurepip --with-pydebug" \
  "-O0"
%endif # with debug_build
BuildPython optimized \
  "--without-ensurepip %{optimizations_flag}" \
  ""
%install
topdir=$(pwd)
%if %{with gdb_hooks}
DirHoldingGdbPy=%{_prefix}/lib/debug/%{_libdir}
mkdir -p %{buildroot}$DirHoldingGdbPy
%endif # with gdb_hooks
%global _pyconfig32_h pyconfig-32.h
%global _pyconfig64_h pyconfig-64.h
%global _pyconfig_h pyconfig-%{wordsize}.h
InstallPython() {
  ConfName=$1
  PyInstSoName=$2
  MoreCFlags=$3
  LDVersion=$4
  ConfDir=build/$ConfName
  echo STARTING: INSTALL OF PYTHON FOR CONFIGURATION: $ConfName
  mkdir -p $ConfDir
  pushd $ConfDir
  %make_install EXTRA_CFLAGS="$MoreCFlags"
  popd
%if %{with gdb_hooks}
  PathOfGdbPy=$DirHoldingGdbPy/$PyInstSoName-%{version}-%{release}.%{_arch}.debug-gdb.py
  cp Tools/gdb/libpython.py %{buildroot}$PathOfGdbPy
%endif # with gdb_hooks
  mv %{buildroot}%{_bindir}/python${LDVersion}-{,`uname -m`-}config
  echo -e '#!/bin/sh\nexec `dirname $0`/python'${LDVersion}'-`uname -m`-config "$@"' > \
    %{buildroot}%{_bindir}/python${LDVersion}-config
  echo '[ $? -eq 127 ] && echo "Could not find python'${LDVersion}'-`uname -m`-config. Look around to see available arches." >&2' >> \
    %{buildroot}%{_bindir}/python${LDVersion}-config
    chmod +x %{buildroot}%{_bindir}/python${LDVersion}-config
  mv %{buildroot}%{_includedir}/python${LDVersion}/pyconfig.h \
     %{buildroot}%{_includedir}/python${LDVersion}/%{_pyconfig_h}
  cat > %{buildroot}%{_includedir}/python${LDVersion}/pyconfig.h << EOF
EOF
  echo FINISHED: INSTALL OF PYTHON FOR CONFIGURATION: $ConfName
}
%if %{with debug_build}
InstallPython debug \
  %{py_INSTSONAME_debug} \
  -O0 \
  %{LDVERSION_debug}
%endif # with debug_build
InstallPython optimized \
  %{py_INSTSONAME_optimized} \
  "" \
  %{LDVERSION_optimized}
install -d -m 0755 %{buildroot}%{pylibdir}/site-packages/__pycache__
%if "%{_lib}" == "lib64"
install -d -m 0755 %{buildroot}%{_prefix}/lib/python%{pybasever}/site-packages/__pycache__
%endif
%if %{with main_python}
install -D -m 0644 Lib/idlelib/Icons/idle_16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/idle3.png
install -D -m 0644 Lib/idlelib/Icons/idle_32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/idle3.png
install -D -m 0644 Lib/idlelib/Icons/idle_48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/idle3.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE10}
mkdir -p %{buildroot}%{_metainfodir}
cp -a %{SOURCE11} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/idle3.appdata.xml
%endif
sed -i -e "s/'pyconfig.h'/'%{_pyconfig_h}'/" \
  %{buildroot}%{pylibdir}/distutils/sysconfig.py \
  %{buildroot}%{pylibdir}/sysconfig.py
cp -p Tools/scripts/pathfix.py %{buildroot}%{_bindir}/
for tool in pygettext msgfmt; do
  cp -p Tools/i18n/${tool}.py %{buildroot}%{_bindir}/${tool}%{pybasever}.py
  ln -s ${tool}%{pybasever}.py %{buildroot}%{_bindir}/${tool}3.py
done
LD_LIBRARY_PATH=./build/optimized ./build/optimized/python \
  Tools/scripts/pathfix.py \
  -i "%{_bindir}/python%{pybasever}" -pn \
  %{buildroot} \
  %{buildroot}%{_bindir}/*%{pybasever}.py \
  %{?with_gdb_hooks:%{buildroot}$DirHoldingGdbPy/*.py}
rm -rf %{buildroot}%{pylibdir}/test/test_tools
find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)
find %{buildroot} -name \*.bat -exec rm {} \;
find %{buildroot}/ -name "*~" -exec rm -f {} \;
find . -name "*~" -exec rm -f {} \;
%if 0%{?clamp_mtime_to_source_date_epoch}
LD_LIBRARY_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
PYTHONPATH="%{_rpmconfigdir}/redhat" \
%{buildroot}%{_bindir}/python%{pybasever} -s -B -m clamp_source_mtime %{buildroot}%{pylibdir}
%endif
find %{buildroot} -type f -a -name "*.py" -print0 | \
    LD_LIBRARY_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
    PYTHONPATH="%{buildroot}%{_libdir}/python%{pybasever} %{buildroot}%{_libdir}/python%{pybasever}/site-packages" \
    xargs -0 %{buildroot}%{_bindir}/python%{pybasever} -O -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("%{buildroot}")[2], optimize=opt) for opt in range(3) for f in sys.argv[1:]]' || :
rm -rf %{buildroot}%{_bindir}/__pycache__
find %{buildroot} -perm 555 -exec chmod 755 {} \;
%if %{with debug_build} && %{with main_python}
ln -s \
  %{_bindir}/python%{LDVERSION_debug} \
  %{buildroot}%{_bindir}/python3-debug
%endif
%if %{without rpmwheels}
%{?python_wheel_inject_sbom:%python_wheel_inject_sbom %{buildroot}%{pylibdir}/ensurepip/_bundled/*.whl}
%endif
%if %{without main_python}
rm %{buildroot}%{_bindir}/python3
rm %{buildroot}%{_bindir}/pydoc3
rm %{buildroot}%{_bindir}/pathfix.py
rm %{buildroot}%{_bindir}/pygettext3.py
rm %{buildroot}%{_bindir}/msgfmt3.py
rm %{buildroot}%{_bindir}/idle3
rm %{buildroot}%{_bindir}/python3-*
rm %{buildroot}%{_bindir}/pyvenv
rm %{buildroot}%{_bindir}/2to3*
rm %{buildroot}%{_libdir}/libpython3.so
rm %{buildroot}%{_mandir}/man1/python3.1*
rm %{buildroot}%{_libdir}/pkgconfig/python3.pc
%oreon_autofiles main
%endif
%check

find %{buildroot} -type f -a -name "*.py" -print0 | \
    LD_LIBRARY_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
    PYTHONPATH="%{buildroot}%{_libdir}/python%{pybasever} %{buildroot}%{_libdir}/python%{pybasever}/site-packages" \
    xargs -0 %{buildroot}%{_bindir}/python%{pybasever} %{SOURCE8}
ldd %{buildroot}/%{dynload_dir}/_curses*.so \
    | grep curses \
    | grep libncurses.so && (echo "_curses.so linked against libncurses.so" ; exit 1)
for Module in %{buildroot}/%{dynload_dir}/*.so ; do
    case $Module in
    *.%{SOABI_debug})
        ldd $Module | grep %{py_INSTSONAME_optimized} &&
            (echo Debug module $Module linked against optimized %{py_INSTSONAME_optimized} ; exit 1)
        ;;
    *.%{SOABI_optimized})
        ldd $Module | grep %{py_INSTSONAME_debug} &&
            (echo Optimized module $Module linked against debug %{py_INSTSONAME_debug} ; exit 1)
        ;;
    esac
done
test "$(LD_LIBRARY_PATH=$(pwd)/build/optimized $(pwd)/build/optimized/python -c 'import decimal; print(decimal.__libmpdec_version__)')" = \
     "%{libmpdec_version}"
topdir=$(pwd)
CheckPython() {
  ConfName=$1
  ConfDir=$(pwd)/build/$ConfName
  export OPENSSL_CONF=/non-existing-file
  echo STARTING: CHECKING OF PYTHON FOR CONFIGURATION: $ConfName
  WITHIN_PYTHON_RPM_BUILD= \
  LD_LIBRARY_PATH=$ConfDir $ConfDir/python -m test.regrtest \
    -wW --slowest --findleaks \
    -x test_distutils \
    -x test_bdist_rpm \
    -x test_gdb \
    %ifarch ppc64le aarch64
    -x test_faulthandler \
    %endif
    %ifarch %{mips64}
    -x test_ctypes \
    %endif
    %ifarch ppc64le
    -x test_buffer \
    %endif
  echo FINISHED: CHECKING OF PYTHON FOR CONFIGURATION: $ConfName
}
%if %{with tests}
%if %{with debug_build}
CheckPython debug
%endif # with debug_build
CheckPython optimized
%endif # with tests
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
