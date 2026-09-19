%global source0_hash c4c178fbb05f72acc484d22ddb0568f7532c409b0a13e06513ff54b91e947783

%define glib2_version 2.16.0
%define dbus_version 1.0
%define gcrypt_version 1.2.2

Name: libgnome-keyring
Version: 3.12.0
Release: 33%{?dist}
Summary: Framework for managing passwords and other secrets

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
Source0: http://download.gnome.org/sources/libgnome-keyring/3.12/libgnome-keyring-%{version}.tar.xz
URL: http://live.gnome.org/GnomeKeyring

BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: dbus-devel >= %{dbus_version}
BuildRequires: libgcrypt-devel >= %{gcrypt_version}
BuildRequires: intltool
BuildRequires: gobject-introspection-devel
BuildRequires: vala
BuildRequires: make

# https://gitlab.gnome.org/GNOME/libgnome-keyring/commit/3766bcc482f9e02fb5f9c183e814833ad1fbf08a
Patch0:  libgnome-keyring-vapi-build-fix.patch
Conflicts: gnome-keyring < 2.29.4

%description
gnome-keyring is a program that keep password and other secrets for
users. The library libgnome-keyring is used by applications to integrate
with the gnome-keyring system.

%package devel
Summary: Development files for libgnome-keyring
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts: gnome-keyring-devel < 2.29.4
Provides: gnome-keyring-devel = %{version}-%{release}

%description devel
The libgnome-keyring-devel package contains the libraries and
header files needed to develop applications that use libgnome-keyring.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-gtk-doc --enable-introspection=yes

# avoid unneeded direct dependencies
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang libgnome-keyring

%check
make check

%ldconfig_scriptlets

%files -f libgnome-keyring.lang
%license COPYING
%doc AUTHORS NEWS README HACKING
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gir-1.0
%{_datadir}/vala/
%doc %{_datadir}/gtk-doc/

%changelog
%autochangelog
