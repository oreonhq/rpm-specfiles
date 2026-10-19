%global stable_kf6 stable
%global source0_hash aeac3ec0fa39a26cf9bacd87a30f5d8cf2968116ca99902873499b6cd45f9b17
Name:           kpublictransport
Version:        26.04.3
Release:        1%{?dist}
License:        CC0-1.0 AND ODbL-1.0 AND LGPL-2.1-or-later AND BSD-2-Clause AND MIT AND LGPL-2.0-or-later AND BSD-3-Clause
Summary:        Library to assist with accessing public transport timetables and other data
Url:            https://invent.kde.org/libraries/kpublictransport
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires: qt6qml(org.kde.kitemmodels)
# oreon:deps
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Location)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(polyclipping)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 -DBUILD_QCH=OFF -DQT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kpublictransport-devel -f %{oreon_filedir}/kpublictransport-devel.list
%files -n kpublictransport-doc -f %{oreon_filedir}/kpublictransport-doc.list

%changelog

%autochangelog

