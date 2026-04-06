%global framework kcmutils

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
## currently includes no tests, consider re-enabling when it does
#global tests 1
%endif

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 addon with extra API to write KConfigModules

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
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
BuildRequires:  kf5-kconfigwidgets-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kdeclarative-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kguiaddons-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-ki18n-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kiconthemes-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kitemviews-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kpackage-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kservice-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-kxmlgui-devel >= %{kf5_dl_majmin}
BuildRequires:  kf5-rpm-macros

BuildRequires:  cmake(KF5GuiAddons)

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

%description
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kconfigwidgets-devel >= %{kf5_dl_majmin}
Requires:       kf5-kservice-devel >= %{kf5_dl_majmin}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name

# create/own dirs
mkdir -p %{buildroot}%{_kf5_qtplugindir}/kcms


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make test ARGS="--output-on-failure --timeout 300" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5KCMUtils.so.*
%{_kf5_libdir}/libKF5KCMUtilsCore.so.*
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_qtplugindir}/kcms/
%{_kf5_qmldir}/org/kde/kcmutils/

%files devel
%{_kf5_includedir}/KCMUtils/
%{_kf5_includedir}/KCMUtilsCore/
%{_kf5_libdir}/libKF5KCMUtils.so
%{_kf5_libdir}/libKF5KCMUtilsCore.so
%{_kf5_libdir}/cmake/KF5KCMUtils/
%{_kf5_archdatadir}/mkspecs/modules/qt_KCMUtils.pri
%{_kf5_libexecdir}/kcmdesktopfilegenerator


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
