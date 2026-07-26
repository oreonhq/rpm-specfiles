%global source0_hash 7ec97633752fbde2505b40d762d933b642cae42b6b86d6e801fbdfcd2eeb5334

%global framework kwindowsystem

## uncomment to enable bootstrap mode
#global bootstrap 1

## currently includes no tests
%if !0%{?bootstrap} 
%if 0%{?fedora} || 0%{?epel}
%global tests 1
%endif
%endif

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 1 integration module with classes for windows management

License: CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

# filter plugin provides
%global __provides_exclude_from ^(%{_kf5_plugindir}/.*\\.so)$

BuildRequires: make
BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel

%if 0%{?tests}
BuildRequires: openbox
%if 0%{?fedora}
BuildRequires: weston
%endif
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires:       kf5-filesystem >= %{majmin}

%description
KDE Frameworks Tier 1 integration module that provides classes for managing and
working with windows.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build

%install
%cmake_install

%find_lang_kf5 kwindowsystem5_qt

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif

%ldconfig_scriptlets

%files -f kwindowsystem5_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5WindowSystem.so.*
%dir %{_kf5_plugindir}/kwindowsystem/
#{_kf5_plugindir}/kwindowsystem/KF5WindowSystemWaylandPlugin.so
%{_kf5_plugindir}/kwindowsystem/KF5WindowSystemX11Plugin.so

%files devel
%{_kf5_includedir}/KWindowSystem/
%{_kf5_libdir}/libKF5WindowSystem.so
%{_kf5_libdir}/cmake/KF5WindowSystem/
%{_kf5_archdatadir}/mkspecs/modules/qt_KWindowSystem.pri

%changelog
%autochangelog
