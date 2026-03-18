%global framework frameworkintegration

Name:    kf5-%{framework}
Version: 5.116.0
Release: 11%{?dist}
Summary: KDE Frameworks 5 Tier 4 workspace and cross-framework integration plugins
License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

## upstream patches (lookaside cache)

# filter plugin provides
%global __provides_exclude_from ^(%{_kf5_plugindir}/.*\\.so)$

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kconfigwidgets-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kiconthemes-devel >= %{majmin}
BuildRequires:  kf5-kio-devel >= %{majmin}
BuildRequires:  kf5-knewstuff-devel >= %{majmin}
BuildRequires:  kf5-knotifications-devel >= %{majmin}
BuildRequires:  kf5-kpackage-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}

BuildRequires:  libXcursor-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
%if 0%{?fedora} > 23 && 0%{?fedora} < 40
%global appstream 1
BuildRequires:  cmake(AppStreamQt)
BuildRequires:  cmake(packagekitqt5)
%endif

# prior to 5.11.0-3, main pkg was multilib'd (due to arch'd -devel deps) -- rex
Obsoletes:      %{name} < 5.11.0-3
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

## consider removing for f28+, since Qt5 tracks via versioned symbols now -- rex
BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

%description
Framework Integration is a set of plugins responsible for better integration of
Qt applications when running on a KDE Plasma workspace.

Applications do not need to link to this directly.

%package        libs
Summary:        Runtime libraries for %{name}.
Requires:       %{name} = %{version}-%{release}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kf5-kiconthemes-devel >= %{majmin}
Requires:       kf5-kconfigwidgets-devel >= %{majmin}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{framework}-%{version}


%build
%cmake_kf5

%cmake_build


%install
%cmake_install


%files
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/kf5/infopage/
%{_kf5_datadir}/knotifications5/plasma_workspace.notifyrc
%dir %{_kf5_libexecdir}/kpackagehandlers
%{_kf5_libexecdir}/kpackagehandlers/knshandler
# move to subpkg? -- rex
%if 0%{?appstream}
%{_kf5_libexecdir}/kpackagehandlers/appstreamhandler
%endif

%ldconfig_scriptlets libs

%files libs
%{_kf5_libdir}/libKF5Style.so.*
%{_kf5_plugindir}/FrameworkIntegrationPlugin.so

%files devel
%{_kf5_includedir}/FrameworkIntegration/
%{_kf5_includedir}/KStyle/
%{_kf5_libdir}/libKF5Style.so
%{_kf5_libdir}/cmake/KF5FrameworkIntegration/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-11
- Prepare for Oreon 11 (RP1)
