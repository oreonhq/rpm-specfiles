%global framework kdbusaddons

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 1 addon with various classes on top of QtDBus

License: CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel

Requires:       kf5-filesystem >= %{majmin}

%description
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version}


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang_kf5 kdbusaddons5_qt


%ldconfig_scriptlets

%files -f kdbusaddons5_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}*
%{_kf5_bindir}/kquitapp5
%{_kf5_libdir}/libKF5DBusAddons.so.*

%files devel
%{_kf5_includedir}/KDBusAddons/
%{_kf5_libdir}/libKF5DBusAddons.so
%{_kf5_libdir}/cmake/KF5DBusAddons/
%{_kf5_archdatadir}/mkspecs/modules/qt_KDBusAddons.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
