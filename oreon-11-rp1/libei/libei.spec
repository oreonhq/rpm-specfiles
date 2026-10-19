%global source0_hash 5ed6078fa63afd554cc04b1001675615da0ed8fe23b80492ab63403140b5a830
Name:           libei
Version:        1.6.0
Release:        1%{?dist}
Summary:        Library for Emulated Input
License:        MIT
URL:            http://gitlab.freedesktop.org/libinput/libei
Source0:        https://gitlab.freedesktop.org/libinput/libei/-/archive/%{version}/libei-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libxml2
BuildRequires:  meson
BuildRequires:  pkgconf-pkg-config
BuildRequires:  python3
BuildRequires:  python3-attrs
BuildRequires:  python3-jinja2
BuildRequires:  python3-rpm-macros
BuildRequires:  systemd-devel
# /oreon:deps
%description
libei is a library to Emulate Input. It allows clients to talk to
an EIS implementatation (Emulated Input Server), typically a Wayland compositor
and send input events via that connection. The EIS implementation
replays those events as if they came from physical devices.

%package devel
Summary:        Library for Emulated Input Development Package
Requires:       libei%{?_isa} = %{version}-%{release}
%description devel
Library for Emulated Input Development Package.

%package utils
Summary:        Library for Emulated Input Utilities Package
Requires:       libei%{?_isa} = %{version}-%{release}
%description utils
Utilities to test and/or debug emulated input devices.

# libeis packages
%package -n libeis
Summary:        Library for Emulated Input Servers
%description -n libeis
libeis is a library to provide logical devices that other applications
can then use to emulate input. This library is typically used by
a Wayland compositor that provides an EIS implementation.

%package -n libeis-devel
Summary:        Library for Emulated Input Servers Development Package
Requires:       libeis%{?_isa} = %{version}-%{release}
%description -n libeis-devel
Library for Emulated Input Servers Development Package.

# liboeffis packages
%package -n liboeffis
Summary:        Library for XDG RemoteDesktop Portal Setup
%description -n liboeffis
liboeffis is a helper library to contact the XDG RemoteDesktop portal
and obtain an EIS socket through the portal.

%package -n liboeffis-devel
Summary:        Library for XDG RemoteDesktop Portal Setup Development Package
Requires:       liboeffis%{?_isa} = %{version}-%{release}
%description -n liboeffis-devel
Library for XDG RemoteDesktop Portal Setup Development Package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git
# Replace whatever the source uses with the approved call
%py3_shebang_fix $(git grep -l  '#!/usr/bin/.*python3')

%build

%meson -Dtests=disabled -Ddocumentation='[]' -Dliboeffis=enabled
%meson_build
%install
%meson_install
%oreon_autofiles libeis usr/*/lib*.so.*
%oreon_autofiles libeis-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles liboeffis usr/*/lib*.so.*
%oreon_autofiles liboeffis-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libei-devel -f %{oreon_filedir}/libei-devel.list
%files -n libei-utils -f %{oreon_filedir}/libei-utils.list
%files -n libeis -f %{oreon_filedir}/libeis.list
%files -n libeis-devel -f %{oreon_filedir}/libeis-devel.list
%files -n liboeffis -f %{oreon_filedir}/liboeffis.list
%files -n liboeffis-devel -f %{oreon_filedir}/liboeffis-devel.list

%changelog

%autochangelog
