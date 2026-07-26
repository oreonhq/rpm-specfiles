%global source0_hash ef689b29a27e57b6e5b41107d6fbb0252aba6788f6f96e079da0bddbc43a1c94

%global framework kunitconversion

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 2 addon for unit conversions

License: CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel

%description
KDE Frameworks 5 Tier 2 addon for unit conversions.

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
%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-man

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5UnitConversion.so.*
%{_kf5_datadir}/qlogging-categories5/%{framework}.*

%files devel

%{_kf5_includedir}/KUnitConversion/
%{_kf5_libdir}/libKF5UnitConversion.so
%{_kf5_libdir}/cmake/KF5UnitConversion/
%{_kf5_archdatadir}/mkspecs/modules/qt_KUnitConversion.pri

%changelog
%autochangelog
