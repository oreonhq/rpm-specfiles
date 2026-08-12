%global source0_hash 537cee9bbadf5471e5217e48605adbf941335de45f0041e7d5a31422e4b49ff1

%undefine __cmake_in_source_build
%global framework kitemmodels

Name:           kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with item models

License:        CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)

Requires:       kf5-filesystem >= %{majmin}

%description
KDE Frameworks 5 Tier 1 addon with item models.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5ItemModels.so.*
%{_kf5_qmldir}/org/kde/kitemmodels/

%files devel

%{_kf5_includedir}/KItemModels/
%{_kf5_libdir}/libKF5ItemModels.so
%{_kf5_libdir}/cmake/KF5ItemModels/
%{_kf5_archdatadir}/mkspecs/modules/qt_KItemModels.pri

%changelog
%autochangelog
