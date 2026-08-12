%global source0_hash 66aa9adadee6ff2bae14caba731597ba7a7cd158763d9d80a9cfe395afc17403

%undefine __cmake_in_source_build

Name:         davix
Version:      0.8.10
Release:        7%{?dist}
Summary:      Toolkit for HTTP-based file management
License:      LGPL-2.1-or-later AND LGPL-2.0-or-later AND BSD-2-Clause AND MIT AND Apache-2.0 AND curl
URL:          https://dmc-docs.web.cern.ch/dmc-docs/davix.html
Source0:      https://github.com/cern-fts/davix/releases/download/R_0_8_10/davix-0.8.10.tar.gz

BuildRequires:      gcc-c++
BuildRequires:      python3
BuildRequires:      cmake
# main lib dependencies
%if 0%{?fedora} || 0%{?rhel} >= 9
# use bundled curl version on EPEL 8
BuildRequires:      curl-devel
%else
# build uses "git apply" to apply a patch to the bundled curl source
BuildRequires:      git-core
%endif
BuildRequires:      libxml2-devel
BuildRequires:      openssl-devel
BuildRequires:      zlib-devel
# davix-copy dependencies
BuildRequires:      gsoap-devel
BuildRequires:      libuuid-devel
# unit tests
BuildRequires:      gtest-devel
# documentation
BuildRequires:      doxygen
BuildRequires:      python3-sphinx
BuildRequires:      python3-sphinx_rtd_theme

Requires:     %{name}-libs%{?_isa} = %{version}-%{release}

%description
Davix is a toolkit designed for file operations
with HTTP based protocols (WebDav, Amazon S3, ...).
Davix provides an API and a set of command line tools.

%package libs
Summary:      Runtime libraries for %{name}
%if ! ( 0%{?fedora} || 0%{?rhel} >= 9)
Provides:     bundled(libcurl) = 7.69.0
%endif

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
%if 0%{?fedora} || 0%{?rhel} >= 9
# remove bundled curl version outside EPEL 8
rm -rf deps/curl
%endif
rm -rf test/pywebdav
rm -rf doc/sphinx/_themes/sphinx_rtd_theme

%build
%cmake \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
%if 0%{?fedora} || 0%{?rhel} >= 9
  -DEMBEDDED_LIBCURL=FALSE \
%endif
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

%files
%{_bindir}/davix-cp
%{_bindir}/davix-get
%{_bindir}/davix-http
%{_bindir}/davix-ls
%{_bindir}/davix-mkdir
%{_bindir}/davix-mv
%{_bindir}/davix-put
%{_bindir}/davix-rm
%doc %{_mandir}/man1/davix-get.1*
%doc %{_mandir}/man1/davix-http.1*
%doc %{_mandir}/man1/davix-ls.1*
%doc %{_mandir}/man1/davix-mkdir.1*
%doc %{_mandir}/man1/davix-mv.1*
%doc %{_mandir}/man1/davix-put.1*
%doc %{_mandir}/man1/davix-rm.1*

%files libs
%{_libdir}/libdavix.so.*
%{_libdir}/libdavix_copy.so.*
%doc %{_pkgdocdir}/RELEASE-NOTES.md
%license LICENSE

%files devel
%{_includedir}/davix
%{_libdir}/libdavix.so
%{_libdir}/libdavix_copy.so
%{_libdir}/pkgconfig/davix.pc
%{_libdir}/pkgconfig/davix_copy.pc
%doc %{_mandir}/man3/libdavix.3*

%files tests
%{_bindir}/davix-tester
%{_bindir}/davix-unit-tests

%files doc
%doc %{_pkgdocdir}/html
%license LICENSE

%changelog
%autochangelog
