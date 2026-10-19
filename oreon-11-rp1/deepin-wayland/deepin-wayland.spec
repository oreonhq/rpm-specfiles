%global source0_hash 428ac3910f64012b89e12a7abce3fd631477f1455e61b9e9d4e503a56ad9d448
%global repo dde-wayland
Name:           deepin-wayland
Version:        1.0.0
Release:        1%{?dist}
Summary:        Deepin Wayland libraries
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        https://github.com/linuxdeepin/%{repo}/archive/%{version}/%{repo}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libxkbcommon-devel
BuildRequires:  make
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtwayland-devel
BuildRequires:  wayland-devel
# /oreon:deps
%description
This package provides Wayland libraries with Deepin customization.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Header files and libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{repo}-%{version}

%build

%qmake_qt5 LIB_INSTALL_DIR=%_libdir
%make_build
%install
%make_install INSTALL_ROOT=%buildroot
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n deepin-wayland-devel -f %{oreon_filedir}/deepin-wayland-devel.list

%changelog

%autochangelog
