%global source0_hash c36b28f10ffcc8f1f798aca973bcc132f91f33eb9b6b8904381b4077766043d5
Name:    dbus-python
Version: 1.4.0
Release:        1%{?dist}
Summary:        D-Bus Python Bindings
License: MIT
URL:     http://www.freedesktop.org/wiki/Software/DBusBindings/
Source0:        http://dbus.freedesktop.org/releases/dbus-python/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  dbus-x11
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3dist(ninja)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
# /oreon:deps
%description
D-Bus Python Bindings

%package -n python3-dbus
Summary: D-Bus bindings for python3
%{?python_provide:%python_provide python3-dbus}
BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(setuptools-scm)
BuildRequires: python3dist(pip)
BuildRequires: python3dist(ninja)
BuildRequires: make
%description -n python3-dbus
%{summary}.

%package devel
Summary: Libraries and headers for dbus-python
%description devel
Headers and static libraries for hooking up custom mainloops to the dbus python
bindings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%py3_install
%oreon_autofiles python3-dbus usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dbus-python-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n python3-dbus -f %{oreon_filedir}/python3-dbus.list
%files -n dbus-python-devel -f %{oreon_filedir}/dbus-python-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.0-1
- Prepare for Oreon 11 (RP1)
