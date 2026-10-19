%global source0_hash dbb00b1c28e0407cc27d8b07a2ed0b4ea22f92e4b3e3006431cbd6726b6256b5
%global tarname gtksourceviewmm
%global api_ver 3.0
%global glibmm_version 2.46.1
%global gtkmm_version 3.18.0
%global gtksourceview_version 3.18.0
Name:           gtksourceviewmm3
Version:        3.21.3
Release:        1%{?dist}
Summary:        A C++ wrapper for gtksourceview3
License:        LGPL-2.0-or-later
URL:            http://projects.gnome.org/gtksourceviewmm/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{tarname}/3.21/%{tarname}-%{version}.tar.xz
Requires:       glibmm24%{?_isa} >= %{glibmm_version}
Requires:       gtkmm30%{?_isa} >= %{gtkmm_version}
Requires:       gtksourceview3%{?_isa} >= %{gtksourceview_version}
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel
BuildRequires:  graphviz
BuildRequires:  gtkmm30-devel
BuildRequires:  gtksourceview3-devel
BuildRequires:  make
# /oreon:deps
%description
gtksourceviewmm is a C++ wrapper for the gtksourceview widget
library. It offers all the power of gtksourceview with an interface
familiar to c++ developers, including users of the gtkmm library

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer's documentation for the gtksourceviewmm3 library
BuildArch:      noarch
BuildRequires:  doxygen graphviz
BuildRequires: make
Requires:       gtkmm30-doc
%description      doc
This package contains developer's documentation for the Gtksourceviewmm
library. Gtksourceviewmm is the C++ API for the Gtksourceview library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{tarname}-%{version}

%build

%configure --disable-static
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gtksourceviewmm3-devel -f %{oreon_filedir}/gtksourceviewmm3-devel.list
%files -n gtksourceviewmm3-doc -f %{oreon_filedir}/gtksourceviewmm3-doc.list

%changelog

%autochangelog
