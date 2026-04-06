%global base_name libkipi

Name:    kf5-libkipi
Summary: Common plugin infrastructure for KDE image applications
Version: 24.05.2
Release: 5%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/graphics/%{base_name}
%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%else
%global kf5_dl_stable stable
%endif
Source0: http://download.kde.org/%{kf5_dl_stable}/release-service/%{version}/src/%{base_name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-rpm-macros
BuildRequires: pkgconfig(Qt5Gui)

%if 0%{?fedora} > 23
Recommends: kf5-kipi-plugins
%endif

%description
Kipi (KDE Image Plugin Interface) is an effort to develop a common plugin
structure (for Digikam, Gwenview, etc.). Its aim is to share
image plugins among graphic applications.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
#Requires: qt5-qtbase-devel
#Requires: kf5-kconfig-devel
#Requires: kf5-kxmlgui-devel
#Requires: kf5-kservice-devel
Requires: cmake(Qt5Gui)
Requires: cmake(KF5Config)
Requires: cmake(KF5Service)
Requires: cmake(KF5XmlGui)
%description devel
%{summary}.


%prep
%autosetup  -n %{base_name}-%{version} -p1


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%doc AUTHORS README
%license LICENSES/*
%{_kf5_libdir}/libKF5Kipi.so.*
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/kservicetypes5/kipiplugin.desktop
%{_kf5_datadir}/qlogging-categories5/kipi.categories

%files devel
%{_kf5_libdir}/libKF5Kipi.so
%{_kf5_includedir}/KIPI/
%{_kf5_libdir}/cmake/KF5Kipi/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 24.05.2-5
- Prepare for Oreon 11 (RP1)
