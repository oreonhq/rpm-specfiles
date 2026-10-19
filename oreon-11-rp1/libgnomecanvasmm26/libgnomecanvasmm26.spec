%global source0_hash 996577f97f459a574919e15ba7fee6af8cda38a87a98289e9a4f54752d83e918
Name:           libgnomecanvasmm26
Version:        2.26.0
%global major_minor_version %(echo "%version" | sed "s|^\\([^\\.]*\\.[^\\.]*\\).*$|\\1|")
Release:        1%{?dist}
Summary:        C++ interface for Gnome libs (a GUI library for X)
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libgnomecanvasmm/2.26/libgnomecanvasmm-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtkmm24-devel
BuildRequires:  libgnomecanvas-devel
# /oreon:deps
%description
This package provides C++ wrappers for libgnomecanvas, for use with gtkmm.

%package devel
Summary:        Headers for developing programs that will use %{name}.
Requires:       %{name} = %{version}-%{release}
Requires:       gtkmm24-devel
Requires:       libgnomecanvas-devel
%description devel
This package contains the headers that programmers will need to
develop applications which will use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libgnomecanvasmm-%{version}

%build

%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf %buildroot
make DESTDIR=${RPM_BUILD_ROOT} install
find %buildroot -type f -name "*.la" -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libgnomecanvasmm26-devel -f %{oreon_filedir}/libgnomecanvasmm26-devel.list

%changelog

%autochangelog
