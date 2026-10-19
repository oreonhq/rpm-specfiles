%global source0_hash 45b0698da89627b49dc1ee66d2819c23eaec82316ef1316b8deeeb3d41a00e01
%define qt3pkg qt
Name:    dbus-qt3
Summary:        Qt3 DBus Bindings
Version: 0.9
Release:        41%{?dist}
License: GPL-2.0-or-later
Url:     http://www.freedesktop.org/wiki/Software/DBusBindings
Source0:        http://people.freedesktop.org/~krake/dbus-1-qt3/dbus-1-qt3-%{version}.tar.gz
Patch0:  dbus-1-qt3-0.9-libtool-aarch64.patch
Patch1:  dbus-qt3-configure-c99.patch
Provides: dbus-1-qt3 = %{version}-%{release}
# oreon:deps
BuildRequires:  dbus-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt-devel
# /oreon:deps
%description
This library provides Qt3-classes for accessing the DBus.

%package devel
Summary: Development files for %{name} 
Provides: dbus-1-qt3-devel = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: dbus-devel
Requires: %{qt3pkg}-devel
Requires: pkgconfig
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n dbus-1-qt3-%{version}
%patch -P0 -p1 -b .libtool-aarch64
%patch -P1 -p1 -b .configure-c99

%build

%configure \
  --disable-static \
  --disable-warnings
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dbus-qt3-devel -f %{oreon_filedir}/dbus-qt3-devel.list

%changelog

%autochangelog
