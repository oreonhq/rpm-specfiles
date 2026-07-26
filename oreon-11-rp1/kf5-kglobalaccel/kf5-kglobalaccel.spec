%global source0_hash f6dfaa2482c8a4dfc12ed40094fd120bd41c5053899d3f85c2ff6b8215659866

%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]

%global framework kglobalaccel

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 integration module for global shortcuts

License: CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

## upstream fixes

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kcrash-devel >= %{majmin}
BuildRequires:  kf5-kdbusaddons-devel >= %{majmin}
BuildRequires:  kf5-kwindowsystem-devel >= %{majmin}

# for systemd-related macros
BuildRequires:  systemd

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5X11Extras)

BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%if %{without kf6_compat}
Conflicts:      kglobalacceld
%endif

%description
%{summary}.

%package        libs
Summary:        Runtime libraries for %{name}
Requires:       %{name} = %{version}-%{release}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{framework}-%{version}

%build
%cmake_kf5 %{?with_kf6_compat:-DBUILD_RUNTIME=OFF}
%cmake_build

%install
%cmake_install

# unpackaged files
%if 0%{?flatpak:1}
rm -fv %{buildroot}%{_prefix}/lib/systemd/user/plasma-kglobalaccel.service
%endif

%find_lang_kf5 kglobalaccel5_qt

%files -f kglobalaccel5_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}*
%if %{without kf6_compat}
%{_kf5_bindir}/kglobalaccel5
%{_kf5_datadir}/kservices5/kglobalaccel5.desktop
%{_datadir}/dbus-1/services/org.kde.kglobalaccel.service
%if ! 0%{?flatpak:1}
%{_userunitdir}/plasma-kglobalaccel.service
%endif
%endif

%files libs
%{_kf5_libdir}/libKF5GlobalAccel.so.*
%if %{without kf6_compat}
%{_kf5_libdir}/libKF5GlobalAccelPrivate.so.*
%{_kf5_qtplugindir}/org.kde.kglobalaccel5.platforms/
%endif

%files devel
%{_kf5_includedir}/KGlobalAccel/
%{_kf5_libdir}/libKF5GlobalAccel.so
%{_kf5_libdir}/cmake/KF5GlobalAccel/
%{_kf5_archdatadir}/mkspecs/modules/qt_KGlobalAccel.pri
%{_kf5_datadir}/dbus-1/interfaces/*

%changelog
%autochangelog
