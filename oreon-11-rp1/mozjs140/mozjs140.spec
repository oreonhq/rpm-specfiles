%global source0_hash 15d2d359b8571ecd0898faa6e05aa902b0de7cb34aadfc4d94adf6c8428f84df
%global major 140
%global build_with_lto    1
%global toolchain clang
%global require_tests     1
%if !%{build_with_lto}
%define _lto_cflags %{nil}
%endif
%ifarch %{ix86}
%global _lto_cflags %{nil}
%endif
%ifarch ppc ppc64 s390 s390x
%global big_endian 1
%endif
Name:           mozjs%{major}
Version:        140.16.0
Release:        3%{?dist}
Summary:        SpiderMonkey JavaScript library
License:        MPL-2.0 AND Apache-2.0 AND BSD-3-Clause AND BSD-2-Clause AND MIT AND GPL-3.0-or-later
URL:            https://spidermonkey.dev/
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
Patch15:        9aa8b4b051dd539e0fbd5e08040870b3c712a846.patch
Patch16:        D261512.1755672843.diff
Patch20:        spidermonkey_checks_disable.patch
%if "%{toolchain}" == "clang"
%endif
%if "%{toolchain}" == "gcc"
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cbindgen
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  libicu-devel
BuildRequires:  llvm
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n firefox-%{version} -p1

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

# Fixups executable permmissions
chmod -x third_party/rust/bumpalo/src/lib.rs

%build

export M4=m4
export AWK=awk
export AC_MACRODIR=./build/autoconf/
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
chmod -x %{buildroot}%{_includedir}/mozjs-%{major}/js/ProfilingCategoryList.h
chmod -x %{buildroot}%{_includedir}/mozjs-%{major}/js-config.h
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

pushd js/src/
%if 0%{?require_tests}
%{python3} tests/jstests.py -d -s -t 2400 --exclude-file=known_failures.txt --no-progress --wpt=disabled ../../js/src/dist/bin/js%{major}
%else
%{python3} tests/jstests.py -d -s -t 2400 --exclude-file=known_failures.txt --no-progress --wpt=disabled ../../js/src/dist/bin/js%{major} || :
%endif
%if 0%{?require_tests}
%ifarch s390 s390x
%{python3} jit-test/jit_test.py -s -t 2400 --no-progress -x large-arraybuffers/basic.js ../../js/src/dist/bin/js%{major} basic
%else
%{python3} jit-test/jit_test.py -s -t 2400 --no-progress ../../js/src/dist/bin/js%{major} basic
%endif
%else
%{python3} jit-test/jit_test.py -s -t 2400 --no-progress ../../js/src/dist/bin/js%{major} basic || :
%endif
%files -f %{oreon_filedir}/main.list
%files -n mozjs140-devel -f %{oreon_filedir}/mozjs140-devel.list

%changelog

%autochangelog

