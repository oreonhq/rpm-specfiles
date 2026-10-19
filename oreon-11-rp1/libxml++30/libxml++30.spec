%global source0_hash 0c9b381b5a83d6b3ab4b0b865d7256dab27d575981b63be2f859edcb94da59c7
%global api_ver 3.0
Name:           libxml++30
Version:        3.2.6
Release:        1%{?dist}
Summary:        C++ wrapper for the libxml2 XML parser library
License:        LGPL-2.1-or-later
URL:            https://libxmlplusplus.github.io/libxmlplusplus/
Source0:        https://download.gnome.org/sources/libxml++/3.2/libxml++-%{version}.tar.xz
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  meson
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
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
%global oreon_srcdir libxml++-%{version}
%oreon_prep
%build

%meson -Dbuild-documentation=true
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
