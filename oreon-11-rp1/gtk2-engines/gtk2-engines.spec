%global source0_hash e0ed144cdd298bc69b53face0e907369fb6a51f1eb333b5d04331f12758b454c
Summary:        Theme engines for GTK+ 2.0
Name:           gtk2-engines
Version:        2.91.1
Release:        1%{?dist}
License:        LGPL-2.1-or-later
Source0:        https://download.gnome.org/sources/gtk-engines/2.91/gtk-engines-%{version}.tar.bz2
URL:            http://download.gnome.org/sources/gtk-engines
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
The gtk2-engines package contains shared objects and configuration
files that implement a number of GTK+ theme engines. Theme engines
provide different looks for GTK+, some of which resemble other
toolkits or operating systems.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
The gtk2-engines-devel package contains files needed to develop
software that uses the theme engines in the gtk2-engines package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gtk-engines-%{version}

%build

%configure --disable-static
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT%{_datadir}/themes/Redmond
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.4.0/engines/libredmond95.so
%find_lang gtk3-engines
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gtk2-engines-devel -f %{oreon_filedir}/gtk2-engines-devel.list

%changelog

%autochangelog
