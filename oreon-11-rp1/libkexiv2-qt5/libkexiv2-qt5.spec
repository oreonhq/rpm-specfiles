%global stable_kf6 stable
%global source0_hash 0806898554b62a6f834d33bb481923d82bde91b1692ba7b146fec94b9a503d03
Name:    libkexiv2-qt5
Summary:        A wrapper around Exiv2 library
Version: 25.08.3
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/graphics/libkexiv2
Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/libkexiv2-%{version}.tar.xz
Obsoletes: kf5-libkexiv2 < %{version}-%{release}
Provides:  kf5-libkexiv2 = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(exiv2)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
# /oreon:deps
%description

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt5Gui)
Obsoletes: kf5-libkexiv2-devel < %{version}-%{release}
Provides:  kf5-libkexiv2-devel = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libkexiv2-%{version}
%oreon_prep
%build

%cmake_kf5 -DBUILD_WITH_QT6=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libkexiv2-qt5-devel -f %{oreon_filedir}/libkexiv2-qt5-devel.list

%changelog

%autochangelog
