%undefine __cmake_in_source_build
%global framework bluez-qt

Name:           kf5-%{framework}
Summary:        A Qt wrapper for Bluez
Version: 5.116.0
Release: 5%{?dist}

License:        CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/frameworks/%{framework}

%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2).50
%else
%global kf5_dl_stable stable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2)
%endif
Source0:        http://download.kde.org/%{kf5_dl_stable}/frameworks/%{kf5_dl_majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  kf5-rpm-macros >= %{version}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

# For %%{_udevrulesdir}
BuildRequires:  systemd

Requires:       kf5-filesystem >= %{version}
%if 0%{?fedora} > 22
Recommends:     bluez >= 5
%else
Requires:       bluez >= 5
%endif

%if 0%{?fedora} >= 22
## libbluedevil 5.2.2 was the last release
Obsoletes:      libbluedevil < 5.2.90
%endif

%description
BluezQt is Qt-based library written handle all Bluetooth functionality.

%package        devel
Summary:        Development files for %{name}
%if 0%{?fedora} >= 22
## libbluedevil 5.2.2 was the last release
Obsoletes:      libbluedevil-devel < 5.2.90
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
Development files for %{name}.


%prep
%autosetup -n %{framework}-%{version}


%build
%{cmake_kf5} \
  -DUDEV_RULES_INSTALL_DIR:PATH="%{_udevrulesdir}"
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/*categories
%{_libdir}/libKF5BluezQt.so.*
%{_kf5_qmldir}/org/kde/bluezqt/
%{_udevrulesdir}/61-kde-bluetooth-rfkill.rules

%files devel
%{_kf5_includedir}/BluezQt/

%{_kf5_libdir}/libKF5BluezQt.so
%{_kf5_libdir}/cmake/KF5BluezQt/
%{_kf5_libdir}/pkgconfig/KF5BluezQt.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_BluezQt.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
