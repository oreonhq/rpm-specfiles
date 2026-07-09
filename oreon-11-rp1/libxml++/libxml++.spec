%global source0_hash 74b95302e24dbebc56e97048e86ad0a4121fc82a43e58d381fbe1d380e8eba04
%global api_ver 2.6

Name:           libxml++
Version:        2.42.3
Release:        8%{?dist}
Summary:        C++ wrapper for the libxml2 XML parser library

License:        LGPL-2.1-or-later
URL:            https://libxmlplusplus.sourceforge.net/
Source0:        https://download.gnome.org/sources/libxml++/2.42/libxml++-%{version}.tar.xz

BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen, graphviz
BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt
BuildRequires:  meson

%description
libxml++ is a C++ wrapper for the libxml2 XML parser library. Its original
author is Ari Johnson and it is currently maintained by Christophe de Vienne
and Murray Cumming.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libxml2-devel
Requires:       glibmm24-devel

%description devel
This package contains the headers and libraries for libxml++ development.

%package        doc
Summary:        Documentation for %{name}, includes full API docs
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       glibmm24-doc

%description    doc
This package contains the full API documentation for %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
sed -i s'#\r##' examples/dom_parser/example_with_namespace.xml

%build
%meson -Dbuild-documentation=true
%meson_build

%install
%meson_install


%files
%license COPYING
%doc NEWS README.md
%{_libdir}/%{name}-%{api_ver}.so.2*


%files devel
%{_includedir}/%{name}-%{api_ver}/
%{_libdir}/%{name}-%{api_ver}/
%{_libdir}/%{name}-%{api_ver}.so
%{_libdir}/pkgconfig/%{name}-%{api_ver}.pc


%files doc
%doc %{_datadir}/devhelp/books/%{name}-%{api_ver}
%doc %{_docdir}/%{name}-%{api_ver}


%changelog
%autochangelog