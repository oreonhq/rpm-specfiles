%global framework kauth

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 2 integration module to perform actions as privileged user

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2).50
%else
%global kf5_dl_stable stable
%global kf5_dl_majmin %(echo %{version} | cut -d. -f1,2)
%endif
Source0: http://download.kde.org/%{kf5_dl_stable}/frameworks/%{kf5_dl_majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{kf5_dl_majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-rpm-macros

BuildRequires:  polkit-qt5-1-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel

%description
KAuth is a framework to let applications perform actions as a privileged user.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kcoreaddons-devel >= %{kf5_dl_majmin}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf5 \
  -DKDE_INSTALL_LIBEXECDIR=%{_kf5_libexecdir}

%cmake_build


%install
%cmake_install

%find_lang_kf5 kauth5_qt


%ldconfig_scriptlets

%files -f kauth5_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5Auth.so.5*
%{_kf5_libdir}/libKF5AuthCore.so.5*
%{_kf5_datadir}/dbus-1/system.d/org.kde.kf5auth.conf
%{_kf5_qtplugindir}/kauth/
%{_kf5_datadir}/kf5/kauth/
%{_kf5_libexecdir}/kauth/

%files devel
%{_kf5_includedir}/KAuth/
%{_kf5_includedir}/KAuthCore/
%{_kf5_includedir}/KAuthWidgets/
%{_kf5_libdir}/libKF5Auth.so
%{_kf5_libdir}/libKF5AuthCore.so
%{_kf5_libdir}/cmake/KF5Auth/
%{_kf5_archdatadir}/mkspecs/modules/qt_KAuth*.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
