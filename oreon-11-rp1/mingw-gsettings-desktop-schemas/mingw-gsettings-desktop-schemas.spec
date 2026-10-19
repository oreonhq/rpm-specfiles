%global source0_hash 1e2419a5f21d26c324b28ae1c00e29e9175e8b596fff385a04c2172b36652226
%{?mingw_package_header}
%global release_version %(echo %{version} | awk -F. '{print $1}')
Name:           mingw-gsettings-desktop-schemas
Version:        51.0
Release:        1%{?dist}
Summary:        MinGW Windows gsettings-desktop-schemas
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/gsettings-desktop-schemas
Source0:        https://download.gnome.org/sources/gsettings-desktop-schemas/%{release_version}/gsettings-desktop-schemas-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  gettext
BuildRequires:  glib2
BuildRequires:  meson
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-glib2
# /oreon:deps
%description
This package contains a collection of GSettings schemas for
settings shared by various components of a desktop.

%package -n mingw32-gsettings-desktop-schemas
Summary:        MinGW Windows gsettings-desktop-schemas
%description -n mingw32-gsettings-desktop-schemas
This package contains a collection of GSettings schemas for
settings shared by various components of a desktop.

%package -n mingw64-gsettings-desktop-schemas
Summary:        MinGW Windows gsettings-desktop-schemas
%description -n mingw64-gsettings-desktop-schemas
This package contains a collection of GSettings schemas for
settings shared by various components of a desktop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gsettings-desktop-schemas-%{version}
%oreon_prep
%build

%mingw_meson -Dintrospection=false
%mingw_ninja
%install
%mingw_ninja_install
%mingw_find_lang %{name} --all-name
%oreon_autofiles mingw32-gsettings-desktop-schemas usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gsettings-desktop-schemas usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-gsettings-desktop-schemas -f %{oreon_filedir}/mingw32-gsettings-desktop-schemas.list
%files -n mingw64-gsettings-desktop-schemas -f %{oreon_filedir}/mingw64-gsettings-desktop-schemas.list

%changelog

%autochangelog
