%global source0_hash 0680a53b7bf90b4e4bf444d1d89e6df41c777e0bacc96e9c09fc4dd2f5fe6b72
%?mingw_package_header
Name:           mingw-gtkmm24
Version:        2.24.5
Release:        1%{?dist}
Summary:        MinGW Windows C++ interface for GTK2 (a GUI library for X)
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://gtkmm.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gtkmm/2.24/gtkmm-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-atk
BuildRequires:  mingw32-atkmm
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-cairomm
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-glibmm24
BuildRequires:  mingw32-gtk2
BuildRequires:  mingw32-pango
BuildRequires:  mingw32-pangomm
BuildRequires:  mingw64-atk
BuildRequires:  mingw64-atkmm
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-cairomm
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-glibmm24
BuildRequires:  mingw64-gtk2
BuildRequires:  mingw64-pango
BuildRequires:  mingw64-pangomm
# /oreon:deps
%description
gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm2 wraps
GTK+ 2.  Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

# Win32
%package -n mingw32-gtkmm24
Summary:        MinGW Windows C++ interface for GTK2 (a GUI library for X)
Requires:       pkgconfig
Obsoletes:      mingw32-gtkmm24-static < 2.24.2-5
%description -n mingw32-gtkmm24
gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm2 wraps
GTK+ 2.  Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

# Win64
%package -n mingw64-gtkmm24
Summary:        MinGW Windows C++ interface for GTK2 (a GUI library for X)
Requires:       pkgconfig
Obsoletes:      mingw64-gtkmm24-static < 2.24.2-5
%description -n mingw64-gtkmm24
gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm2 wraps
GTK+ 2.  Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%?mingw_debug_package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gtkmm-%{version}

%build

%mingw_configure --disable-static --enable-shared --disable-demos --disable-documentation
%mingw_make %{?_smp_mflags}
%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT/%{mingw32_datadir}/gtkmm-2.4/demo/
rm -rf $RPM_BUILD_ROOT/%{mingw64_datadir}/gtkmm-2.4/demo/
sed -i -e "s,#include <gtkmm/pagesetupunixdialog.h>,," $RPM_BUILD_ROOT/%{mingw32_includedir}/gtkmm-2.4/gtkmm.h
sed -i -e "s,#include <gtkmm/printer.h>,," $RPM_BUILD_ROOT/%{mingw32_includedir}/gtkmm-2.4/gtkmm.h
sed -i -e "s,#include <gtkmm/printjob.h>,," $RPM_BUILD_ROOT/%{mingw32_includedir}/gtkmm-2.4/gtkmm.h
sed -i -e "s,#include <gtkmm/printunixdialog.h>,," $RPM_BUILD_ROOT/%{mingw32_includedir}/gtkmm-2.4/gtkmm.h
find $RPM_BUILD_ROOT -name "*.la" -delete
%oreon_autofiles mingw32-gtkmm24 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gtkmm24 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-gtkmm24 -f %{oreon_filedir}/mingw32-gtkmm24.list
%files -n mingw64-gtkmm24 -f %{oreon_filedir}/mingw64-gtkmm24.list

%changelog

%autochangelog
