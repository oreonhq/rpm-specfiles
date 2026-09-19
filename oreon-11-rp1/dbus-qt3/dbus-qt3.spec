%global source0_hash 45b0698da89627b49dc1ee66d2819c23eaec82316ef1316b8deeeb3d41a00e01

# fedora package review: http://bugzilla.redhat.com/429760

%define qt3pkg qt
%if 0%{?fedora} > 8
%define qt3pkg qt3
%endif

Name:    dbus-qt3
Summary: Qt3 DBus Bindings
Version: 0.9
Release: 41%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Url:     http://www.freedesktop.org/wiki/Software/DBusBindings
Source0: http://people.freedesktop.org/~krake/dbus-1-qt3/dbus-1-qt3-%{version}.tar.gz

Patch0:  dbus-1-qt3-0.9-libtool-aarch64.patch
Patch1:  dbus-qt3-configure-c99.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: dbus-devel
BuildRequires: %{qt3pkg}-devel
BuildRequires: make

Provides: dbus-1-qt3 = %{version}-%{release}

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

# unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la

%ldconfig_scriptlets

%files
%doc README AUTHORS ChangeLog COPYING
%{_libdir}/lib*.so.*

%files devel
%{_bindir}/dbusxml2qt3
%{_libdir}/lib*.so
%{_includedir}/dbus-1.0/qt3/
%{_libdir}/pkgconfig/dbus-1-qt3.pc

%changelog
%autochangelog
