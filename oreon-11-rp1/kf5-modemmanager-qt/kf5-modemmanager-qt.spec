%undefine __cmake_in_source_build
%global framework modemmanager-qt


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kf5-%{framework}
Version: 5.116.0
Release: 6%{?dist}
Summary: A Tier 1 KDE Frameworks module wrapping ModemManager DBus API

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/modemmanager-qt-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}

BuildRequires:  ModemManager-devel >= 1.0.0
BuildRequires:  qt5-qtbase-devel

Requires:       kf5-filesystem >= %{majmin}

%description
A Qt 5 library for ModemManager.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ModemManager-devel
Requires:       qt5-qtbase-devel
%description    devel
Qt 5 libraries and header files for developing applications
that use ModemManager.


%prep
%autosetup -n %{framework}-%{version}


%build
%cmake_kf5

%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%doc README README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/*categories
%{_kf5_datadir}/qlogging-categories5/*.categories
%{_kf5_libdir}/libKF5ModemManagerQt.so.*

%files devel
%{_kf5_libdir}/libKF5ModemManagerQt.so
%{_kf5_libdir}/cmake/KF5ModemManagerQt/
%{_kf5_includedir}/ModemManagerQt/

#{_kf5_archdatadir}/mkspecs/modules/qt_ModemManagerQt.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-6
- Prepare for Oreon 11 (RP1)
