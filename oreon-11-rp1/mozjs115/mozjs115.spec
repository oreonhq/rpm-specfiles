%global source0_hash eb4cd91deecebff92e3fb20a65b3945a2ca8611bce6537a0e289989511486522
%global major 115
%global build_with_lto    1
%ifarch ppc ppc64 s390 s390x
%global require_tests     0
%else
%global require_tests     1
%endif
%if 0%{?build_with_lto}
%else
%define _lto_cflags %{nil}
%endif
%ifarch ppc ppc64 s390 s390x
%global big_endian 1
%endif
Name:           mozjs%{major}
Version:        115.41.0
Release:        1%{?dist}
Summary:        SpiderMonkey JavaScript library
License:        MPL-2.0 AND Apache-2.0 AND BSD-3-Clause AND BSD-2-Clause AND MIT AND GPL-3.0-or-later
URL:            https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey
Source0:        https://ftp.mozilla.org/pub/firefox/releases/%{version}esr/source/firefox-%{version}esr.source.tar.xz
Source1:        known_failures.txt
Patch01:        fix-soname.patch
Patch02:        copy-headers.patch
Patch03:        tests-increase-timeout.patch
Patch09:        icu_sources_data.py-Decouple-from-Mozilla-build-system.patch
Patch10:        icu_sources_data-Write-command-output-to-our-stderr.patch
Patch12:        emitter.patch
Patch13:        tests-Use-native-TemporaryDirectory.patch
Patch14:        init_patch.patch
Patch15:        remove-sloppy-m4-detection-from-bundled-autoconf.patch
Patch16:        firefox-112.0-commasplit.patch
Patch17:        six-is-always-PY3-don-t-ask-for-it.patch
Patch20:        spidermonkey_checks_disable.patch
Patch21:        0001-Skip-failing-tests-on-ppc64-and-s390x.patch
Patch30:        tests-Replace-pipes-with-shlex-for-Python-3.13.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  clang-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libicu-devel
BuildRequires:  llvm
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3.13-devel
BuildRequires:  readline-devel
BuildRequires:  rust
BuildRequires:  rustfmt
BuildRequires:  wget
BuildRequires:  zip
# /oreon:deps
%description
SpiderMonkey is the code-name for Mozilla Firefox's C++ implementation of
JavaScript. It is intended to be embedded in other applications
that provide host environments for JavaScript.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

%autosetup -n firefox-%{version} -p1

# Purge the bundled six library incompatible with Python 3.12
rm third_party/python/six/six.py

# Link the system six library (build tooling expects that)
ln -s /usr/lib/python%{python3_version}/site-packages/six.py third_party/python/six/six.py

# Copy out the LICENSE file
cp LICENSE js/src/

# Copy out file containing known test failures with system libicu
cp %{SOURCE1} js/src/

# Remove zlib directory (to be sure using system version)
rm -rf modules/zlib

# Remove unneeded bundled stuff
rm -rf js/src/devtools/automation/variants/
rm -rf js/src/octane/
rm -rf js/src/ctypes/libffi/

# icu >= 76 link fix
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
sed -i 's/icu-i18n/icu-uc &/' js/moz.configure
%endif

%build

%if 0%{?build_with_lto}
export CARGO_PROFILE_RELEASE_LTO=true
%endif
export M4=m4
export AWK=awk
export AC_MACRODIR=./build/autoconf/
export PYTHON3="/usr/bin/python3.13"
pushd js/src/
%configure \
  --with-system-icu \
  --with-system-zlib \
  --disable-tests \
  --disable-strip \
  --with-intl-api \
  --enable-readline \
  --enable-shared-js \
  --enable-optimize \
  --disable-debug \
  --enable-pie \
  --disable-jemalloc
%make_build
%install
pushd js/src/
%make_install
chmod -x %{buildroot}%{_libdir}/pkgconfig/*.pc
case `uname -i` in
  i386 | ppc | s390 | sparc )
    wordsize="32"
    ;;
  x86_64 | ppc64 | s390x | sparc64 )
    wordsize="64"
    ;;
  *)
    wordsize=""
    ;;
esac
if test -n "$wordsize"
then
  mv %{buildroot}%{_includedir}/mozjs-%{major}/js-config.h \
     %{buildroot}%{_includedir}/mozjs-%{major}/js-config-$wordsize.h
  cat >%{buildroot}%{_includedir}/mozjs-%{major}/js-config.h <<EOF
EOF
fi
rm %{buildroot}%{_bindir}/js%{major}-config
rm %{buildroot}%{_libdir}/libjs_static.ajs
mv %{buildroot}%{_libdir}/libmozjs-%{major}.so \
   %{buildroot}%{_libdir}/libmozjs-%{major}.so.0.0.0
ln -s libmozjs-%{major}.so.0.0.0 %{buildroot}%{_libdir}/libmozjs-%{major}.so.0
ln -s libmozjs-%{major}.so.0 %{buildroot}%{_libdir}/libmozjs-%{major}.so
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export PYTHONPATH="${PYTHONPATH}:../../third_party/python/"
pushd js/src/
%if 0%{?require_tests}
/usr/bin/python3.13 tests/jstests.py -d -s -t 2400 --exclude-file=known_failures.txt --no-progress --wpt=disabled ../../js/src/dist/bin/js%{major}
%else
/usr/bin/python3.13 tests/jstests.py -d -s -t 2400 --exclude-file=known_failures.txt --no-progress --wpt=disabled ../../js/src/dist/bin/js%{major} || :
%endif
%if 0%{?require_tests}
%ifarch s390 s390x
/usr/bin/python3.13 jit-test/jit_test.py -s -t 2400 --no-progress -x large-arraybuffers/basic.js ../../js/src/dist/bin/js%{major} basic
%else
/usr/bin/python3.13 jit-test/jit_test.py -s -t 2400 --no-progress ../../js/src/dist/bin/js%{major} basic
%endif
%else
/usr/bin/python3.13 jit-test/jit_test.py -s -t 2400 --no-progress ../../js/src/dist/bin/js%{major} basic || :
%endif
%files -f %{oreon_filedir}/main.list
%files -n mozjs115-devel -f %{oreon_filedir}/mozjs115-devel.list

%changelog

%autochangelog
