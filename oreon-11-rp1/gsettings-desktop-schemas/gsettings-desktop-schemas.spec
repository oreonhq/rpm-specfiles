# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1e2419a5f21d26c324b28ae1c00e29e9175e8b596fff385a04c2172b36652226
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global debug_package %{nil}

%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)

Name:           gsettings-desktop-schemas
Version:        51.0
Release:        1%{?dist}
Summary:        A collection of GSettings schemas

License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/gsettings-desktop-schemas
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires:  gettext
BuildRequires:  glib2-devel >= 2.31.0
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson

Requires: glib2 >= 2.31.0

%if 0%{?rhel} && 0%{?rhel} >= 10
Recommends: font(redhattextvf)
Recommends: font(redhatmonovf)
%else
Recommends: font(adwaitasans)
Recommends: font(adwaitamono)
%endif

%description
gsettings-desktop-schemas contains a collection of GSettings schemas for
settings shared by various components of a desktop.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries
and header files for developing applications that use %{name}.

%prep
%oreon_sha256
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%check
glib-compile-schemas --dry-run --strict %{buildroot}%{_datadir}/glib-2.0/schemas

%files -f %{name}.lang
%doc AUTHORS MAINTAINERS NEWS README
%license COPYING
%{_datadir}/glib-2.0/schemas/*
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/gsettings-desktop-schemas.convert
%{_datadir}/GConf/gsettings/wm-schemas.convert
%{_libdir}/girepository-1.0/GDesktopEnums-3.0.typelib

%files devel
%doc HACKING
%{_includedir}/*
%{_datadir}/pkgconfig/*
%{_datadir}/gir-1.0/GDesktopEnums-3.0.gir

%changelog
%autochangelog
