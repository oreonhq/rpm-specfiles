%global source0_hash 9e7f9c2ac3d22dec3baa0a0fc17a9366ffb442c41cdb81c37cf65ca462eac55f

%global framework kdeclarative

# uncomment to enable bootstrap mode
%global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 addon for Qt declarative

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.1-only OR LGPL-3.0-only AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

# filter qml provides
%global __provides_exclude_from ^%{_kf5_qmldir}/.*\\.so$

## upstream patches

BuildRequires: make
BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kglobalaccel-devel >= %{majmin}
BuildRequires:  kf5-kguiaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kiconthemes-devel >= %{majmin}
BuildRequires:  kf5-kio-devel >= %{majmin}
BuildRequires:  kf5-knotifications-devel >= %{majmin}
BuildRequires:  kf5-kpackage-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-kwindowsystem-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros

BuildRequires:  libepoxy-devel

BuildRequires:  qt5-qtbase-devel

# https://bugs.kde.org/show_bug.cgi?id=365569#c8 claims this may be needed,
# so err on the side of caution
BuildRequires:  qt5-qtbase-private-devel

BuildRequires:  qt5-qtdeclarative-devel

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: mesa-dri-drivers
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

%description
KDE Frameworks 5 Tier 3 addon for Qt declarative

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kconfig-devel >= %{majmin}
Requires:       kf5-kpackage-devel >= %{majmin}
Requires:       qt5-qtdeclarative-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{framework}-%{version}

%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make test ARGS="--output-on-failure --timeout 10 --verbose" -C %{_target_platform} ||:
%endif

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_bindir}/kpackagelauncherqml
%{_kf5_libdir}/libKF5Declarative.so.*
%{_kf5_libdir}/libKF5QuickAddons.so.*
%{_kf5_libdir}/libKF5CalendarEvents.so.*
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/draganddrop/
%{_kf5_qmldir}/org/kde/graphicaleffects/
%{_kf5_qmldir}/org/kde/kconfig/
%{_kf5_qmldir}/org/kde/kcoreaddons/
%{_kf5_qmldir}/org/kde/kquickcontrols/
%{_kf5_qmldir}/org/kde/kquickcontrolsaddons/
%dir %{_kf5_qmldir}/org/kde/private/
%{_kf5_qmldir}/org/kde/private/kquickcontrols/
%{_kf5_qmldir}/org/kde/kio/
%{_kf5_qmldir}/org/kde/kwindowsystem/
%{_kf5_qmldir}/org/kde/kcm/

%files devel

%{_kf5_includedir}/KDeclarative/
%{_kf5_libdir}/libKF5Declarative.so
%{_kf5_libdir}/libKF5QuickAddons.so
%{_kf5_libdir}/libKF5CalendarEvents.so
%{_kf5_libdir}/cmake/KF5Declarative/
%{_kf5_archdatadir}/mkspecs/modules/qt_KDeclarative.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_QuickAddons.pri

%changelog
%autochangelog
