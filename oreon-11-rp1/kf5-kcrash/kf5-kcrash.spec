%global source0_hash 81d346f9d663ccab1d388cb8fc45fb6c60efa33683b942251cf811e24179e865

%undefine __cmake_in_source_build
%global framework kcrash

Name:    kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary: KDE Frameworks 5 Tier 2 addon for handling application crashes

License: CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

## upstream patches

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kwindowsystem-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros

BuildRequires:  libX11-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel

%description
KCrash provides support for intercepting and handling application crashes.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build
%{cmake_kf5} \
  %{?fedora:-DKCRASH_CORE_PATTERN_RAISE:BOOL=OFF}
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5Crash.so.*

%files devel

%{_kf5_includedir}/KCrash/
%{_kf5_libdir}/libKF5Crash.so
%{_kf5_libdir}/cmake/KF5Crash/
%{_kf5_archdatadir}/mkspecs/modules/qt_KCrash.pri

%changelog
%autochangelog
