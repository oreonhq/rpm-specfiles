%global source0_hash 59eba16ce43765f2e2a6cf4873a58d317be801f1e929647d85da9f171e41e9ac

Summary:      Miniature XML development library
Name:         mxml
Version:      3.3.1
Release:      10%{?dist}
License:      Apache-2.0 WITH mxml-exception
URL:          https://www.msweet.org/mxml/
Source:       https://github.com/michaelrsweet/mxml/archive/v%{version}/mxml-%{version}.tar.gz
BuildRequires: make
BuildRequires: gcc

%description
Mini-XML is a small XML parsing library that you can use to read XML
and XML-like data files in your application without requiring large
non-standard libraries.

%package devel
Summary:  Libraries, includes, etc to develop mxml applications
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Libraries, include files, etc you can use to develop mxml
applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Omit the epub file.
sed -e '/^DOCFILES/ s|doc/mxml.epub||' -i Makefile.in

%build
%configure
%make_build

%install
%make_install BUILDROOT=%{buildroot}

# Configuring with --disable-static doesn't work, so let's just delete
# the .a file by hand.
rm %{buildroot}%{_libdir}/libmxml.a

# Remove files we want to ship in licensedir.
rm %{buildroot}%{_pkgdocdir}/{LICENSE,NOTICE}

%files
%license LICENSE NOTICE
%{_libdir}/libmxml.so.1{,.*}

%files devel
%{_pkgdocdir}
%{_includedir}/mxml.h
%{_libdir}/libmxml.so
%{_mandir}/man3/mxml.3*
%{_libdir}/pkgconfig/mxml.pc

%changelog
%autochangelog
