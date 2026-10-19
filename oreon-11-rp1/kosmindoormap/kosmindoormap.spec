%global stable_kf6 stable
%global source0_hash 1da64c99c29fbd3f722732a14d44ab67417e66cec8de179fa5b2ec676aa6331b
Name:    kosmindoormap
Version: 25.12.3
Release:        1%{?dist}
Summary:        OSM multi-floor indoor map renderer
License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-3.0-or-later AND MIT AND ODbL-1.0
URL:     https://invent.kde.org/libraries/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires:       kf6-filesystem
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KOpeningHours)
BuildRequires:  cmake(KPublicTransport)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  extra-cmake-modules
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  openssl-devel
BuildRequires:  osmctools
BuildRequires:  protobuf-devel
BuildRequires:  protobuf-lite-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  rsync
BuildRequires:  zlib-devel
# /oreon:deps
%description
A library and QML component for rendering multi-level OSM indoor
maps of for example a (large) train station.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kosmindoormap-devel -f %{oreon_filedir}/kosmindoormap-devel.list

%changelog

%autochangelog
