%global source1_hash a9d7550fb8b41c54f362ee4fa5f8cd9f45d70a19a21d2e2b3c127b8edd11b8a3
%global source0_hash 39f92f366bdf3f1a02af4da75b4a5c52df6c9f7e736c7d65de13283f9f0ef416
%global source4_hash da313e9ed72260c0c0690e8c93f409dc426183dae6d7772d30cad8875b2e11b3
%global source2_key_fpr 8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D
%bcond_with docs
Name:           cmocka
Version:        2.0.2
Release:        1%{?dist}
License:        Apache-2.0
Summary:        An elegant unit testing framework for C with support for mock objects
URL:            https://cmocka.org
Source0:        https://cmocka.org/files/2.0/%{name}-%{version}.tar.xz
Source1:        https://cmocka.org/files/2.0/%{name}-%{version}.tar.xz.asc
Source2:        cmocka.keyring
Source4:        https://github.com/jothepro/doxygen-awesome-css/archive/refs/tags/v2.4.1.tar.gz#/doxygen-awesome-css-2.4.1.tar.gz
%if %{with docs}
%endif
Obsoletes:      libcmocka-static < %{version}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  gpgverify
BuildRequires:  libuv-devel
# /oreon:deps
%description
There are a variety of C unit testing frameworks available however many of them
are fairly complex and require the latest compiler technology. Some development
requires the use of old compilers which makes it difficult to use some unit
testing frameworks. In addition many unit testing frameworks assume the code
being tested is an application or module that is targeted to the same platform
that will ultimately execute the test. Because of this assumption many
frameworks require the inclusion of standard C library headers in the code
module being tested which may collide with the custom or incomplete
implementation of the C library utilized by the code under test.

Cmocka only requires a test application is linked with the standard C library
which minimizes conflicts with standard C library headers. Also, CMocka tries
to avoid the use of some of the newer features of C compilers.

This results in CMocka being a relatively small library that can be used to
test a variety of exotic code. If a developer wishes to simply test an
application with the latest compiler then other unit testing frameworks may be
preferable.

This is the successor of Google's Cmockery.

%package -n libcmocka
Summary:        Lightweight library to simplify and generalize unit tests for C
Conflicts: cmockery2
%description -n libcmocka
There are a variety of C unit testing frameworks available however many of them
are fairly complex and require the latest compiler technology. Some development
requires the use of old compilers which makes it difficult to use some unit
testing frameworks. In addition many unit testing frameworks assume the code
being tested is an application or module that is targeted to the same platform
that will ultimately execute the test. Because of this assumption many
frameworks require the inclusion of standard C library headers in the code
module being tested which may collide with the custom or incomplete
implementation of the C library utilized by the code under test.

CMocka only requires a test application is linked with the standard C library
which minimizes conflicts with standard C library headers. Also, CMocka tries
to avoid the use of some of the newer features of C compilers.

This results in CMocka being a relatively small library that can be used to
test a variety of exotic code. If a developer wishes to simply test an
application with the latest compiler then other unit testing frameworks may be
preferable.

This is the successor of Google's Cmockery.

%package -n libcmocka-devel
Summary:        Development headers for the cmocka library
Requires:       libcmocka = %{version}-%{release}
Requires:       (libcmocka-cmake-devel if cmake)
Requires:       pkgconf-pkg-config
Conflicts: cmockery2-devel
%description -n libcmocka-devel
Development headers for the cmocka unit testing library.

%package -n libcmocka-cmake-devel
Summary:        CMake support for the cmocka library
Requires:       cmake
Requires:       libcmocka-devel = %{version}
Provides:       libcmocka-devel:%{_libdir}/cmake/cmocka
%description -n libcmocka-cmake-devel
cmake support for developing with the cmocka unit testing library.

%if %{with docs}
%package -n cmocka-doc
Summary:        API documentation for the cmocka unit testing framework
BuildArch:      noarch
%description -n cmocka-doc
This package provides the API documentation for the cmocka unit testing
framework.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; }
test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" 2>/dev/null | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -a4 -p1 -n cmocka-2.0.2

%build

%define _lto_cflags %{nil}
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DWITH_STATIC_LIB=ON \
  -DUNIT_TESTING=ON \
  -DDOXYGEN_AWESOME_CSS_DIR=%{_sourcedir}/doxygen-awesome-css-2.4.1
%cmake_build
%if %{with docs}
%__cmake --build %{__cmake_builddir} --target docs
%endif
%install
%cmake_install
%ldconfig_scriptlets -n libcmocka
%oreon_autofiles libcmocka usr/*/lib*.so.*
%oreon_autofiles libcmocka-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libcmocka-cmake-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cmocka-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libcmocka -f %{oreon_filedir}/libcmocka.list
%files -n libcmocka-devel -f %{oreon_filedir}/libcmocka-devel.list
%files -n libcmocka-cmake-devel -f %{oreon_filedir}/libcmocka-cmake-devel.list
%if %{with docs}
%files -n cmocka-doc -f %{oreon_filedir}/cmocka-doc.list

%endif
%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.2-1
- Import
