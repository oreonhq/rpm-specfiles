%global source0_hash 91288dbd552d9d29758b9f73a79b8ec091d33b143158605ea0de8dcd11185c19

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

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kconfigwidgets-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kdeclarative-devel >= %{majmin}
BuildRequires:  kf5-kguiaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kiconthemes-devel >= %{majmin}
BuildRequires:  kf5-kitemviews-devel >= %{majmin}
BuildRequires:  kf5-kpackage-devel >= %{majmin}
BuildRequires:  kf5-kservice-devel >= %{majmin}
BuildRequires:  kf5-kxmlgui-devel >= %{majmin}
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
Requires:       kf5-kconfigwidgets-devel >= %{majmin}
Requires:       kf5-kservice-devel >= %{majmin}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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
%autochangelog
