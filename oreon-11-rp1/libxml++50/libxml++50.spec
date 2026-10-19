%global source0_hash 4996e8a73995e8a4cd656c8591dce38181146edfc30cb47c97d1db3c56990ad7
%global api_ver 5.0
Name:           libxml++50
Version:        5.6.1
Release:        1%{?dist}
Summary:        C++ wrapper for the libxml2 XML parser library
License:        LGPL-2.1-or-later
URL:            https://libxmlplusplus.github.io/libxmlplusplus/
Source0:        https://github.com/libxmlplusplus/libxmlplusplus/releases/download/%{version}/libxml++-%{version}.tar.xz
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  meson
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  python3
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
License:	MIT AND LGPL-2.1-or-later
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

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
