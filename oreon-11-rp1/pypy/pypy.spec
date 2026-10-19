%global source0_hash 23537c62e875ad1a3e675c64d4435eff392ea20843e20d690fd1400b79363d64
%global basever 7.3
Name:           pypy
Version:        %{basever}.21
%global pyversion 2.7
Release:        1%{?dist}
Summary:        Python implementation with a Just-In-Time compiler
License:        MIT AND MIT-CMU AND Python-2.0.1 AND Unicode-3.0 AND BSD-3-Clause AND (Apache-2.0 OR BSD-3-Clause)
URL:            https://www.pypy.org/
ExcludeArch:    %{ix86}
%bcond rpmwheels 0
%global src_name %{ver_name}-v%{version}-src
%ifarch %{ix86} x86_64 %{arm} s390x %{power64} aarch64 riscv64
%global with_jit 1
%else
%global with_jit 0
%endif
%global with_stackless 0
%global with_emacs 1
%global verbose_logs 0
%global run_selftests 1
%global pypy_include_dir  %{pypyprefix}/include
%global pypyprefix %{_libdir}/%{name}-%{basever}
%global pylibver 2.7
%global pymajorlibver 2
%global ver_name  %{name}%{pymajorlibver}
%global goal_dir pypy/goal
%ifarch %{ix86} x86_64 %{arm}
%global _package_note_linker gold
%endif
Source0:        https://downloads.python.org/%{name}/%{ver_name}.7-v%{version}-src.tar.bz%{pymajorlibver}
Source1: macros.%{name}
Source2: macros.%{name}%{pymajorlibver}
Source3: pip-CVE-2023-5752.patch
Source4: setuptools-CVE-2024-6345.patch
Source5: setuptools-CVE-2025-47273.patch
Source6: pip-requests-CVE-2024-47081.patch
Source7: pip-urllib3-CVE-2025-50181.patch
Source8: pycparser-ply-CVE-2025-56005.patch
Patch0: 006-always-log-stdout.patch
Patch1: 007-remove-startup-message.patch
Patch2: 009-add-libxcrypt-support.patch
Patch10: 010-fix-ppc-s390x-jit-backend.patch
Source189: 189-use-rpm-wheels.patch
Patch382: 382-cve-2015-20107.patch
Patch394: 394-cve-2022-45061-cpu-denial-of-service-via-inefficient-idna-decoder.patch
Patch399: 399-cve-2023-24329.patch
%global use_self_when_building 1
%if 0%{use_self_when_building}
%global bootstrap_python_interp pypy2
%else
%global bootstrap_python_interp python2
%endif
%ifarch %{valgrind_arches}
%endif
%if %{with rpmwheels}
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: %{ver_name} = %{version}-%{release}
Provides: %{ver_name}%{_isa} = %{version}-%{release}
Provides: pypy%{pyversion} = %{version}-%{release}
Provides: pypy%{pyversion}%{_isa} = %{version}-%{release}
Provides: %{ver_name}(abi) = %{basever}
# oreon:deps
BuildRequires:  /usr/bin/git
BuildRequires:  bzip2-devel
BuildRequires:  chrpath
BuildRequires:  emacs
BuildRequires:  execstack
BuildRequires:  expat-devel
BuildRequires:  gc-devel
BuildRequires:  gcc
BuildRequires:  gdbm-devel
BuildRequires:  libffi-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-interpreter
BuildRequires:  pypy2
BuildRequires:  python-rpm-macros
BuildRequires:  sqlite-devel
BuildRequires:  tcl-devel
BuildRequires:  time
BuildRequires:  tk-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
PyPy's implementation of Python, featuring a Just-In-Time compiler on some CPU
architectures, and various optimized implementations of the standard types
(strings, dictionaries, etc)

%if 0%{with_jit}
This build of PyPy has JIT-compilation enabled.
%else
This build of PyPy has JIT-compilation disabled, as it is not supported on this
CPU architecture.
%endif

%package libs
Summary:  Run-time libraries used by PyPy implementations of Python
%if %{without rpmwheels}
License: MIT AND MIT-CMU AND Python-2.0.1 AND Unicode-3.0 AND BSD-3-Clause AND (Apache-2.0 OR BSD-3-Clause) AND (BSD-2-Clause OR Apache-2.0) AND Apache-2.0 AND ISC AND LGPL-2.0-or-later AND MPL-2.0
%endif
Requires: emacs-filesystem%{?_emacs_version: >= %{_emacs_version}}
%if %{with rpmwheels}
Requires: python-setuptools-wheel < 45
Requires: python-pip-wheel
%else
Provides: bundled(python2dist(setuptools)) = 44.0.0
Provides: bundled(python2dist(packaging)) = 16.8
Provides: bundled(python2dist(pyparsing)) = 2.2.1
Provides: bundled(python2dist(six)) = 1.10.0
Provides: bundled(python2dist(pip)) = 20.0.2
Provides: bundled(python2dist(appdirs)) = 1.4.3
Provides: bundled(python2dist(CacheControl)) = 0.12.6
Provides: bundled(python2dist(contextlib2)) = 0.6.0
Provides: bundled(python2dist(certifi)) = 2019.11.28
Provides: bundled(python2dist(chardet)) = 3.0.4
Provides: bundled(python2dist(colorama)) = 0.4.3
Provides: bundled(python2dist(distlib)) = 0.3.0
Provides: bundled(python2dist(distro)) = 1.4.0
Provides: bundled(python2dist(html5lib)) = 1.0.1
Provides: bundled(python2dist(idna)) = 2.8
Provides: bundled(python2dist(ipaddress)) = 1.0.23
Provides: bundled(python2dist(lockfile)) = 0.12.2
Provides: bundled(python2dist(msgpack)) = 0.6.2
Provides: bundled(python2dist(packaging)) = 20.1
Provides: bundled(python2dist(pep517)) = 0.7.0
Provides: bundled(python2dist(progress)) = 1.5
Provides: bundled(python2dist(pyparsing)) = 2.4.6
Provides: bundled(python2dist(pytoml)) = 0.1.21
Provides: bundled(python2dist(requests)) = 2.22.0
Provides: bundled(python2dist(retrying)) = 1.3.3
Provides: bundled(python2dist(setuptools)) = 44.0.0
Provides: bundled(python2dist(six)) = 1.14.0
Provides: bundled(python2dist(urllib3)) = 1.25.7
Provides: bundled(python2dist(webencodings)) = 0.5.1
%endif
Provides: bundled(python2dist(pycparser)) = 2.23
Provides: bundled(python2dist(ply)) = 3.9
Provides: bundled(python2dist(cryptography)) = 2.7
Provides: %{ver_name}-libs = %{version}-%{release}
Provides: %{ver_name}-libs%{_isa} = %{version}-%{release}
Provides: pypy%{pyversion}-libs = %{version}-%{release}
Provides: pypy%{pyversion}-libs%{_isa} = %{version}-%{release}
%description libs
Libraries required by the various PyPy implementations of Python.

%package devel
Summary:  Development tools for working with PyPy
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{ver_name}-devel = %{version}-%{release}
Provides: %{ver_name}-devel%{_isa} = %{version}-%{release}
Provides: pypy%{pyversion}-devel = %{version}-%{release}
Provides: pypy%{pyversion}-devel%{_isa} = %{version}-%{release}
%description devel
Header files for building C extension modules against PyPy

%if 0%{with_stackless}
%package stackless
Summary:  Stackless Python interpreter built using PyPy
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: %{ver_name}-stackless = %{version}-%{release}
Provides: %{ver_name}-stackless%{_isa} = %{version}-%{release}
Provides: pypy%{pyversion}-stackless = %{version}-%{release}
Provides: pypy%{pyversion}-stackless%{_isa} = %{version}-%{release}
%description stackless
Build of PyPy with support for micro-threads for massive concurrency
%endif

%prep

%autosetup -n pypy%{pyversion}-v%{version}-src -p1 -S git

# Temporary workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1954999
%{?!apply_patch:%define apply_patch(qp:m:) {%__apply_patch %**}}

%if %{with rpmwheels}
%apply_patch -m %(basename %{SOURCE189}) %{SOURCE189}
rm lib-python/2.7/ensurepip/_bundled/*.whl
rmdir lib-python/2.7/ensurepip/_bundled
%endif

%if %{without rpmwheels}
# Patch the bundled pip wheel for CVE-2023-5752, CVE-2024-47081, CVE-2025-50181
unzip -qq lib-python/2.7/ensurepip/_bundled/pip-20.0.2-py2.py3-none-any.whl
patch -p1 < %{SOURCE3}
patch -p1 < %{SOURCE6}
patch -p1 < %{SOURCE7}
zip -rq lib-python/2.7/ensurepip/_bundled/pip-20.0.2-py2.py3-none-any.whl pip pip-20.0.2.dist-info
rm -rf pip/ pip-20.0.2.dist-info/

# Patch the bundled setuptools wheel for CVE-2024-6345, CVE-2025-47273
unzip -qq lib-python/2.7/ensurepip/_bundled/setuptools-44.0.0-py2.py3-none-any.whl
patch -p1 < %{SOURCE4}
patch -p1 < %{SOURCE5}
zip -rq lib-python/2.7/ensurepip/_bundled/setuptools-44.0.0-py2.py3-none-any.whl easy_install.py pkg_resources setuptools setuptools-44.0.0.dist-info
rm -rf easy_install.py pkg_resources/ setuptools/ setuptools-44.0.0.dist-info/
%endif

# Patch the bundled ply for CVE-2025-56005
patch -p1 < %{SOURCE8}

# Replace /usr/local/bin/python or /usr/bin/env python shebangs with /usr/bin/python2 or pypy2:
find \( -name "*.py" -o -name "py.cleanup" \) -exec \
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

rm -rf lib-python/3

# Replace all lib-python python shebangs with pypy
find lib-python/%{pylibver} -name "*.py" -exec \
  sed -r -i '1s|^#!\s*/usr/bin.*python.*|#!/usr/bin/%{name}|' \
    "{}" \
    \;

%if ! 0%{use_self_when_building}
  # use the pycparser from PyPy even on CPython
  ln -s lib_pypy/cffi/_pycparser pycparser
%endif

# Remove windows executable binaries
rm lib-python/2.7/distutils/command/*.exe

%build

%ifarch s390x
%global optflags %(echo %{optflags} | sed 's/-march=z9-109 /-march=z10 /')
%endif
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
  %global gcrootfinder_options --gcrootfinder=shadowstack
  export CFLAGS=$(echo "$RPM_OPT_FLAGS" | sed -e 's/-g//')
  export CFLAGS=$(echo "$CFLAGS" -Wno-unused -fPIC)
  if test -x './pypy' ; then
    INTERP='./pypy'
    %ifarch %{arm}
      PYPY_GC_MAX_DELTA=200MB $INTERP --jit loop_longevity=300 ../../rpython/bin/rpython -Ojit targetpypystandalone
    %endif
  else
    INTERP='%{bootstrap_python_interp}'
  fi
  RPM_BUILD_ROOT= \
  PYPY_USESSION_DIR=$(pwd) \
  PYPY_USESSION_BASENAME=$ExeName \
  $INTERP ../../rpython/bin/rpython  \
  %{gcrootfinder_options} \
  $Options \
  targetpypystandalone \
%ifarch riscv64
  --withoutmod-_continuation \
%endif
;
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
  %{name} \
%if 0%{with_jit}
  "-Ojit" \
%else
  "-O2" \
%endif
  %{nil}
%if 0%{with_stackless}
BuildPyPy \
  %{name}-stackless \
   "--stackless"
%endif
%{_emacs_bytecompile} rpython/jit/tool/pypytrace-mode.el
%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{pypyprefix}
%{bootstrap_python_interp} pypy/tool/release/package.py --archive-name %{name}-%{basever} --builddir %{buildroot}/%{_libdir} --no-embedded-dependencies
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
execstack --clear-execstack %{buildroot}/%{pypyprefix}/bin/pypy
(%{py_byte_compile %{buildroot}%{pypyprefix}/bin/pypy %{buildroot}%{pypyprefix}}) || :
%{buildroot}%{pypyprefix}/bin/%{name} -c 'import _tkinter'
%{buildroot}%{pypyprefix}/bin/%{name} -c 'import Tkinter'
%{buildroot}%{pypyprefix}/bin/%{name} -c 'import _sqlite3'
%{buildroot}%{pypyprefix}/bin/%{name} -c 'import _curses'
%{buildroot}%{pypyprefix}/bin/%{name} -c 'import curses'
%{buildroot}%{pypyprefix}/bin/%{name} -c 'import syslog'
%{buildroot}%{pypyprefix}/bin/%{name} -c 'from _sqlite3 import *'
%global pypy_debuginfo_dir /usr/src/debug/pypy-%{version}-src
mkdir -p %{buildroot}%{pypy_debuginfo_dir}
cp -a pypy %{buildroot}%{pypy_debuginfo_dir}
mkdir -p %{buildroot}/%{_emacs_sitelispdir}
cp -a rpython/jit/tool/pypytrace-mode.el %{buildroot}/%{_emacs_sitelispdir}/%{name}trace-mode.el
cp -a rpython/jit/tool/pypytrace-mode.elc %{buildroot}/%{_emacs_sitelispdir}/%{name}trace-mode.elc
ln -sf %{pypyprefix}/bin/%{name} %{buildroot}%{_bindir}/%{name}%{pylibver}
ln -sf %{_bindir}/%{name}%{pylibver} %{buildroot}%{_bindir}/%{name}%{pymajorlibver}
ln -sf %{_bindir}/%{name}%{pymajorlibver} %{buildroot}%{_bindir}/%{name}
mv %{buildroot}/%{pypyprefix}/bin/libpypy-c.so %{buildroot}/%{_libdir}
rm -rf %{buildroot}/%{_libdir}/%{name}-%{basever}.tar.bz2
rm -rf %{buildroot}/%{pypyprefix}/README.rst
rm -rf %{buildroot}/%{pypyprefix}/README.rst
rm -rf %{buildroot}/%{pypy_include_dir}/README
chrpath --delete %{buildroot}/%{pypyprefix}/bin/%{name}
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d
install -m 644 %{SOURCE1} %{buildroot}/%{_rpmconfigdir}/macros.d
install -m 644 %{SOURCE2} %{buildroot}/%{_rpmconfigdir}/macros.d
rm -f %{buildroot}%{pypyprefix}/bin/pypy.debug
rm -f %{buildroot}%{pypyprefix}/bin/libpypy-c.so.debug
%if %{without rpmwheels}
%{?python_wheel_inject_sbom:%python_wheel_inject_sbom %{buildroot}%{pypyprefix}/lib-python/%{pylibver}/ensurepip/_bundled/*.whl}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%check

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
         "from test.regrtest import findtests; print('\n'.join(findtests()))"
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
CheckPyPy %{name}-c
%if 0%{with_stackless}
CheckPyPy %{name}-c-stackless
%endif
%global _docdir_fmt %{name}
%files -f %{oreon_filedir}/main.list
%files -n pypy-libs -f %{oreon_filedir}/pypy-libs.list
%files -n pypy-devel -f %{oreon_filedir}/pypy-devel.list

%changelog

%autochangelog
