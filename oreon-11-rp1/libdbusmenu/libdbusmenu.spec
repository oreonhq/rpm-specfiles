# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b9cc4a2acd74509435892823607d966d424bd9ad5d0b00938f27240a1bfa878a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global ubuntu_release 16.04

%global with_tests 0

%if 0%{?rhel} > 9
%bcond_with    gtk2
%else
%bcond_without gtk2
%endif

Name:       libdbusmenu
Version:    %{ubuntu_release}.0
Release:    1%{?dist}
Summary:    Library for passing menus over DBus

License:    (LGPL-3.0-only OR LGPL-2.1-only) AND GPL-3.0-only
URL:        https://launchpad.net/libdbusmenu
Source0:    https://launchpad.net/libdbusmenu/%{ubuntu_release}/%{version}/+download/%{name}-%{version}.tar.gz

Patch0:     00-no-werror.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: make
BuildRequires:  atk-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  glibc-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(gio-2.0) >= 2.35.4
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.24
BuildRequires:  pkgconfig(glib-2.0) >= 2.35.4
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.10
%if %{with gtk2}
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.16
%endif
BuildRequires:  pkgconfig(gtk+-3.0) >= 2.91
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.13.4
BuildRequires:  pkgconfig(x11) >= 1.3
BuildRequires:  vala

%if 0%{?with_tests}
BuildRequires:  dbus-test-runner
BuildRequires:  python2
BuildRequires:  valgrind
%endif

%description
This is a small library designed to make sharing and displaying of menu
structures over DBus simple and easy to use. It works for both QT and GTK+ and
makes building menus simple.

%package devel
Summary:    %{summary} - Development files
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with gtk2}
%package gtk2
Summary:    %{summary} - GTK+2 version
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description gtk2
Shared libraries for the %{name}-gtk2 library.
%endif

%package gtk3
Summary:    %{summary} - GTK+3 version
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description gtk3
Shared libraries for the %{name}-gtk3 library.

%if %{with gtk2}
%package gtk2-devel
Summary:    Development files for %{name}-gtk2
Requires:   %{name}-gtk2%{?_isa} = %{version}-%{release}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   gtk2-devel

%description gtk2-devel
The %{name}-gtk2-devel package contains libraries and header files for
developing applications that use %{name}-gtk2.
%endif

%package gtk3-devel
Summary:    Development files for %{name}-gtk3
Requires:   %{name}-gtk3%{?_isa} = %{version}-%{release}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   gtk3-devel

%description gtk3-devel
The %{name}-gtk3-devel package contains libraries and header files for
developing applications that use %{name}-gtk3.

%package jsonloader
Summary:    Test lib development files
Requires:   %{name}-devel%{?_isa} = %{version}-%{release}
Requires:   libdbusmenu = %{version}-%{release}

%description jsonloader
Test library for %{name}.

%package jsonloader-devel
Summary:    Test lib development files for %{name}
Requires:   %{name}-jsonloader%{?_isa} = %{version}-%{release}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description jsonloader-devel
The %{name}-jsonloader-devel package contains libraries and header files for
developing applications that use %{name}-jsonloader.

%package    doc
Summary:    Document files for %{name}
BuildArch:  noarch

%description doc
The %{name}-doc package contains documents for developing applications that
use %{name}.

%package    tools
Summary:    Development tools for the dbusmenu libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description tools
The %{name}-tools package contains helper tools for developing applications
that use %{name}.

%prep
%oreon_sha256
%setup -q -n %{name}-%{version} -c

export ACLOCAL_PATH=/usr/share/gettext/m4/
pushd %{name}-%{version}
%patch 0 -p1
autoreconf -fiv
popd

cp -a %{name}-%{version}/{README,COPYING,COPYING.2.1,COPYING-GPL3,AUTHORS,ChangeLog} .
cp -a %{name}-%{version} %{name}-gtk3-%{version}

%build
build(){
%configure --disable-static --disable-dumper --enable-introspection $*
%make_build
}

pushd %{name}-gtk3-%{version}
sed -i -e 's@^#!.*python$@#!/usr/bin/python2@' tools/dbusmenu-bench
build --with-gtk=3
popd

%if %{with gtk2}
pushd %{name}-%{version}
sed -i -e 's@^#!.*python$@#!/usr/bin/python2@' tools/dbusmenu-bench
build --with-gtk=2
popd
%endif

%install
pushd %{name}-gtk3-%{version}
%make_install
find %{buildroot} -name '*.la' -delete
popd

%if %{with gtk2}
pushd %{name}-%{version}
%make_install
find %{buildroot} -name '*.la' -delete
popd
%endif

rm -fr %{buildroot}%{_docdir}/%{name}

rm %{buildroot}/%{_libexecdir}/dbusmenu-bench

%if 0%{?with_tests}
%check
for variant in %{name}-gtk3-%{version} %{name}-%{version}; do
    pushd $variant
        make check V=1
    popd
done
%endif

%ldconfig_scriptlets
%if %{with gtk2}
%ldconfig_scriptlets gtk2
%endif
%ldconfig_scriptlets gtk3
%ldconfig_scriptlets jsonloader

%files
%license COPYING COPYING.2.1 COPYING-GPL3
%doc README AUTHORS ChangeLog
%{_libdir}/libdbusmenu-glib.so.*
%{_libdir}/girepository-1.0/Dbusmenu-0.4.typelib

%files devel
%doc %{name}-%{version}/tests/glib-server-nomenu.c
%dir %{_includedir}/libdbusmenu-glib-0.4/
%dir %{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-glib/
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-glib/*.h
%{_libdir}/libdbusmenu-glib.so
%{_libdir}/pkgconfig/dbusmenu-glib-0.4.pc
%{_datadir}/gir-1.0/Dbusmenu-0.4.gir
%{_datadir}/vala/vapi/Dbusmenu-0.4.vapi

%files jsonloader
%{_libdir}/libdbusmenu-jsonloader.so.*

%files jsonloader-devel
%dir %{_includedir}/libdbusmenu-glib-0.4/
%dir %{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-jsonloader/
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-jsonloader/*.h
%{_libdir}/libdbusmenu-jsonloader.so
%{_libdir}/pkgconfig/dbusmenu-jsonloader-0.4.pc

%files gtk3
%{_libdir}/libdbusmenu-gtk3.so.*
%{_libdir}/girepository-1.0/DbusmenuGtk3-0.4.typelib

%if %{with gtk2}
%files gtk2
%{_libdir}/libdbusmenu-gtk.so.*
%{_libdir}/girepository-1.0/DbusmenuGtk-0.4.typelib
%endif

%files gtk3-devel
%dir %{_includedir}/libdbusmenu-gtk3-0.4
%dir %{_includedir}/libdbusmenu-gtk3-0.4/libdbusmenu-gtk
%{_includedir}/libdbusmenu-gtk3-0.4/libdbusmenu-gtk/*.h
%{_libdir}/libdbusmenu-gtk3.so
%{_libdir}/pkgconfig/dbusmenu-gtk3-0.4.pc
%{_datadir}/gir-1.0/DbusmenuGtk3-0.4.gir
%{_datadir}/vala/vapi/DbusmenuGtk3-0.4.vapi

%if %{with gtk2}
%files gtk2-devel
%dir %{_includedir}/libdbusmenu-gtk-0.4
%dir %{_includedir}/libdbusmenu-gtk-0.4/libdbusmenu-gtk
%{_includedir}/libdbusmenu-gtk-0.4/libdbusmenu-gtk/*.h
%{_libdir}/libdbusmenu-gtk.so
%{_libdir}/pkgconfig/dbusmenu-gtk-0.4.pc
%{_datadir}/gir-1.0/DbusmenuGtk-0.4.gir
%{_datadir}/vala/vapi/DbusmenuGtk-0.4.vapi
%endif

%files doc
%dir %{_datadir}/gtk-doc/
%{_datadir}/gtk-doc/*

%files tools
%{_libexecdir}/dbusmenu-testapp
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/json/
%{_datadir}/%{name}/json/test-gtk-label.json

%changelog
%autochangelog
