%global source0_hash 06055351f3a6f8755df60f48b3fdaabb4a406939b9c777f474e8a22bdd116f80

%undefine __cmake_in_source_build
%global framework modemmanager-qt

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kf5-%{framework}
Version: 5.116.0
Release: 8%{?dist}
Summary: A Tier 1 KDE Frameworks module wrapping ModemManager DBus API

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/modemmanager-qt-%{version}.tar.xz

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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
%autochangelog
