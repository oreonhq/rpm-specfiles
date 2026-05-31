%global source0_hash c36b28f10ffcc8f1f798aca973bcc132f91f33eb9b6b8904381b4077766043d5

Name:    dbus-python
Version: 1.4.0
Release: %autorelease
Summary: D-Bus Python Bindings

License: MIT
URL:     http://www.freedesktop.org/wiki/Software/DBusBindings/
Source0:        http://dbus.freedesktop.org/releases/dbus-python/%{name}-%{version}.tar.xz

BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(glib-2.0)
# for %%check
BuildRequires: dbus-x11
BuildRequires: python3-gobject

BuildRequires: gcc
BuildRequires: meson

%global _description\
D-Bus python bindings for use with python programs.

%description %_description

%package -n python3-dbus
Summary: D-Bus bindings for python3
%{?python_provide:%python_provide python3-dbus}
BuildRequires: python3-devel
# for py3_build
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
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%py3_install

%check
%meson_test

%files -n python3-dbus
%doc NEWS
%license COPYING
%{python3_sitearch}/*.so
%{python3_sitearch}/dbus/
%{python3_sitearch}/dbus_python*egg-info

%files devel
%doc README ChangeLog doc/API_CHANGES.txt doc/tutorial.txt
%{_includedir}/dbus-1.0/dbus/dbus-python.h
%{_libdir}/pkgconfig/dbus-python.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.0-1
- Prepare for Oreon 11 (RP1)
