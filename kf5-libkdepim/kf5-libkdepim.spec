%global framework libkdepim

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: Library for common kdepim apps

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  boost-devel
%global kf5_ver 5.71
BuildRequires:  extra-cmake-modules >= %{kf5_ver}
BuildRequires:  kf5-rpm-macros >= %{kf5_ver} 
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)

BuildRequires:  cmake(Qt5Designer)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)

#global majmin_ver %(echo %{version} | cut -d. -f1,2)
#global majmin_ver %{version}

Obsoletes:      kdepim-libs < 7:16.04.0
Conflicts:      kdepim-libs < 7:16.04.0
# kdepimwidgets designer plugin moved here
Conflicts:      kdepim-common < 16.04.0
# kcm_ldap moved here
Conflicts:      kaddressbook < 16.04.0

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version}

# Rename translation files to avoid conflict with KF6
find ./po -type f -execdir mv {} libkdepim5.po \;
sed -i '0,/ecm_set_disabled_deprecation_versions/s//add_definitions(-DTRANSLATION_DOMAIN=\\"libkdepim5\\")\n&/' CMakeLists.txt
sed -i "s/libkdepim/libkdepim5/" src/Messages.sh


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5Libkdepim.so.5
%{_kf5_libdir}/libKPim5Libkdepim.so.5.*

%ldconfig_scriptlets akonadi

%files devel
%{_includedir}/KPim5/Libkdepim/
%{_kf5_libdir}/cmake/KF5Libkdepim/
%{_kf5_libdir}/cmake/KPim5Libkdepim/
%{_kf5_libdir}/cmake/KPim5MailTransportDBusService/
%{_kf5_libdir}/libKPim5Libkdepim.so
%{_kf5_archdatadir}/mkspecs/modules/qt_Libkdepim.pri
%{_kf5_libdir}/cmake/MailTransportDBusService/
%{_kf5_datadir}/dbus-1/interfaces/org.kde.addressbook.service.xml
%{_kf5_datadir}/dbus-1/interfaces/org.kde.mailtransport.service.xml
%{_kf5_qtplugindir}/designer/kdepim5widgets.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-5
- Prepare for Oreon 11 (RP1)
