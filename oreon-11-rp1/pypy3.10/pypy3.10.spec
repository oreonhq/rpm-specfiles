%global source0_hash a7c22930b918f40870865ed8a74147f4434ef84d3d6ca2b3c1eba9355d4929c8
%global basever 7.3
%global micro 19
%global pyversion 3.10
Name:           pypy%{pyversion}
Version:        %{basever}.%{micro}%{?pre:~%{pre}}
%global version_ %{basever}.%{micro}%{?pre}
%global baserelease %{autorelease -n}
Release:        1%{?dist}
Summary:        Python 3.10 implementation with a Just-In-Time compiler
License:        MIT AND MIT-CMU AND Python-2.0.1 AND Unicode-3.0 AND BSD-3-Clause AND (Apache-2.0 OR BSD-3-Clause)
URL:            https://www.pypy.org/
ExcludeArch:    %{ix86}
%bcond rpmwheels 1
%ifarch %{ix86} x86_64 %{arm} %{power64} s390x aarch64 riscv64
%bcond jit 1
%else
%bcond jit 0
%endif
%bcond emacs 1
%bcond selftests 1
%global goal_dir pypy/goal
%bcond main_pypy3 %[0%{?fedora} && 0%{?fedora} < 42]
Source0:        https://downloads.python.org/pypy/%{name}-v%{version}-src.tar.bz2
Source2: macros.pypy3
Source3: pycparser-ply-CVE-2025-56005.patch
Patch1: 001-nevertty.patch
Patch6: 006-always-log-stdout.patch
Patch7: 007-remove-startup-message.patch
Patch9: 009-add-libxcrypt-support.patch
%bcond build_using_pypy2 1
%if %{with build_using_pypy2}
%global bootstrap_python_interp pypy2
%else
%global bootstrap_python_interp python2
%endif
%ifarch %{valgrind_arches}
%endif
%if %{with selftests}
%endif
%if %{with emacs}
%endif
%if %{with rpmwheels}
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%if %{with main_pypy3}
Provides: pypy3 = %{version}-%{release}
Provides: pypy3%{?_isa} = %{version}-%{release}
Obsoletes: pypy3 < 7.3.4-4
Conflicts: pypy3 < %{version}-%{release}
Obsoletes: pypy3.7 < 7.3.9-20
Obsoletes: pypy3.8 < 7.3.11-20
%endif
%global __requires_exclude ^/usr/bin/pypy
# oreon:deps
BuildRequires:  /usr/bin/execstack
BuildRequires:  /usr/bin/free
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/patchelf
BuildRequires:  bzip2-devel
BuildRequires:  emacs
BuildRequires:  expat-devel
BuildRequires:  gc-devel
BuildRequires:  gcc
BuildRequires:  gdbm-devel
BuildRequires:  libffi-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-interpreter
BuildRequires:  pypy2
BuildRequires:  python-pip-wheel
BuildRequires:  python-rpm-macros
BuildRequires:  python-setuptools-wheel
BuildRequires:  sqlite-devel
BuildRequires:  tcl-devel
BuildRequires:  time
BuildRequires:  tk-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
PyPy's implementation of Python %{pyversion}, featuring a Just-In-Time compiler
on some CPU architectures, and various optimized implementations
of the standard types (strings, dictionaries, etc.).

%if %{with jit}
This build of PyPy has JIT-compilation enabled.
%else
This build of PyPy has JIT-compilation disabled, as it is not supported on this
CPU architecture.
%endif

%package libs
Summary:  Run-time libraries used by PyPy implementations of Python %{pyversion}
%if %{with emacs}
Requires: emacs-filesystem%{?_emacs_version: >= %{_emacs_version}}
%endif
%if %{with main_pypy3}
Provides: pypy3-libs = %{version}-%{release}
Provides: pypy3-libs%{?_isa} = %{version}-%{release}
Obsoletes: pypy3-libs < 7.3.4-4
Obsoletes: pypy3.7-libs < 7.3.9-20
Obsoletes: pypy3.8-libs < 7.3.11-20
%endif
%if %{with rpmwheels}
Requires: python-setuptools-wheel
Requires: python-pip-wheel
%else
Provides: bundled(python3dist(pip)) = 23.0.1
Provides: bundled(python3dist(setuptools)) = 65.5.0
%endif
%{?libmpdec_version:
Provides: bundled(mpdecimal) = %{libmpdec_version}
Provides: bundled(libmpdec) = %{libmpdec_version}
}
Provides: bundled(python3dist(cffi)) = 1.18.0
Provides: bundled(python3dist(pycparser)) = 2.22
Provides: bundled(python3dist(ply)) = 3.9
Provides: bundled(python3dist(cryptography)) = 2.7
Provides: bundled(python3dist(hpy)) = 0.9.0
%description libs
Libraries required by the various PyPy implementations of Python %{pyversion}.

%package test
Summary:  Tests for PyPy%{pyversion}
Requires: pypy%{pyversion}%{?_isa} = %{version}-%{release}
Requires: pypy%{pyversion}-libs%{?_isa} = %{version}-%{release}
%if %{with main_pypy3}
Provides: pypy3-test = %{version}-%{release}
Provides: pypy3-test%{?_isa} = %{version}-%{release}
Obsoletes: pypy3.7-test < 7.3.9-20
Obsoletes: pypy3.8-test < 7.3.11-20
%endif
%description test
Various testing modules of PyPy%{pyversion}.
Useful when you want to run the test suite of PyPy%{pyversion}.

%package devel
Summary:  Development tools for working with PyPy%{pyversion}
Requires: pypy%{pyversion}%{?_isa} = %{version}-%{release}
Requires: pypy%{pyversion}-libs%{?_isa} = %{version}-%{release}
%if %{with main_pypy3}
Provides: pypy3-devel = %{version}-%{release}
Provides: pypy3-devel%{?_isa} = %{version}-%{release}
Obsoletes: pypy3-devel < 7.3.4-4
Obsoletes: pypy3.7-devel < 7.3.9-20
Obsoletes: pypy3.8-devel < 7.3.11-20
%endif
Supplements: tox
%description devel
Header files for building C extension modules against PyPy%{pyversion}.

%prep

%autosetup -n pypy%{pyversion}-v%{version_}-src -p1 -S git

%if %{with rpmwheels}
# Instead of bundled wheels, use our RPM packaged wheels from /usr/share/python-wheels
rm lib-python/3/ensurepip/_bundled/*.whl
# This append to _sysconfigdata.py is a hacked equivalent to CPython's configure --with-wheel-pkg-dir
echo "build_time_vars['WHEEL_PKG_DIR'] = '%{python_wheel_dir}'" >> lib_pypy/_sysconfigdata.py
%endif

# Patch the bundled ply for CVE-2025-56005
patch -p1 < %{SOURCE3}

# Replace /usr/local/bin/python or /usr/bin/env python shebangs with /usr/bin/python2 or pypy2:
find -name "*.py" -exec \
  sed \
    -i -r -e "s@/usr/(local/)?bin/(env )?python(2|3)?@/usr/bin/%{bootstrap_python_interp}@" \
    "{}" \
    \;

for f in rpython/translator/goal/bpnn.py ; do
   # Detect shebang lines && remove them:
   sed -e '/^#!/Q 0' -e 'Q 1' $f \
      && sed -i '1d' $f
   chmod a-x $f
done

# Replace all lib-python and lib_pypy python shebangs with pypy3 (those will be shipped with pypy3-libs)
find lib-python/3 lib_pypy -name "*.py" -exec \
  sed -r -i '1s@^#!\s*/usr/bin.*(python|pypy).*@#!/usr/bin/%{name}@' \
    "{}" \
    \;

# Not needed on Linux
rm lib-python/3/idlelib/idle.bat

%if %{without build_using_pypy2}
  # use the pycparser from PyPy even on CPython
  ln -s lib_pypy/cffi/_pycparser pycparser
%endif

%build

free
BuildPyPy() {
  ExeName=$1
  Options=$2
  echo "--------------------------------------------------------------"
  echo "--------------------------------------------------------------"
  echo "--------------------------------------------------------------"
  echo "STARTING BUILD OF: $ExeName"
  echo "--------------------------------------------------------------"
  echo "--------------------------------------------------------------"
  echo "--------------------------------------------------------------"
  pushd %{goal_dir}
  export CFLAGS=$(echo "$RPM_OPT_FLAGS")
  export CFLAGS=$(echo "$CFLAGS" -Wno-unused -fPIC)
  if test -x './pypy' ; then
    INTERP='./pypy'
  else
    INTERP='%{bootstrap_python_interp}'
  fi
  time \
    RPM_BUILD_ROOT= \
    PYPY_USESSION_DIR=$(pwd) \
    PYPY_USESSION_BASENAME=$ExeName \
    $INTERP ../../rpython/bin/rpython  \
    --gcrootfinder=shadowstack \
    $Options \
    targetpypystandalone \
%ifarch riscv64
    --withoutmod-_continuation \
%endif
    --platlibdir=%{_lib}
  echo "--------------------------------------------------------------"
  echo "--------------------------------------------------------------"
  echo "--------------------------------------------------------------"
  echo "FINISHED BUILDING: $ExeName"
  echo "--------------------------------------------------------------"
  echo "--------------------------------------------------------------"
  echo "--------------------------------------------------------------"
  popd
}
BuildPyPy \
  pypy3 \
%if %{with jit}
  "-Ojit" \
%else
  "-O2" \
%endif
  %{nil}
%if %{with emacs}
%{_emacs_bytecompile} rpython/jit/tool/pypytrace-mode.el
%endif
%install
%global pypylibdir %{_libdir}/pypy%{pyversion}
%global installation_archive_name pypy%{pyversion}-%{version_}
%global packaging_builddir builddir
%global packaged_prefix %{packaging_builddir}/%{installation_archive_name}
%global soname_version 0.1
%{bootstrap_python_interp} pypy/tool/release/package.py --archive-name '%{installation_archive_name}' --builddir '%{packaging_builddir}' --no-embedded-dependencies
rm %{packaged_prefix}/bin/python*
rm %{packaged_prefix}/bin/pypy
%{!?with_main_pypy3:rm %{packaged_prefix}/bin/pypy3}
rm %{packaged_prefix}/bin/*.debug
mv %{packaged_prefix}/bin/libpypy%{pyversion}-c.so %{packaged_prefix}/%{_lib}/libpypy%{pyversion}-c.so.%{soname_version}
ln -s libpypy%{pyversion}-c.so.%{soname_version} %{packaged_prefix}/%{_lib}/libpypy%{pyversion}-c.so
patchelf --set-soname libpypy%{pyversion}-c.so.%{soname_version} %{packaged_prefix}/%{_lib}/libpypy%{pyversion}-c.so.%{soname_version}
patchelf --replace-needed libpypy%{pyversion}-c.so libpypy%{pyversion}-c.so.%{soname_version} %{packaged_prefix}/bin/pypy%{pyversion}
rm %{packaged_prefix}/include/README
cp -a LICENSE %{packaged_prefix}/%{_lib}/pypy%{pyversion}
rm -r %{packaged_prefix}/%{_lib}/pypy%{pyversion}/_blake2/impl
rm -r %{packaged_prefix}/%{_lib}/pypy%{pyversion}/_libmpdec
rm -r %{packaged_prefix}/%{_lib}/pypy%{pyversion}/_sha3/kcp
rm    %{packaged_prefix}/%{_lib}/pypy%{pyversion}/_pypy_*.c
mkdir -p %{buildroot}%{_prefix}
mv %{packaged_prefix}/bin     %{buildroot}%{_bindir}
mv %{packaged_prefix}/include %{buildroot}%{_includedir}
mv %{packaged_prefix}/%{_lib} %{buildroot}%{_libdir}
install -d -m 0755 %{buildroot}%{pypylibdir}/site-packages/__pycache__
%if "%{_lib}" == "lib64"
install -d -m 0755 %{buildroot}%{_prefix}/lib/pypy%{pyversion}/site-packages/__pycache__
%endif
find \
  %{buildroot}                                                           \
  -name "*.py"                                                           \
    \(                                                                   \
       \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \;   \
             -print -exec sed -i '1d' {} \;                              \
          \)                                                             \
       -o                                                                \
       \(                                                                \
             -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \;         \
             -exec chmod a-x {} \;                                       \
        \)                                                               \
    \)
execstack --clear-execstack %{buildroot}%{_bindir}/pypy%{pyversion}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
(%{py_byte_compile %{buildroot}%{_bindir}/pypy%{pyversion} %{buildroot}}) || :
%{buildroot}%{_bindir}/pypy%{pyversion} -c 'import _tkinter'
%{buildroot}%{_bindir}/pypy%{pyversion} -c 'import tkinter'
%{buildroot}%{_bindir}/pypy%{pyversion} -c 'import _sqlite3'
%{buildroot}%{_bindir}/pypy%{pyversion} -c 'import _curses'
%{buildroot}%{_bindir}/pypy%{pyversion} -c 'import curses'
%{buildroot}%{_bindir}/pypy%{pyversion} -c 'import syslog'
%{buildroot}%{_bindir}/pypy%{pyversion} -c 'from _sqlite3 import *'
unset LD_LIBRARY_PATH
%global pypy_debuginfo_dir /usr/src/debug/pypy%{pyversion}-%{version_}-src
mkdir -p %{buildroot}%{pypy_debuginfo_dir}
cp -a pypy %{buildroot}%{pypy_debuginfo_dir}
find \
  %{buildroot}%{pypy_debuginfo_dir}  \
  \( -type f                         \
     -a                              \
     \! \( -name "*.py"              \
           -o                        \
           -name "Makefile"          \
           -o                        \
           -name "typeids.txt"       \
           -o                        \
           -name "dynamic-symbols-*" \
        \)                           \
  \)                                 \
  -delete
%if %{with emacs}
mkdir -p %{buildroot}/%{_emacs_sitelispdir}
cp -a rpython/jit/tool/pypytrace-mode.el %{buildroot}/%{_emacs_sitelispdir}/pypy%{pyversion}trace-mode.el
cp -a rpython/jit/tool/pypytrace-mode.elc %{buildroot}/%{_emacs_sitelispdir}/pypy%{pyversion}trace-mode.elc
%endif
%if %{with main_pypy3}
install -m0644 -p -D -t %{buildroot}/%{_rpmconfigdir}/macros.d %{SOURCE2}
%endif
%if %{without rpmwheels}
%{?python_wheel_inject_sbom:%python_wheel_inject_sbom %{buildroot}%{pypylibdir}/ensurepip/_bundled/*.whl}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%check

%{?libmpdec_version:
test "$(%{goal_dir}/pypy%{pyversion}-c -c 'import decimal; print(decimal.__libmpdec_version__.decode("ascii"))')" = \
     "%{libmpdec_version}"
}
topdir=$(pwd)
SkipTest() {
    TEST_NAME=$1
    sed -i -e"s|^$TEST_NAME$||g" testnames.txt
}
CheckPyPy() {
    ExeName=$1
    echo "--------------------------------------------------------------"
    echo "--------------------------------------------------------------"
    echo "--------------------------------------------------------------"
    echo "STARTING TEST OF: $ExeName"
    echo "--------------------------------------------------------------"
    echo "--------------------------------------------------------------"
    echo "--------------------------------------------------------------"
    pushd %{goal_dir}
    ( ./$ExeName -c \
         "from test.libregrtest.runtest import findtests; print('\n'.join(findtests()))"
    ) > testnames.txt
      SkipTest test_audioop
      SkipTest test_gdb
      SkipTest test_hotshot
      SkipTest test_strop
      SkipTest test_multiprocessing
    echo "== Test names =="
    cat testnames.txt
    echo "================="
    echo "" > failed-tests.txt
    for TestName in $(cat testnames.txt) ; do
        echo "===================" $TestName "===================="
        ( /usr/bin/time \
           perl -e 'alarm shift @ARGV; exec @ARGV' 900 \
             ./$ExeName -m test.regrtest -v $TestName ) \
        || (echo $TestName >> failed-tests.txt) \
        || true
    done
    echo "== Failed tests =="
    cat failed-tests.txt
    echo "================="
    popd
    echo "--------------------------------------------------------------"
    echo "--------------------------------------------------------------"
    echo "--------------------------------------------------------------"
    echo "FINISHED TESTING: $ExeName"
    echo "--------------------------------------------------------------"
    echo "--------------------------------------------------------------"
    echo "--------------------------------------------------------------"
}
%if %{with selftests}
CheckPyPy pypy%{pyversion}-c
%endif # with selftests
%global _docdir_fmt %{name}
%files -f %{oreon_filedir}/main.list
%files -n pypy3.10-libs -f %{oreon_filedir}/pypy3.10-libs.list
%files -n pypy3.10-test -f %{oreon_filedir}/pypy3.10-test.list
%files -n pypy3.10-devel -f %{oreon_filedir}/pypy3.10-devel.list

%changelog

%autochangelog
