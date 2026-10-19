%global source0_hash fa462f1834bae569c5944c34608872f9447e5a2889ba2aa4d5ff9f2d6ff8a395
%global major_minor_version %(echo %{version} | cut -d "." -f 1-2)
Name:           at-spi2-core
Version:        2.62.0.1
Release:        1%{?dist}
Summary:        Protocol definitions and daemon for D-Bus at-spi
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/%{name}/
Source0:        https://download.gnome.org/sources/%{name}/%{major_minor_version}/%{name}-%{version}.tar.xz
Source1:        xwayland-session-scriptlet
Requires:       dbus
Requires:       /usr/bin/xprop
# oreon:deps
BuildRequires:  /usr/bin/sphinx-build
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libei-1.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  python3-devel
# /oreon:deps
%description
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This version of at-spi is a major break from previous versions.
It has been completely rewritten to use D-Bus rather than
ORBIT / CORBA for its transport protocol.

%package devel
Summary: Development files and headers for at-spi2-core
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The at-spi2-core-devel package includes the header files and
API documentation for libatspi.

%package -n atk
Summary: Interfaces for accessibility support
Requires: at-spi2-core%{?_isa} = %{version}-%{release}
%description -n atk
The ATK library provides a set of interfaces for adding accessibility
support to applications and graphical user interface toolkits. By
supporting the ATK interfaces, an application or toolkit can be used
with tools such as screen readers, magnifiers, and alternative input
devices.

%package -n atk-devel
Summary: Development files for the ATK accessibility toolkit
Requires: atk%{?_isa} = %{version}-%{release}
%description -n atk-devel
This package includes libraries, header files, and developer documentation
needed for development of applications or toolkits which use ATK.

%package -n at-spi2-atk
Summary: A GTK+ module that bridges ATK to D-Bus at-spi
Requires: atk%{?_isa} = %{version}-%{release}
Requires: at-spi2-core%{?_isa} = %{version}-%{release}
%description -n at-spi2-atk
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This version of at-spi is a major break from previous versions.
It has been completely rewritten to use D-Bus rather than
ORBIT / CORBA for its transport protocol.

This package includes a gtk-module that bridges ATK to the new
D-Bus based at-spi.

%package -n at-spi2-atk-devel
Summary: A GTK+ module that bridges ATK to D-Bus at-spi
Requires: at-spi2-atk%{?_isa} = %{version}-%{release}
%description -n at-spi2-atk-devel
The at-spi2-atk-devel package includes the header files for the at-spi2-atk
library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Ddocs=true -Ddefault_bus=dbus-broker -Ddbus_daemon=/usr/bin/dbus-daemon -Ddbus_broker=/usr/bin/dbus-broker-launch
%meson_build
%install
%meson_install
install -Dpm 0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/Xwayland-session.d/00-at-spi
%{find_lang} %{name}
%oreon_autofiles at-spi2-core-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles atk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles atk-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles at-spi2-atk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles at-spi2-atk-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n at-spi2-core-devel -f %{oreon_filedir}/at-spi2-core-devel.list
%files -n atk -f %{oreon_filedir}/atk.list
%files -n atk-devel -f %{oreon_filedir}/atk-devel.list
%files -n at-spi2-atk -f %{oreon_filedir}/at-spi2-atk.list
%files -n at-spi2-atk-devel -f %{oreon_filedir}/at-spi2-atk-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.60.0-1
- Prepare for Oreon 11 (RP1)
