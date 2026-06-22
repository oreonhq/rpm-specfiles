%global source0_hash 272179ddd9a2e41a0fc8e42e33dfbdca0b3711aa5abf372d3f2d51543d09b625

%{?mingw_package_header}

# https://src.fedoraproject.org/rpms/redhat-rpm-config/pull-request/166#comment-95032
%undefine _auto_set_build_flags

%global pkgname python3
%global py_ver 3.11
%global py_ver_nodots 311
%global mingw32_py3_libdir       %{mingw32_libdir}/python%{py_ver}
%global mingw64_py3_libdir       %{mingw64_libdir}/python%{py_ver}
%global mingw32_py3_hostlibdir   %{_prefix}/%{mingw32_target}/lib/python%{py_ver}
%global mingw64_py3_hostlibdir   %{_prefix}/%{mingw64_target}/lib/python%{py_ver}
%global mingw32_py3_incdir       %{mingw32_includedir}/python%{py_ver}
%global mingw64_py3_incdir       %{mingw64_includedir}/python%{py_ver}
%global mingw32_python3_sitearch %{mingw32_libdir}/python%{py_ver}/site-packages
%global mingw64_python3_sitearch %{mingw64_libdir}/python%{py_ver}/site-packages

# Some of the files below /usr/lib/pythonMAJOR.MINOR/test  (e.g. bad_coding.py)
# are deliberately invalid, leading to SyntaxError exceptions if they get
# byte-compiled.
%global _python_bytecompile_errors_terminate_build 0

#global pre rc2

Name:          mingw-%{pkgname}
Version:       3.11.15
Release:       4%{?dist}
Summary:       MinGW Windows %{pkgname}

BuildArch:     noarch
License:       Python-2.0.1
URL:           https://www.python.org/
Source0:       https://www.python.org/ftp/python/%{version}/Python-%{version}%{?pre}.tar.xz

Source1:       macros.mingw32-python3
Source2:       macros.mingw64-python3
Source3:       mingw32_python3.attr
Source4:       mingw64_python3.attr


# Add support for building with mingw
Patch1:        mingw-python3_platform-mingw.patch
# Implement setenv for mingw
Patch2:        mingw-python3_setenv.patch
# Ignore main program for frozen scripts
Patch3:        mingw-python3_frozenmain.patch
# Link resource files and build pythonw.exe
Patch4:        mingw-python3_pythonw.patch
# Implement PyThread_get_thread_native_id for mingw-win-pthread
Patch5:        mingw-python3_pthread_threadid.patch
# Output list of failed modules to mods_failed.txt so that we can abort the build
Patch6:        mingw-python3_mods-failed.patch
# Adapt distutils for cross-compiling
Patch7:        mingw-python3_distutils.patch
# Make sysconfigdata.py relocatable
Patch8:        mingw-python3_make-sysconfigdata.py-relocatable.patch
# Fix module builds: select, ssl, multiprocessing
# Disable modules which do not build
# Fix broken parallel make
Patch9:        mingw-python3_modules.patch
# Use POSIX layout
Patch10:       mingw-python3_posix-layout.patch
# Enable some modules needed on Windows
Patch11:       mingw-python3_win-modules.patch
# Enable the socket module
Patch12:       mingw-python3_module-socket.patch
# MinGW fix for select module
Patch13:       mingw-python3_module-select.patch
# Add -lpython<VER> to Libs: in pkgconfig (windows extensions need to be linked against libpython)
Patch14:       mingw-python3_pkgconfig.patch
# Backport: Fix build with tcl9
Patch15:       https://github.com/python/cpython/commit/e0799352823289fafb8131341abd751923ee9c08.patch
# Backport proposed fix for CVE-2026-2297
# https://github.com/python/cpython/pull/145515
Patch16:       CVE-2026-2297.patch
# Backport fix for CVE-2026-4519
Patch20:       https://github.com/python/cpython/commit/ceac1efc66516ac387eef2c9a0ce671895b44f03.patch
# Backport fix for CVE-2026-3644
Patch21:       https://github.com/python/cpython/pull/146026.patch
# Backport fix for CVE-2026-4224
Patch22:       https://github.com/python/cpython/pull/146000.patch
# Backport fix for CVE-2026-6100
Patch23:       https://github.com/python/cpython/commit/e20c6c9667c99ecaab96e1a2b3767082841ffc8b.patch
# Backport fix for CVE-2026-3479
Patch24:       https://github.com/python/cpython/pull/146136.patch
# Backport fix for CVE-2026-1502
Patch25:       https://github.com/python/cpython/pull/148351.patch
# Backport fix for CVE-2026-4786
Patch26:       https://github.com/python/cpython/pull/148520.patch


BuildRequires: make
BuildRequires: automake autoconf libtool
BuildRequires: autoconf-archive
BuildRequires: python%{py_ver}-devel

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc
# Needed for correct value of CXX in _sysconfigdata.py
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-bzip2
BuildRequires: mingw32-dlfcn
BuildRequires: mingw32-expat
BuildRequires: mingw32-libffi
BuildRequires: mingw32-openssl
BuildRequires: mingw32-sqlite
BuildRequires: mingw32-tcl
BuildRequires: mingw32-tk

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc
# Needed for correct value of CXX in _sysconfigdata.py
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-bzip2
BuildRequires: mingw64-dlfcn
BuildRequires: mingw64-expat
BuildRequires: mingw64-libffi
BuildRequires: mingw64-openssl
BuildRequires: mingw64-sqlite
BuildRequires: mingw64-tcl
BuildRequires: mingw64-tk


%description
MinGW Windows %{pkgname}


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname}
Requires:      python%{py_ver}
Requires:      python%{py_ver}-devel
Requires:      python-rpm-macros
Requires:      python3-rpm-generators
Requires:      mingw32-dlfcn
Provides:      mingw32(python(abi)) = %{py_ver}

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname}.


%package -n mingw32-%{pkgname}-test
Summary:       MinGW Windows %{pkgname} - native testsuite
Requires:      mingw32-python3

%description -n mingw32-%{pkgname}-test
MinGW Windows %{pkgname} - native testsuite.


%package -n mingw32-%{pkgname}-tkinter
Summary:       MinGW Windows %{pkgname} - GUI toolkit
Requires:      mingw32-python3

%description -n mingw32-%{pkgname}-tkinter
MinGW Windows %{pkgname} - GUI toolkit.


%package -n mingw32-%{pkgname}-idle
Summary:       MinGW Windows %{pkgname} - development environment
Requires:      mingw32-python3

%description -n mingw32-%{pkgname}-idle
MinGW Windows %{pkgname} - development environment.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname}
Requires:      python%{py_ver}
Requires:      python%{py_ver}-devel
Requires:      python-rpm-macros
Requires:      python3-rpm-generators
Requires:      mingw64-dlfcn
Provides:      mingw64(python(abi)) = %{py_ver}

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname}.


%package -n mingw64-%{pkgname}-test
Summary:       MinGW Windows %{pkgname} - native testsuite
Requires:      mingw64-python3

%description -n mingw64-%{pkgname}-test
MinGW Windows %{pkgname} - native testsuite.


%package -n mingw64-%{pkgname}-tkinter
Summary:       MinGW Windows %{pkgname} - GUI toolkit
Requires:      mingw64-python3

%description -n mingw64-%{pkgname}-tkinter
MinGW Windows %{pkgname} - GUI toolkit.


%package -n mingw64-%{pkgname}-idle
Summary:       MinGW Windows %{pkgname} - development environment
Requires:      mingw64-python3

%description -n mingw64-%{pkgname}-idle
MinGW Windows %{pkgname} - development environment.


%{?mingw_debug_package}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Python-%{version}%{?pre}
autoreconf -vfi

# Ensure that we are using the system copy of various libraries rather than copies shipped in the tarball
rm -r Modules/expat
rm -r Modules/_ctypes/{darwin,libffi}*

# Just to be sure that we are using the wanted thread model
rm -f Python/thread_nt.h


%build
# FIXME: avoid incompatible-pointer-types errors
export MINGW32_CFLAGS="%{mingw32_cflags} -fpermissive"
export MINGW64_CFLAGS="%{mingw64_cflags} -fpermissive"
export MINGW32_MAKE_ARGS="WINDRES=%{mingw32_target}-windres LD=%{mingw32_target}-ld DLLWRAP=%{mingw32_target}-dllwrap"
export MINGW64_MAKE_ARGS="WINDRES=%{mingw64_target}-windres LD=%{mingw64_target}-ld DLLWRAP=%{mingw64_target}-dllwrap"

CONFIG_SITE=$PWD/config.site-mingw \
%mingw_configure \
--enable-shared \
--with-build-python=%{_bindir}/python3.11 \
--with-system-expat \
--with-suffix=.exe \
--enable-loadable-sqlite-extensions \
--with-ensurepip=no

# Create directories needed by build
mkdir -p build_win32/PC/icons build_win64/PC/icons

%mingw_make_build

# Abort build if not explicitly disabled modules failed to build
if [ -e build_win32/mods_failed.txt ]; then
    echo "The following modules failed to build for win32"
    cat build_win32/mods_failed.txt
fi
if [ -e build_win64/mods_failed.txt ]; then
    echo "The following modules failed to build for win64"
    cat build_win64/mods_failed.txt
fi
if [ -e build_win32/mods_failed.txt ] || [ -e build_win64/mods_failed.txt ]; then
    exit 1;
fi


%install
%mingw_make_install

# Link import library to libdir
ln -s %{mingw32_py3_libdir}/config-%{py_ver}/libpython%{py_ver}.dll.a %{buildroot}%{mingw32_libdir}/libpython%{py_ver}.dll.a
ln -s %{mingw64_py3_libdir}/config-%{py_ver}/libpython%{py_ver}.dll.a %{buildroot}%{mingw64_libdir}/libpython%{py_ver}.dll.a

# Copy some useful "stuff"
install -dm755 %{buildroot}%{mingw32_py3_libdir}/Tools/{i18n,scripts}
install -dm755 %{buildroot}%{mingw64_py3_libdir}/Tools/{i18n,scripts}
install -pm755 Tools/i18n/{msgfmt,pygettext}.py %{buildroot}%{mingw32_py3_libdir}/Tools/i18n/
install -pm755 Tools/i18n/{msgfmt,pygettext}.py %{buildroot}%{mingw64_py3_libdir}/Tools/i18n/
install -pm755 Tools/scripts/{README,*py} %{buildroot}%{mingw32_py3_libdir}/Tools/scripts/
install -pm755 Tools/scripts/{README,*py} %{buildroot}%{mingw64_py3_libdir}/Tools/scripts/

# Cleanup shebangs
find %{buildroot}%{mingw32_py3_libdir}/ -name '*.py' | xargs sed -i "s|#[ ]*![ ]*/usr/bin/env python$|#!/usr/bin/python3|"
find %{buildroot}%{mingw64_py3_libdir}/ -name '*.py' | xargs sed -i "s|#[ ]*![ ]*/usr/bin/env python$|#!/usr/bin/python3|"

# Remove references to build directory
for file in config-%{py_ver}/Makefile _sysconfigdata__win32_.py; do
    sed -i "s|%{_builddir}|/build|g" %{buildroot}%{mingw32_py3_libdir}/$file
    sed -i "s|%{_builddir}|/build|g" %{buildroot}%{mingw64_py3_libdir}/$file
done

# Fix permissons
find %{buildroot} -type f | xargs chmod 0644
find %{buildroot} -type f \( -name "*.dll" -o -name "*.exe" \) | xargs chmod 0755

# Don't ship manpages
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

# Host site-packages skeleton
mkdir -p %{buildroot}%{mingw32_py3_hostlibdir}/site-packages
mkdir -p %{buildroot}%{mingw64_py3_hostlibdir}/site-packages

# Hackishly faked distutils/sysconfig.py
mkdir -p %{buildroot}%{mingw32_py3_hostlibdir}/distutils
mkdir -p %{buildroot}%{mingw64_py3_hostlibdir}/distutils
pushd %{buildroot}%{mingw32_libdir}/python%{py_ver}/distutils/
for file in *.py; do
    ln -s %{mingw32_libdir}/python%{py_ver}/distutils/$file %{buildroot}%{mingw32_py3_hostlibdir}/distutils/$file
done
popd
pushd %{buildroot}%{mingw64_libdir}/python%{py_ver}/distutils/
for file in *.py; do
    ln -s %{mingw64_libdir}/python%{py_ver}/distutils/$file %{buildroot}%{mingw64_py3_hostlibdir}/distutils/$file
done
popd
ln -s %{mingw32_py3_libdir}/distutils/command %{buildroot}%{mingw32_py3_hostlibdir}/distutils/command
ln -s %{mingw64_py3_libdir}/distutils/command %{buildroot}%{mingw64_py3_hostlibdir}/distutils/command
rm %{buildroot}%{mingw32_py3_hostlibdir}/distutils/sysconfig.py
rm %{buildroot}%{mingw64_py3_hostlibdir}/distutils/sysconfig.py

cat > %{buildroot}%{mingw32_py3_hostlibdir}/distutils/sysconfig.py <<EOF
import imp
import os
_sysconfig = imp.load_source('distutils.sysconfig', '%{mingw32_py3_libdir}/distutils/sysconfig.py')
from distutils.sysconfig import *
# Overwrite methods from sysconfig
if "mingw32" in os.getenv("CC"):
    get_python_inc = lambda plat_specific=0, prefix=None: "%{mingw32_py3_incdir}"
    get_python_lib = lambda plat_specific=0, standard_lib=0, prefix=None: "%{mingw32_python3_sitearch}"
else:
    get_python_inc = lambda plat_specific=0, prefix=None: "%{_includedir}/python%{py_ver}"
    get_python_lib = lambda plat_specific=0, standard_lib=0, prefix=None: "%{_libdir}/python%{py_ver}/site-packages"
EOF

cat > %{buildroot}%{mingw64_py3_hostlibdir}/distutils/sysconfig.py <<EOF
import imp
import os
_sysconfig = imp.load_source('distutils.sysconfig', '%{mingw64_py3_libdir}/distutils/sysconfig.py')
from distutils.sysconfig import *
# Overwrite methods from sysconfig
if "mingw32" in os.getenv("CC"):
    get_python_inc = lambda plat_specific=0, prefix=None: "%{mingw64_py3_incdir}"
    get_python_lib = lambda plat_specific=0, standard_lib=0, prefix=None: "%{mingw64_python3_sitearch}"
else:
    get_python_inc = lambda plat_specific=0, prefix=None: "%{_includedir}/python%{py_ver}"
    get_python_lib = lambda plat_specific=0, standard_lib=0, prefix=None: "%{_libdir}/python%{py_ver}/site-packages"
EOF

# Install macros
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/macros.d/macros.mingw32-python3
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/macros.d/macros.mingw64-python3
sed -i 's|@PY_VER@|%{py_ver}|g; s|@PY_VER_NODOTS@|%{py_ver_nodots}|g' \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.mingw32-python3 \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.mingw64-python3

# Install dependency generators
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/fileattrs/mingw32_python3.attr
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_rpmconfigdir}/fileattrs/mingw64_python3.attr

# Wrappers
mkdir -p %{buildroot}%{_bindir}
ln -s %{_libexecdir}/mingw-scripts %{buildroot}%{_bindir}/mingw32-python3
ln -s %{_libexecdir}/mingw-scripts %{buildroot}%{_bindir}/mingw64-python3

mkdir -p %{buildroot}%{_prefix}/%{mingw32_target}/bin
cat > %{buildroot}%{_prefix}/%{mingw32_target}/bin/python3 <<EOF
#!/bin/sh
%{_bindir}/mingw32-python3 "\$@"
EOF
chmod +x %{buildroot}%{_prefix}/%{mingw32_target}/bin/python3

mkdir -p %{buildroot}%{_prefix}/%{mingw64_target}/bin
cat > %{buildroot}%{_prefix}/%{mingw64_target}/bin/python3 <<EOF
#!/bin/sh
%{_bindir}/mingw64-python3 "\$@"
EOF
chmod +x %{buildroot}%{_prefix}/%{mingw64_target}/bin/python3

# TODO: These cause unsatisfyable requires on msvcr71.dll
rm -f %{buildroot}%{mingw32_py3_libdir}/distutils/command/wininst-7.1.exe
rm -f %{buildroot}%{mingw64_py3_libdir}/distutils/command/wininst-7.1.exe

# Drop unversioned 2to3
rm %{buildroot}%{mingw32_bindir}/2to3
rm %{buildroot}%{mingw64_bindir}/2to3

# Drop pip stuff installed to native dirs
rm -f %{buildroot}%{_bindir}/pip*
rm -rf %{buildroot}%{_prefix}/lib/python%{py_ver}/site-packages/pip*

# Ensure config scripts are executable
chmod +x %{buildroot}%{mingw32_bindir}/python3-config
chmod +x %{buildroot}%{mingw64_bindir}/python3-config


%files -n mingw32-%{pkgname}
%license LICENSE
%{_bindir}/mingw32-python3
%{_rpmconfigdir}/macros.d/macros.mingw32-python3
%{_rpmconfigdir}/fileattrs/mingw32_python3.attr
%{_prefix}/%{mingw32_target}/bin/python3
%{mingw32_py3_hostlibdir}/
%{mingw32_bindir}/2to3-%{py_ver}
%{mingw32_bindir}/idle3*
%{mingw32_bindir}/pydoc3*
%{mingw32_bindir}/python3.exe
%{mingw32_bindir}/python3-config
%{mingw32_bindir}/python%{py_ver}.exe
%{mingw32_bindir}/python%{py_ver}-config
%{mingw32_bindir}/python3w.exe
%{mingw32_bindir}/libpython%{py_ver}.dll
%{mingw32_py3_incdir}/
%{mingw32_libdir}/libpython%{py_ver}.dll.a
%{mingw32_py3_libdir}/
%{mingw32_libdir}/pkgconfig/*.pc
# Part of mingw32-python3-tkinter
%exclude %{mingw32_py3_libdir}/tkinter/
%exclude %{mingw32_py3_libdir}/lib-dynload/_tkinter.cpython-%{py_ver_nodots}.dll
%exclude %{mingw32_py3_libdir}/turtle.py
%exclude %{mingw32_py3_libdir}/__pycache__/turtle*
%exclude %{mingw32_py3_libdir}/turtledemo
# Part of mingw32-python3-idle
%exclude %{mingw32_bindir}/idle3
%exclude %{mingw32_bindir}/idle%{py_ver}
%exclude %{mingw32_py3_libdir}/idlelib/
# Part of mingw32-python3-test
%exclude %{mingw32_py3_libdir}/ctypes/test/
%exclude %{mingw32_py3_libdir}/distutils/tests/
%exclude %{mingw32_py3_libdir}/lib2to3/tests/
%exclude %{mingw32_py3_libdir}/test/
%exclude %{mingw32_py3_libdir}/tkinter/test/
%exclude %{mingw32_py3_libdir}/unittest/test/
%exclude %{mingw32_py3_libdir}/lib-dynload/_ctypes_test.cpython-%{py_ver_nodots}.dll
%exclude %{mingw32_py3_libdir}/lib-dynload/_testbuffer.cpython-%{py_ver_nodots}.dll
%exclude %{mingw32_py3_libdir}/lib-dynload/_testcapi.cpython-%{py_ver_nodots}.dll
%exclude %{mingw32_py3_libdir}/lib-dynload/_testimportmultiple.cpython-%{py_ver_nodots}.dll
%exclude %{mingw32_py3_libdir}/lib-dynload/_testinternalcapi.cpython-%{py_ver_nodots}.dll
%exclude %{mingw32_py3_libdir}/lib-dynload/_testmultiphase.cpython-%{py_ver_nodots}.dll
%exclude %{mingw32_py3_libdir}/lib-dynload/_xxtestfuzz.cpython-%{py_ver_nodots}.dll

%files -n mingw32-%{pkgname}-test
%{mingw32_py3_libdir}/ctypes/test/
%{mingw32_py3_libdir}/distutils/tests/
%{mingw32_py3_libdir}/lib2to3/tests/
%{mingw32_py3_libdir}/test/
%{mingw32_py3_libdir}/tkinter/test/
%{mingw32_py3_libdir}/unittest/test/
%{mingw32_py3_libdir}/lib-dynload/_ctypes_test.cpython-%{py_ver_nodots}.dll
%{mingw32_py3_libdir}/lib-dynload/_testbuffer.cpython-%{py_ver_nodots}.dll
%{mingw32_py3_libdir}/lib-dynload/_testcapi.cpython-%{py_ver_nodots}.dll
%{mingw32_py3_libdir}/lib-dynload/_testimportmultiple.cpython-%{py_ver_nodots}.dll
%{mingw32_py3_libdir}/lib-dynload/_testinternalcapi.cpython-%{py_ver_nodots}.dll
%{mingw32_py3_libdir}/lib-dynload/_testmultiphase.cpython-%{py_ver_nodots}.dll
%{mingw32_py3_libdir}/lib-dynload/_xxtestfuzz.cpython-%{py_ver_nodots}.dll

%files -n mingw32-%{pkgname}-tkinter
%{mingw32_py3_libdir}/tkinter/
%exclude %{mingw32_py3_libdir}/tkinter/test/
%{mingw32_py3_libdir}/lib-dynload/_tkinter.cpython-%{py_ver_nodots}.dll
%{mingw32_py3_libdir}/turtle.py
%{mingw32_py3_libdir}/__pycache__/turtle*
%{mingw32_py3_libdir}/turtledemo

%files -n mingw32-%{pkgname}-idle
%{mingw32_bindir}/idle3
%{mingw32_bindir}/idle%{py_ver}
%{mingw32_py3_libdir}/idlelib/

%files -n mingw64-%{pkgname}
%license LICENSE
%{_bindir}/mingw64-python3
%{_rpmconfigdir}/macros.d/macros.mingw64-python3
%{_rpmconfigdir}/fileattrs/mingw64_python3.attr
%{_prefix}/%{mingw64_target}/bin/python3
%{mingw64_py3_hostlibdir}/
%{mingw64_bindir}/2to3-%{py_ver}
%{mingw64_bindir}/idle3*
%{mingw64_bindir}/pydoc3*
%{mingw64_bindir}/python3.exe
%{mingw64_bindir}/python3-config
%{mingw64_bindir}/python%{py_ver}.exe
%{mingw64_bindir}/python%{py_ver}-config
%{mingw64_bindir}/python3w.exe
%{mingw64_bindir}/libpython%{py_ver}.dll
%{mingw64_py3_incdir}/
%{mingw64_libdir}/libpython%{py_ver}.dll.a
%{mingw64_py3_libdir}/
%{mingw64_libdir}/pkgconfig/*.pc
# Part of mingw64-python3-tkinter
%exclude %{mingw64_py3_libdir}/tkinter/
%exclude %{mingw64_py3_libdir}/lib-dynload/_tkinter.cpython-%{py_ver_nodots}.dll
%exclude %{mingw64_py3_libdir}/turtle.py
%exclude %{mingw64_py3_libdir}/__pycache__/turtle*
%exclude %{mingw64_py3_libdir}/turtledemo
# Part of mingw64-python3-idle
%exclude %{mingw64_bindir}/idle3
%exclude %{mingw64_bindir}/idle%{py_ver}
%exclude %{mingw64_py3_libdir}/idlelib/
# Part of mingw64-python3-test
%exclude %{mingw64_py3_libdir}/ctypes/test/
%exclude %{mingw64_py3_libdir}/distutils/tests/
%exclude %{mingw64_py3_libdir}/lib2to3/tests/
%exclude %{mingw64_py3_libdir}/test/
%exclude %{mingw64_py3_libdir}/tkinter/test/
%exclude %{mingw64_py3_libdir}/unittest/test/
%exclude %{mingw64_py3_libdir}/lib-dynload/_ctypes_test.cpython-%{py_ver_nodots}.dll
%exclude %{mingw64_py3_libdir}/lib-dynload/_testbuffer.cpython-%{py_ver_nodots}.dll
%exclude %{mingw64_py3_libdir}/lib-dynload/_testcapi.cpython-%{py_ver_nodots}.dll
%exclude %{mingw64_py3_libdir}/lib-dynload/_testimportmultiple.cpython-%{py_ver_nodots}.dll
%exclude %{mingw64_py3_libdir}/lib-dynload/_testinternalcapi.cpython-%{py_ver_nodots}.dll
%exclude %{mingw64_py3_libdir}/lib-dynload/_testmultiphase.cpython-%{py_ver_nodots}.dll
%exclude %{mingw64_py3_libdir}/lib-dynload/_xxtestfuzz.cpython-%{py_ver_nodots}.dll

%files -n mingw64-%{pkgname}-test
%{mingw64_py3_libdir}/ctypes/test/
%{mingw64_py3_libdir}/distutils/tests/
%{mingw64_py3_libdir}/lib2to3/tests/
%{mingw64_py3_libdir}/test/
%{mingw64_py3_libdir}/tkinter/test/
%{mingw64_py3_libdir}/unittest/test/
%{mingw64_py3_libdir}/lib-dynload/_ctypes_test.cpython-%{py_ver_nodots}.dll
%{mingw64_py3_libdir}/lib-dynload/_testbuffer.cpython-%{py_ver_nodots}.dll
%{mingw64_py3_libdir}/lib-dynload/_testcapi.cpython-%{py_ver_nodots}.dll
%{mingw64_py3_libdir}/lib-dynload/_testimportmultiple.cpython-%{py_ver_nodots}.dll
%{mingw64_py3_libdir}/lib-dynload/_testinternalcapi.cpython-%{py_ver_nodots}.dll
%{mingw64_py3_libdir}/lib-dynload/_testmultiphase.cpython-%{py_ver_nodots}.dll
%{mingw64_py3_libdir}/lib-dynload/_xxtestfuzz.cpython-%{py_ver_nodots}.dll

%files -n mingw64-%{pkgname}-tkinter
%{mingw64_py3_libdir}/tkinter/
%exclude %{mingw64_py3_libdir}/tkinter/test/
%{mingw64_py3_libdir}/lib-dynload/_tkinter.cpython-%{py_ver_nodots}.dll
%{mingw64_py3_libdir}/turtle.py
%{mingw64_py3_libdir}/__pycache__/turtle*
%{mingw64_py3_libdir}/turtledemo

%files -n mingw64-%{pkgname}-idle
%{mingw64_bindir}/idle3
%{mingw64_bindir}/idle%{py_ver}
%{mingw64_py3_libdir}/idlelib/

%changelog
%autochangelog
