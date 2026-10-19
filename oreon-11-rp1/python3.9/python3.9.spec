%global source2_hash b7cecb5218f65828b8e782934784493c0c1819418d423b81bd0b2529fa5d1a17
%global source1_hash 6120fadaa1f4bd3f80ae0313e9c03b4c4ea069a3cec1398027d2465057fb258a
%global source0_hash 00e07d7c0f2f0cc002432d1ee84d2a40dae404a99303e3f97701c10966c91834
%global pybasever 3.9
%global pyshortver 39
Name: python%{pybasever}
Summary:        Version 3.9 of the Python interpreter
URL: https://www.python.org/
%global general_version %{pybasever}.25
%global upstream_version %{general_version}%{?prerel}
Version: %{general_version}%{?prerel:~%{prerel}}
Release:        1%{?dist}
License: Python
%if "%{?__default_python3_pkgversion}" == "%{pybasever}"
%bcond_without main_python
%else
%bcond_with main_python
%endif
%bcond_without flatpackage
%bcond_with bootstrap
%bcond_without rpmwheels
%bcond_without optimizations
%bcond_without no_semantic_interposition
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
%bcond_with rhel8_compat_shims
%if %{with main_python}
%global pkgname python3
%global exename python3
%else
%global pkgname python%{pybasever}
%global exename python%{pybasever}
%endif
%global pylibdir %{_libdir}/python%{pybasever}
%global dynload_dir %{pylibdir}/lib-dynload
%global ABIFLAGS_optimized %{nil}
%global ABIFLAGS_debug     d
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
%global libmpdec_version 2.5.0
%global py_SOVERSION 1.0
%global py_INSTSONAME_optimized libpython%{LDVERSION_optimized}.so.%{py_SOVERSION}
%global py_INSTSONAME_debug     libpython%{LDVERSION_debug}.so.%{py_SOVERSION}
%undefine py_auto_byte_compile
%if %{with main_python} && ("%{?__default_python3_pkgversion}" != "%{pybasever}")
%undefine __pythonname_provides
%{warn:Doing a main_python build with wrong %%__default_python3_pkgversion (0%{?__default_python3_pkgversion}, but this is %pyshortver)}
%endif
%undefine _include_frame_pointers
%if %{with gdbm}
%endif
%if %{with valgrind}
%endif
%if %{with rpmwheels}
%else
%endif
%if %{without bootstrap}
%endif
Source0:        https://www.python.org/ftp/python/3.9.25/Python-3.9.25.tar.xz
Source1:        https://www.python.org/ftp/python/3.9.25/Python-3.9.25.tar.xz.asc
Source2: https://keybase.io/ambv/pgp_keys.asc
Source8: check-pyc-timestamps.py
Source10: idle3.desktop
Source11: idle3.appdata.xml
Patch1: 00001-rpath.patch
Patch111: 00111-no-static-lib.patch
Patch189: 00189-use-rpm-wheels.patch
%global pip_version 23.0.1
%global setuptools_version 79.0.1
Patch251: 00251-change-user-install-location.patch
Patch353: 00353-architecture-names-upstream-downstream.patch
Patch371: 00371-revert-bpo-1596321-fix-threading-_shutdown-for-the-main-thread-gh-28549-gh-28589.patch
Patch407: 00407-gh-99086-fix-implicit-int-compiler-warning-in-configure-check-for-pthread_scope_system.patch
Patch452: 00452-properly-apply-exported-cflags-for-dtrace-systemtap-builds.patch
Patch471: 00471-cve-2025-12084.patch
Patch473: 00473-cve-2026-0865.patch
Patch474: 00474-cve-2025-15366.patch
Patch475: 00475-cve-2025-15367.patch
Patch476: 00476-cve-2026-1299.patch
%if %{without flatpackage}
%if %{with main_python}
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
BuildRequires:  libuuid-devel
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
BuildRequires:  tzdata
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Python %{pybasever} is an accessible, high-level, dynamically typed, interpreted
programming language, designed with an emphasis on code readability.
It includes an extensive standard library, and has a vast ecosystem of
third-party libraries.

%package -n %{pkgname}
Summary: Python %{pybasever} interpreter
Provides: python%{pybasever} = %{version}-%{release}
Provides: python%{pybasever}%{?_isa} = %{version}-%{release}
Obsoletes: python%{pybasever} < %{version}-%{release}
Recommends: %{_bindir}/python
%endif
Provides: python%{pyshortver} = %{version}-%{release}
Obsoletes: python%{pyshortver} < %{version}-%{release}
Obsoletes: %{pkgname} < 3.9.24-2
%if %{with main_python}
Provides: python(abi) = %{pybasever}
%else
%global __requires_exclude ^python\\(abi\\) = 3\\..+
%global __provides_exclude ^python\\(abi\\) = 3\\..+
%endif
Requires: %{pkgname}-libs%{?_isa} = %{version}-%{release}
Recommends: %{pkgname}-setuptools
Recommends: %{pkgname}-pip
%global __requires_exclude ^(/usr/bin/python3|python\\(abi\\))
%description -n %{pkgname}
Python %{pybasever} is an accessible, high-level, dynamically typed, interpreted
programming language, designed with an emphasis on code readability.
It includes an extensive standard library, and has a vast ecosystem of
third-party libraries.

The %{pkgname} package provides the "%{exename}" executable: the reference
interpreter for the Python language, version 3.
The majority of its standard library is provided in the %{pkgname}-libs package,
which should be installed automatically along with %{pkgname}.
The remaining parts of the Python standard library are broken out into the
%{pkgname}-tkinter and %{pkgname}-test packages, which may need to be installed
separately.

Documentation for Python is provided in the %{pkgname}-docs package.

Packages containing additional libraries for Python are generally named with
the "%{pkgname}-" prefix.

%if %{with main_python}
# https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package
# https://fedoraproject.org/wiki/Changes/Python_means_Python3
%package -n python-unversioned-command
Summary: The "python" command that runs Python 3
BuildArch: noarch
Requires: python3 == %{version}-%{release}
Provides: python = %{version}-%{release}
Provides: python-is-python3 = %{version}-%{release}
%description -n python-unversioned-command
This package contains /usr/bin/python - the "python" command that runs Python 3.

%endif

%package -n %{pkgname}-libs
Summary:        Python runtime libraries
%if %{with rpmwheels}
Requires: python-setuptools-wheel
Requires: python-pip-wheel
%else
Provides: bundled(python3dist(pip)) = %{pip_version}
Provides: bundled(python3dist(setuptools)) = %{setuptools_version}
%endif
Provides: bundled(mpdecimal) = %{libmpdec_version}
Provides: bundled(libmpdec) = %{libmpdec_version}
Recommends: %{pkgname}%{?_isa} = %{version}-%{release}
Recommends: (%{pkgname}-tkinter%{?_isa} = %{version}-%{release} if tk%{?_isa})
Requires: tzdata
Requires: expat >= 2.6
Conflicts: python-libs < 3
Obsoletes: %{pkgname} < 3.9.24-2
%description -n %{pkgname}-libs
This package contains runtime libraries for use by Python:
- the majority of the Python standard library
- a dynamically linked library for use by applications that embed Python as
  a scripting language, and by the main "%{exename}" executable

%package -n %{pkgname}-devel
Summary: Libraries and header files needed for Python development
Requires: %{pkgname} = %{version}-%{release}
Requires: %{pkgname}-libs%{?_isa} = %{version}-%{release}
Requires: (python-rpm-macros if rpm-build)
Requires: (python3-rpm-macros if rpm-build)
Requires: (pyproject-rpm-macros if rpm-build)
%if %{without bootstrap}
%if %{with main_python}
Requires: (%{pkgname}-setuptools if rpm-build)
%endif
Requires: (python3-rpm-generators if rpm-build)
%endif
Provides: %{pkgname}-2to3 = %{version}-%{release}
Provides: 2to3 = %{version}-%{release}
Conflicts: %{pkgname} < %{version}-%{release}
Conflicts: python-devel < 3
Obsoletes: %{pkgname} < 3.9.24-2
%description -n %{pkgname}-devel
This package contains the header files and configuration needed to compile
Python extension modules (typically written in C or C++), to embed Python
into other programs, and to make binary distributions for Python libraries.

It also contains the necessary macros to build RPM packages with Python modules
and 2to3 tool, an automatic source converter from Python 2.X.

%package -n %{pkgname}-idle
Summary: A basic graphical development environment for Python
Requires: %{pkgname} = %{version}-%{release}
Requires: %{pkgname}-tkinter = %{version}-%{release}
Provides: idle3 = %{version}-%{release}
Provides: idle = %{version}-%{release}
Provides: %{pkgname}-tools = %{version}-%{release}
Provides: %{pkgname}-tools%{?_isa} = %{version}-%{release}
Obsoletes: %{pkgname}-tools < %{version}-%{release}
Conflicts: python-tools < 3
Obsoletes: %{pkgname} < 3.9.24-2
%description -n %{pkgname}-idle
IDLE is Python’s Integrated Development and Learning Environment.

IDLE has the following features: Python shell window (interactive
interpreter) with colorizing of code input, output, and error messages;
multi-window text editor with multiple undo, Python colorizing,
smart indent, call tips, auto completion, and other features;
search within any window, replace within editor windows, and
search through multiple files (grep); debugger with persistent
breakpoints, stepping, and viewing of global and local namespaces;
configuration, browsers, and other dialogs.

%package -n %{pkgname}-tkinter
Summary: A GUI toolkit for Python
Requires: %{pkgname} = %{version}-%{release}
%py_provides %{pkgname}-turtle
Obsoletes: %{pkgname} < 3.9.24-2
%description -n %{pkgname}-tkinter
The Tkinter (Tk interface) library is a graphical user interface toolkit for
the Python programming language.

%package -n %{pkgname}-test
Summary: The self-test suite for the main python3 package
Requires: %{pkgname} = %{version}-%{release}
Requires: %{pkgname}-libs%{?_isa} = %{version}-%{release}
Obsoletes: %{pkgname} < 3.9.24-2
%description -n %{pkgname}-test
The self-test suite for the Python interpreter.

This is only useful to test Python itself. For testing general Python code,
you should use the unittest module from %{pkgname}-libs, or a library such as
%{pkgname}-pytest.

%if %{with debug_build}
%package -n %{pkgname}-debug
Summary: Debug version of the Python runtime
Requires: %{pkgname}%{?_isa} = %{version}-%{release}
Requires: %{pkgname}-libs%{?_isa} = %{version}-%{release}
Requires: %{pkgname}-devel%{?_isa} = %{version}-%{release}
Requires: %{pkgname}-test%{?_isa} = %{version}-%{release}
Requires: %{pkgname}-tkinter%{?_isa} = %{version}-%{release}
Requires: %{pkgname}-idle%{?_isa} = %{version}-%{release}
Conflicts: python-debug < 3
%description -n %{pkgname}-debug
python3-debug provides a version of the Python runtime with numerous debugging
features enabled, aimed at advanced Python users such as developers of Python
extension modules.

This version uses more memory and will be slower than the regular Python build,
but is useful for tracking down reference-counting issues and other bugs.

The debug build shares installation directories with the standard Python
runtime. Python modules -- source (.py), bytecode (.pyc), and C-API extensions
(.cpython*.so) -- are compatible between this and the standard version
of Python.

The debug runtime additionally supports debug builds of C-API extensions
(with the "d" ABI flag) for debugging issues in those extensions.
%endif

%else

# Python interpreter packages used to be named (or provide) name pythonXY (e.g.
# python39). However, to align it with the executable names and to prepare for
# Python 3.10, they were renamed to pythonX.Y (e.g. python3.9, python3.10). We
# provide and obsolete the previous names.
# - Here are the tags for the flat package. For the nonflat package, the
#   provide is repeated many lines above.
Provides: python%{pyshortver} = %{version}-%{release}
Obsoletes: python%{pyshortver} < %{version}-%{release}

%if %{with rpmwheels}
Requires: python-setuptools-wheel
Requires: python-pip-wheel
%else
Provides: bundled(python3dist(pip)) = %{pip_version}
Provides: bundled(python3dist(setuptools)) = %{setuptools_version}
%endif

# Provides for the bundled libmpdec
Provides: bundled(mpdecimal) = %{libmpdec_version}
Provides: bundled(libmpdec) = %{libmpdec_version}

# The zoneinfo module needs tzdata
Requires: tzdata

# The requirement on libexpat is generated, but we need to version it.
# When built with expat >= 2.6, but installed with older expat, we get:
#   ImportError: /usr/lib64/python3.X/lib-dynload/pyexpat.cpython-....so:
#   undefined symbol: XML_SetReparseDeferralEnabled
# This breaks many things, including python -m venv.
# Other subpackages (like -debug) also need this, but they all depend on -libs.
Requires: expat >= 2.6

# Provides of the subpackages contained in flatpackage
Provides: %{pkgname}-libs = %{version}-%{release}
Provides: %{pkgname}-devel = %{version}-%{release}
Provides: %{pkgname}-idle = %{version}-%{release}
Provides: %{pkgname}-tkinter = %{version}-%{release}
Provides: %{pkgname}-test = %{version}-%{release}
%if %{with debug_build}
Provides: %{pkgname}-debug = %{version}-%{release}
%endif

# The description for the flat package (SRPM and built)
%description
Python %{pybasever} package for developers.

This package exists to allow developers to test their code against an older
version of Python. This is not a full Python stack and if you wish to run
your applications with Python %{pybasever}, see other distributions
that support it, such as CentOS or RHEL or older Fedora releases.

%endif

# ======================================================
# The prep phase of the build:
# ======================================================

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%gpgverify -k2 -s1 -d0
%autosetup -S git_am -N -n Python-%{upstream_version}

# Apply patches up to 188
%autopatch -M 188

%if %{with rpmwheels}
%autopatch 189
rm Lib/ensurepip/_bundled/*.whl
%endif

# Apply the remaining patches
%autopatch -m 190

# Remove all exe files to ensure we are not shipping prebuilt binaries
# note that those are only used to create Microsoft Windows installers
# and that functionality is broken on Linux anyway
find -name '*.exe' -print -delete

# Remove bundled libraries to ensure that we're using the system copy.
rm -r Modules/expat

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
export CFLAGS_NODIST="%{build_cflags} -D_GNU_SOURCE -fPIC -fwrapv%{?with_no_semantic_interposition: -fno-semantic-interposition}"
export CXXFLAGS="%{extension_cxxflags}"
export CPPFLAGS="$(pkg-config --cflags-only-I libffi)"
export OPT="%{extension_cflags}"
export LINKCC="gcc"
export CFLAGS="$CFLAGS $(pkg-config --cflags openssl)"
export LDFLAGS="%{extension_ldflags} $(pkg-config --libs-only-L openssl)"
export LDFLAGS_NODIST="%{build_ldflags}%{?with_no_semantic_interposition: -fno-semantic-interposition} -g $(pkg-config --libs-only-L openssl)"
BuildPython() {
  ConfName=$1
  ExtraConfigArgs=$2
  MoreCFlags=$3
  ConfDir=build/$ConfName
  echo STARTING: BUILD OF PYTHON FOR CONFIGURATION: $ConfName
  mkdir -p $ConfDir
  pushd $ConfDir
  %global _configure $topdir/configure
  export DFLAGS=" "
%configure \
  --with-platlibdir=%{_lib} \
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
%global flags_override EXTRA_CFLAGS="$MoreCFlags" CFLAGS_NODIST="$CFLAGS_NODIST $MoreCFlags"
%if %{without bootstrap}
  %make_build %{flags_override} regen-all PYTHON_FOR_REGEN="python%{pybasever}"
%endif
  %make_build %{flags_override}
  popd
  echo FINISHED: BUILD OF PYTHON FOR CONFIGURATION: $ConfName
}
%if %{with debug_build}
BuildPython debug \
  "--without-ensurepip --with-pydebug" \
  "-O0 -Wno-cpp"
%endif
BuildPython optimized \
  "--without-ensurepip %{optimizations_flag}" \
  ""
%install
topdir=$(pwd)
%if %{with gdb_hooks}
DirHoldingGdbPy=%{_usr}/lib/debug/%{_libdir}
mkdir -p %{buildroot}$DirHoldingGdbPy
%endif
%global _pyconfig32_h pyconfig-32.h
%global _pyconfig64_h pyconfig-64.h
%global _pyconfig_h pyconfig-%{__isa_bits}.h
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
%endif
  mv %{buildroot}%{_bindir}/python${LDVersion}-{,`uname -m`-}config
  echo -e '#!/bin/sh\nexec %{_bindir}/python'${LDVersion}'-`uname -m`-config "$@"' > \
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
%endif
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
install -D -m 0644 Lib/idlelib/Icons/idle_256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/idle3.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE10}
mkdir -p %{buildroot}%{_metainfodir}
cp -a %{SOURCE11} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/idle3.appdata.xml
%endif
sed -i -e "s/'pyconfig.h'/'%{_pyconfig_h}'/" \
  %{buildroot}%{pylibdir}/distutils/sysconfig.py \
  %{buildroot}%{pylibdir}/sysconfig.py
cp -p Tools/scripts/pathfix.py %{buildroot}%{_bindir}/pathfix%{pybasever}.py
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
LD_LIBRARY_PATH="%{buildroot}%{dynload_dir}/:%{buildroot}%{_libdir}" \
%{buildroot}%{_bindir}/python%{pybasever} -s -B -m compileall \
-f %{_smp_mflags} -o 0 -o 1 -o 2 -s %{buildroot} -p / %{buildroot} --hardlink-dupes --invalidation-mode=timestamp \
-x 'bad_coding|badsyntax|site-packages|lib2to3/tests/data'
%global __brp_python_hardlink %{nil}
rm -rf %{buildroot}%{_bindir}/__pycache__
find %{buildroot} -perm 555 -exec chmod 755 {} \;
%if %{with debug_build} && %{with main_python}
ln -s \
  %{_bindir}/python%{LDVERSION_debug} \
  %{buildroot}%{_bindir}/python3-debug
%endif
mv %{buildroot}%{_bindir}/2to3-%{pybasever} %{buildroot}%{_bindir}/2to3
%if %{without main_python}
rm %{buildroot}%{_bindir}/python3
rm %{buildroot}%{_bindir}/pydoc3
rm %{buildroot}%{_bindir}/pygettext3.py
rm %{buildroot}%{_bindir}/msgfmt3.py
rm %{buildroot}%{_bindir}/idle3
rm %{buildroot}%{_bindir}/python3-*
rm %{buildroot}%{_bindir}/2to3
rm %{buildroot}%{_libdir}/libpython3.so
rm %{buildroot}%{_mandir}/man1/python3.1*
rm %{buildroot}%{_libdir}/pkgconfig/python3.pc
rm %{buildroot}%{_libdir}/pkgconfig/python3-embed.pc
%else
ln -s ./python3 %{buildroot}%{_bindir}/python
ln -s ./pydoc3 %{buildroot}%{_bindir}/pydoc
ln -s ./pygettext3.py %{buildroot}%{_bindir}/pygettext.py
ln -s ./msgfmt3.py %{buildroot}%{_bindir}/msgfmt.py
ln -s ./idle3 %{buildroot}%{_bindir}/idle
ln -s ./python3-config %{buildroot}%{_bindir}/python-config
ln -s ./python3.1 %{buildroot}%{_mandir}/man1/python.1
ln -s ./python3.pc %{buildroot}%{_libdir}/pkgconfig/python.pc
ln -s ./pathfix%{pybasever}.py %{buildroot}%{_bindir}/pathfix.py
%if %{with debug_build}
ln -s ./python3-debug %{buildroot}%{_bindir}/python-debug
%endif
%endif
for file in %{buildroot}%{pylibdir}/pydoc_data/topics.py $(grep --include='*.py' -lr %{buildroot}%{pylibdir}/encodings -e 'Python Character Mapping Codec .* from .* with gencodec.py'); do
    directory=$(dirname ${file})
    module=$(basename ${file%%.py})
    mv ${directory}/{__pycache__/${module}.cpython-%{pyshortver}.pyc,${module}.pyc}
    rm ${directory}/{__pycache__/${module}.cpython-%{pyshortver}.opt-?.pyc,${module}.py}
done
%if %{without rpmwheels}
%{?python_wheel_inject_sbom:%python_wheel_inject_sbom %{buildroot}%{pylibdir}/ensurepip/_bundled/*.whl}
%oreon_autofiles main
%endif
%check

export SETUPTOOLS_USE_DISTUTILS=stdlib
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
  echo STARTING: CHECKING OF PYTHON FOR CONFIGURATION: $ConfName
  LD_LIBRARY_PATH=$ConfDir $ConfDir/python -m test.pythoninfo
  LD_LIBRARY_PATH=$ConfDir $ConfDir/python -m test.regrtest \
    -wW --slowest -j0 --timeout=1800 \
    %if %{with bootstrap}
    -x test_distutils \
    %endif
    %ifarch %{mips64}
    -x test_ctypes \
    %endif
    %ifarch %{arm}
    %if 0%{?fedora} < 34 && 0%{?rhel} < 9 && 0%{?oreon} < 11
    -x test_gdb \
    %endif
    %endif
    %ifarch ppc64le
    -i test_sendfile_close_peer_in_the_middle_of_receiving \
    %endif
  echo FINISHED: CHECKING OF PYTHON FOR CONFIGURATION: $ConfName
}
%if %{with tests}
%if %{with debug_build}
CheckPython debug
%endif
CheckPython optimized
%endif
%if %{without flatpackage}
%if %{with main_python}
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{general_version}%{?prerel:~%{prerel}}-6
- Prepare for Oreon 11 (RP1)
%endif
%endif
