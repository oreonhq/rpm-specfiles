%global source0_hash 1e59690f5e74b2a23ec91564e8c5d03baffa8a3c6243d935c0f299a54d2e44ea
Name:           libqtxdg
Summary:        QtXdg, a Qt6 implementation of XDG standards
Version:        4.4.0
Release:        1%{?dist}
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://lxqt-project.org
Source0:        https://github.com/lxqt/libqtxdg/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       xdg-user-dirs
Requires:       xdg-utils
Obsoletes:      libqtxdg-qt5 <= 1.1.0
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  file-devel
BuildRequires:  gcc-c++
BuildRequires:  lxqt-build-tools
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        Qt - development files for qtxdg
Obsoletes:      libqtxdg-qt5-devel <= 1.1.0
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Files used for developing and building software that uses qtxdg.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libqtxdg-devel -f %{oreon_filedir}/libqtxdg-devel.list

%changelog

%autochangelog
