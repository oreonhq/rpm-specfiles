%global source0_hash aeac3ec0fa39a26cf9bacd87a30f5d8cf2968116ca99902873499b6cd45f9b17

Name:           kpublictransport
Version:        26.04.3
Release:        1%{?dist}
License:        CC0-1.0 AND ODbL-1.0 AND LGPL-2.1-or-later AND BSD-2-Clause AND MIT AND LGPL-2.0-or-later AND BSD-3-Clause
Summary:        Library to assist with accessing public transport timetables and other data
Url:            https://invent.kde.org/libraries/kpublictransport
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/kpublictransport-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: zlib-devel

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Location)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: qt6-qtbase-private-devel

BuildRequires: pkgconfig(polyclipping)
BuildRequires: pkgconfig(protobuf)

BuildRequires: gettext

Requires: qt6qml(org.kde.kitemmodels)

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

%autosetup

%build
%cmake_kf6 -DBUILD_QCH=OFF -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%{_kf6_datadir}/qlogging-categories6/org_kde_kpublictransport.categories
%{_kf6_libdir}/libKPublicTransport.so.1
%{_kf6_libdir}/libKPublicTransport.so.%{version}
%{_kf6_libdir}/libKPublicTransportOnboard.so.1
%{_kf6_libdir}/libKPublicTransportOnboard.so.%{version}
%{_kf6_qmldir}/org/kde/kpublictransport/*
%{_kf6_datadir}/qlogging-categories6/org_kde_kpublictransport_onboard.categories


%files devel
%{_includedir}/*
%{_kf6_libdir}/cmake/*
%{_kf6_libdir}/*.so

%files doc

%changelog
%autochangelog

