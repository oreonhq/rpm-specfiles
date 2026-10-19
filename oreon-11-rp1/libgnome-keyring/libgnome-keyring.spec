%global source0_hash c4c178fbb05f72acc484d22ddb0568f7532c409b0a13e06513ff54b91e947783
%define glib2_version 2.16.0
%define dbus_version 1.0
%define gcrypt_version 1.2.2
Name: libgnome-keyring
Version: 3.12.0
Release:        1%{?dist}
Summary:        Framework for managing passwords and other secrets
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
Source0:        http://download.gnome.org/sources/libgnome-keyring/3.12/libgnome-keyring-%{version}.tar.xz
URL: http://live.gnome.org/GnomeKeyring
Patch0:  libgnome-keyring-vapi-build-fix.patch
Conflicts: gnome-keyring < 2.29.4
# oreon:deps
BuildRequires:  dbus-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  libgcrypt-devel
BuildRequires:  make
BuildRequires:  vala
# /oreon:deps
%description
gnome-keyring is a program that keep password and other secrets for
users. The library libgnome-keyring is used by applications to integrate
with the gnome-keyring system.

%package devel
Summary: Development files for libgnome-keyring
License: LicenseRef-Callaway-LGPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts: gnome-keyring-devel < 2.29.4
Provides: gnome-keyring-devel = %{version}-%{release}
%description devel
The libgnome-keyring-devel package contains the libraries and
header files needed to develop applications that use libgnome-keyring.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-gtk-doc --enable-introspection=yes
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la
%find_lang libgnome-keyring
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libgnome-keyring-devel -f %{oreon_filedir}/libgnome-keyring-devel.list

%changelog

%autochangelog
