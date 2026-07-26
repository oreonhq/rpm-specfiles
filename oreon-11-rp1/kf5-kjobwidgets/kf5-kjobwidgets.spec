%global source0_hash eac37f7d02183f8d4347ab1d86608ee66007a3482a061169e4808caf853dbe87

%undefine __cmake_in_source_build
%global framework kjobwidgets

Name:           kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary:        KDE Frameworks 5 Tier 2 addon for KJobs

License:        CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  libX11-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel

%description
KDE Frameworks 5 Tier 2 addon for KJobs

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
Requires:       kf5-kcoreaddons-devel >= %{version}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install

%find_lang_kf5 kjobwidgets5_qt

%ldconfig_scriptlets

%files -f kjobwidgets5_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5JobWidgets.so.*

%files devel

%{_kf5_includedir}/KJobWidgets/
%{_kf5_libdir}/libKF5JobWidgets.so
%{_kf5_libdir}/cmake/KF5JobWidgets/
%{_kf5_datadir}/dbus-1/interfaces/*.xml
%{_kf5_archdatadir}/mkspecs/modules/qt_KJobWidgets.pri

%changelog
%autochangelog
