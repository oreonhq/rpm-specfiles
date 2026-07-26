%global source0_hash 0c9b381b5a83d6b3ab4b0b865d7256dab27d575981b63be2f859edcb94da59c7

%global api_ver 3.0

Name:           libxml++30
Version:        3.2.5
Release:        7%{?dist}
Summary:        C++ wrapper for the libxml2 XML parser library

License:        LGPL-2.1-or-later
URL:            https://libxmlplusplus.github.io/libxmlplusplus/
Source:         https://download.gnome.org/sources/libxml++/3.2/libxml++-%{version}.tar.xz

BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen, graphviz
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  /usr/bin/xsltproc

%description
libxml++ is a C++ wrapper for the libxml2 XML parser library. Its original
author is Ari Johnson and it is currently maintained by Christophe de Vienne
and Murray Cumming.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}, includes full API docs
BuildArch:      noarch
Requires:       glibmm24-doc

%description    doc
This package contains the full API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n libxml++-%{version} -p1

%build
%meson -Dbuild-documentation=true
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libxml++-%{api_ver}.so.1*

%files devel
%{_includedir}/libxml++-%{api_ver}/
%{_libdir}/libxml++-%{api_ver}.so
%{_libdir}/libxml++-%{api_ver}/
%{_libdir}/pkgconfig/libxml++-%{api_ver}.pc

%files doc
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books
%{_datadir}/devhelp/books/libxml++-%{api_ver}
%{_docdir}/libxml++-%{api_ver}

%changelog
%autochangelog
