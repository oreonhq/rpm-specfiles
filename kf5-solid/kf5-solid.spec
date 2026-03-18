%global framework solid

Name:    kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary: KDE Frameworks 5 Tier 1 integration module that provides hardware information

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://solid.kde.org/

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

## upstreamable patches

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  libupnp-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  systemd-devel

%if ! 0%{?bootstrap}
# Predicate parser deps
BuildRequires:  bison
BuildRequires:  flex
# really runtime-only dep, but doesn't hurt to check availability at buildtime
BuildRequires:  media-player-info
BuildRequires:  pkgconfig(libimobiledevice-1.0)
BuildRequires:  pkgconfig(mount)
%if 0%{?fedora} > 23 || 0%{?rhel} > 7
Recommends:     media-player-info
Recommends:     udisks2
Recommends:     upower
%else
Requires:       media-player-info
Requires:       udisks2
Requires:       upower
%endif
%endif

Requires:       kf5-filesystem

Obsoletes:      kf5-solid-libs < 5.47.0-2
Provides:       kf5-solid-libs = %{version}-%{release}
Provides:       kf5-solid-libs%{?_isa} = %{version}-%{release}

%description
Solid provides the following features for application developers:
 - Hardware Discovery
 - Power Management
 - Network Management

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1
# do not build the solid-power executable, it conflicts with KF6 Solid
sed -i -e 's/if(WITH_NEW_SOLID_JOB AND WITH_NEW_POWER_ASYNC_API)/if(0)/g' \
  src/tools/CMakeLists.txt


%build
%cmake_kf5 \
  -DWITH_NEW_POWER_ASYNC_API:BOOL=ON \
  -DWITH_NEW_POWER_ASYNC_FREEDESKTOP:BOOL=ON \
  -DWITH_NEW_SOLID_JOB:BOOL=ON

%cmake_build


%install
%cmake_install

%find_lang_kf5 solid5_qt


%ldconfig_scriptlets

%files -f solid5_qt.lang
%doc README.md TODO
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_bindir}/solid-hardware5
#files libs
%{_kf5_qmldir}/org/kde/solid/
%{_kf5_libdir}/libKF5Solid.so.*

%files devel
%{_kf5_includedir}/Solid/
%{_kf5_libdir}/libKF5Solid.so
%{_kf5_libdir}/cmake/KF5Solid/
%{_kf5_archdatadir}/mkspecs/modules/qt_Solid.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-7
- Prepare for Oreon 11 (RP1)
