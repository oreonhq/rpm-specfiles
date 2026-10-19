%global source0_hash e021c37f8818f21628a8fc40412138ea0c5e6320c93da3d3fc03d1f0dab86fdc
Summary:        Miniature XML development library
Name:         mxml
Version:      4.0.5
Release:        1%{?dist}
License:      Apache-2.0 WITH mxml-exception
URL:          https://www.msweet.org/mxml/
Source0:        https://github.com/michaelrsweet/mxml/archive/v%{version}/mxml-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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
rm %{buildroot}%{_libdir}/libmxml.a
rm %{buildroot}%{_pkgdocdir}/{LICENSE,NOTICE}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mxml-devel -f %{oreon_filedir}/mxml-devel.list

%changelog

%autochangelog
