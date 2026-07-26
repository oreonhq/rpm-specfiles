%global source0_hash 773a6ad8f3eed3a3859a58c9bcd808c27c20b374850c7f14644707c3340a5038

Name:           libdigidocpp

Version:        4.3.0
Release:        2%{?dist}

Summary:        Library offers creating, signing and verification of digitally signed documents
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/open-eid/libdigidocpp
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires: make
BuildRequires: cmake
BuildRequires:  gcc-c++
BuildRequires:  libtool-ltdl-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(xmlsec1-openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  minizip-ng-compat-devel

# Dynamically loaded libraries
Requires:       opensc%{?_isa}

%description
Libdigidocpp library offers creating, signing and verification of digitally
signed documents, according to XAdES and XML-DSIG standards. Documentation
http://open-eid.github.io/libdigidocpp

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    doc
The %{name}-doc package contains documentation provided by upstream.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

# it contains non UTF-8 files, but they do not worth the process of
# unpackaging and fixing the encoding
rm -rf doc/sample_files.zip

# Remove bundled minizip
rm -rf src/minizip

%build
# the dot after %%{cmake} has been removed from Fedora because of
# https://bugzilla.redhat.com/show_bug.cgi?id=2059201
# https://docs.fedoraproject.org/en-US/packaging-guidelines/CMake/
%if 0%{?el7}
%{cmake3} .\
 -DCMAKE_INSTALL_SYSCONFDIR=/etc \
 -DSWIG_EXECUTABLE=SWIG_EXECUTABLE-NOTFOUND
%else
%{cmake} \
 -DCMAKE_INSTALL_SYSCONFDIR=/etc \
 -DSWIG_EXECUTABLE=SWIG_EXECUTABLE-NOTFOUND
%endif

%if ((0%{?el} >= 9) || (0%{?fedora} >= 33))
%cmake_build
%else
%make_build
%endif

%install

%if ((0%{?el} >= 9) || (0%{?fedora} >= 33))
%cmake_install
%else
%make_install
%endif

%if 0%{?el7}
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%doc AUTHORS README.md RELEASE-NOTES.md
%license COPYING LICENSE.LGPL
%{_libdir}/*.so.*
%dir %{_sysconfdir}/digidocpp
%config(noreplace) %{_sysconfdir}/digidocpp/digidocpp.conf
%{_sysconfdir}/digidocpp/schema/
%{_bindir}/digidoc-*
%{_mandir}/man1/digidoc-tool.1.*

%files devel
%doc AUTHORS README.md RELEASE-NOTES.md
%license COPYING
%{_includedir}/digidocpp/
%{_libdir}/pkgconfig/lib*.pc
%{_libdir}/cmake/libdigidocpp/*.cmake
%{_libdir}/*.so

%files doc
%doc AUTHORS README.md RELEASE-NOTES.md doc/*
%license COPYING
%{_docdir}/libdigidocpp/*

%changelog
%autochangelog
