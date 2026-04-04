%global framework solid

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:           kf6-%{framework}
Version:        6.24.0
Release:	3%{?dist}
Summary:        KDE Frameworks 6 Tier 1 integration module that provides hardware information
License:        LGPL-2.1-or-later AND LGPL-2.1-only AND CCO-1.0 AND BSD-3-Clause AND LGPL-3.0-only
URL:            https://solid.kde.org/
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules >= %{majmin_ver_kf6}
Requires:       kf6-filesystem
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Tools)
BuildRequires:  libupnp-devel
BuildRequires:  systemd-devel
BuildRequires:  libmount-devel
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  pkgconfig(libplist++-2.0)
BuildRequires:  pkgconfig(libimobiledevice-1.0)

BuildRequires:  media-player-info
Recommends:     media-player-info
Recommends:     udisks2
Recommends:     upower

%description
Solid provides the following features for application developers:
 - Hardware Discovery
 - Power Management
 - Network Management

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang_kf6 solid6_qt

%files -f solid6_qt.lang
%doc README.md TODO
%license LICENSES/*.txt
%{_kf6_bindir}/solid-hardware6
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Solid.so.6
%{_kf6_libdir}/libKF6Solid.so.%{version}

%files devel
%{_kf6_includedir}/Solid/
%{_kf6_libdir}/cmake/KF6Solid/
%{_kf6_libdir}/libKF6Solid.so

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
