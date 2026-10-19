%global source0_hash a77026ef9d91adb2265117af46f1ceffd52c93cd79a637d239683b499607ef68
%global         soversion 1.9
Name:           sword
Epoch:          1
Version:        1.9.0
Release:        1%{?dist}
Summary:        Free Bible Software Project
License:        GPL-2.0-only AND LicenseRef-Fedora-Public-Domain AND Apache-2.0 AND LGPL-2.0-or-later AND Zlib AND LGPL-2.1-or-later AND (0BSD OR MIT-0 OR MIT)
URL:            http://www.crosswire.org/sword/
Source0:        sword-1.9.0.tar.gz
Source1:        sword_gen_free_tarball.sh
Source2:        LICENSE_README
Patch0:         cmake-perl-bindings.diff
Patch1:         migrate-to-setuptools.diff
Patch2:         wchar_t_madness.patch
# oreon:deps
BuildRequires:  clucene-core-devel
BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  curl-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  icu
BuildRequires:  libicu-devel
BuildRequires:  libidn-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  swig
BuildRequires:  zlib-devel
# /oreon:deps
%description
The SWORD Project is the CrossWire Bible Society's free Bible software
project. Its purpose is to create cross-platform open-source tools--
covered by the GNU General Public License-- that allow programmers and
Bible societies to write new Bible software more quickly and easily. We
also create Bible study software for all readers, students, scholars,
and translators of the Bible, and have a growing collection of over 200
texts in over 50 languages.

%package devel
Summary:  Development files for the sword project
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: pkgconfig
Requires: curl-devel
Requires: clucene-core-devel
Requires: libicu-devel
%description devel
This package contains the development headers and libraries for the
sword API. You need this package if you plan on compiling software
that uses the sword API, such as Gnomesword or Bibletime.

%package utils
Summary:  Utilities for the sword project
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description utils
This package contains the pre-built utilities for use with the SWORD
Project. The SWORD Project developers encourage you to use the latest
development version of the utilities rather than those released with
a packaged release as updates to the utilities do not affect the
release schedule of the library. However, these utilities were the
latest at the time of the current library release.

%package -n python3-sword
%py_provides python3-sword
Summary: Python bindings for Sword
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: python3
%description -n python3-sword
Python bindings for The SWORD Library.

%package -n perl-sword
Summary: Perl bindings for Sword
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: perl-interpreter
Requires: perl-XML-LibXML
Requires: perl-HTML-Strip
%description -n perl-sword
Perl bindings for The SWORD Library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
       -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
       -DLIB_INSTALL_DIR:PATH=%{_libdir} \
       -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
       -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
       %if "%{?_lib}" == "lib64"
         %{?_cmake_lib_suffix64} \
       %endif
       -DLIBSWORD_LIBRARY_TYPE=Shared \
       -DSWORD_PYTHON_3:BOOL=TRUE \
       -DSWORD_PERL:BOOL=TRUE \
       -DSWORD_BUILD_UTILS="Yes" \
       -DLIBSWORD_SOVERSION=%{soversion} \
       -DLIBDIR=%{_libdir} \
       -DSWORD_BUILD_TESTS=Yes \
       -DSWORD_PYTHON_INSTALL_ROOT="%{buildroot}" \
       -DSWORD_PYTHON_INSTALL_DIR="%{_prefix}"
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/sword/modules
%oreon_autofiles python3-sword usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles perl-sword usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make tests
%files -f %{oreon_filedir}/main.list
%files -n sword-devel -f %{oreon_filedir}/sword-devel.list
%files -n sword-utils -f %{oreon_filedir}/sword-utils.list
%files -n python3-sword -f %{oreon_filedir}/python3-sword.list
%files -n perl-sword -f %{oreon_filedir}/perl-sword.list

%changelog

%autochangelog
