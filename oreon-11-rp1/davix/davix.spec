%global source0_hash 66aa9adadee6ff2bae14caba731597ba7a7cd158763d9d80a9cfe395afc17403
%undefine __cmake_in_source_build
Name:         davix
Version:      8.9.0
Release:        1%{?dist}
Summary:        Toolkit for HTTP-based file management
License:      LGPL-2.1-or-later AND LGPL-2.0-or-later AND BSD-2-Clause AND MIT AND Apache-2.0 AND curl
URL:          https://dmc-docs.web.cern.ch/dmc-docs/davix.html
Source0:        https://github.com/cern-fts/davix/releases/download/R_0_8_10/davix-0.8.10.tar.gz
Requires:     %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gsoap-devel
BuildRequires:  gtest-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  python3
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  zlib-devel
# /oreon:deps
%description
Davix is a toolkit designed for file operations
with HTTP based protocols (WebDav, Amazon S3, ...).
Davix provides an API and a set of command line tools.

%package libs
Summary:      Runtime libraries for %{name}
%description libs
Libraries for %{name}. Davix is a toolkit designed for file operations
with HTTP based protocols (WebDav, Amazon S3, ...).

%package devel
Summary:      Development files for %{name}
Requires:     %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}. Davix is a toolkit designed for file operations
with HTTP based protocols (WebDav, Amazon S3, ...).

%package tests
Summary:      Test suite for %{name}
Requires:     %{name}-libs%{?_isa} = %{version}-%{release}
%description tests
Test suite for %{name}. Davix is a toolkit designed for file operations
with HTTP based protocols (WebDav, Amazon S3, ...).

%package doc
Summary:      Documentation for %{name}
BuildArch:    noarch
%description doc
Documentation and examples for %{name}. Davix is a toolkit designed
for file operations with HTTP based protocols (WebDav, Amazon S3, ...).

%clean
%cmake_build --target clean

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove bundled stuff
rm -rf test/pywebdav
rm -rf doc/sphinx/_themes/sphinx_rtd_theme

%build

%cmake \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DDOC_INSTALL_DIR=%{_pkgdocdir} \
  -DENABLE_THIRD_PARTY_COPY=TRUE \
  -DENABLE_HTML_DOCS=TRUE
%cmake_build
%cmake_build --target doc
( cd %{_vpath_builddir}/doc ; \
  sphinx-build -q -b html ../../doc/sphinx build/html ; \
  rm -f build/html/.buildinfo ; \
  rm -rf build/html/.doctrees )
%check

%{_vpath_builddir}/test/unit/davix-unit-tests
%install
%cmake_install
rm %{buildroot}%{_pkgdocdir}/LICENSE
%ldconfig_scriptlets libs
%oreon_autofiles davix-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles davix-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles davix-tests usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles davix-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n davix-libs -f %{oreon_filedir}/davix-libs.list
%files -n davix-devel -f %{oreon_filedir}/davix-devel.list
%files -n davix-tests -f %{oreon_filedir}/davix-tests.list
%files -n davix-doc -f %{oreon_filedir}/davix-doc.list

%changelog

%autochangelog
