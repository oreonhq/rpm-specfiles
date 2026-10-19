%global source0_hash 96ec98be7a91f6dde33636720e3da2ff6ecbb90e76ccaa49497f31a6855a490e
%{?mingw_package_header}
%define pkgname json-glib
%define glib2_version 2.54.0
Name:           mingw-%{pkgname}
Version:        1.10.8
Release:        1%{?dist}
Summary:        MinGW compiled library for JavaScript Object Notation format
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/JsonGlib
Source0:        https://download.gnome.org/sources/%{pkgname}/1.6/%{pkgname}-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-glib2
# /oreon:deps
%description
%{name} is a library providing serialization and deserialization support
for the JavaScript Object Notation (JSON) format, compiled using MinGW.

# Win32
%package -n mingw32-%{pkgname}
Summary:       MinGW compiled %{pkgname} library for the Win32 target
%description -n mingw32-%{pkgname}
MinGW compiled %{pkgname} library for the Win32 target.

# Win64
%package -n mingw64-%{pkgname}
Summary:       MinGW compiled %{pkgname} library for the Win64 target
%description -n mingw64-%{pkgname}
MinGW compiled %{pkgname} library for the Win64 target.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-%{version}

%build

%mingw_meson -Dintrospection=disabled
%mingw_ninja
%install
export DESTDIR=%{buildroot}
%mingw_ninja install
%mingw_find_lang json-glib-1.0
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-json-glib -f %{oreon_filedir}/mingw32-json-glib.list
%files -n mingw64-json-glib -f %{oreon_filedir}/mingw64-json-glib.list

%changelog

%autochangelog
