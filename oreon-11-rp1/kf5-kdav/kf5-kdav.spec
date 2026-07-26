%global source0_hash c642edbe8417409d8afe2d87ce0ca8f4372f9ee88b25129091c5a5681fa51bd3

%global framework kdav

# uncomment to enable bootstrap mode
%global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kf5-%{framework}
Epoch:   1
Version: 5.116.0
Release: 6%{?dist}
Summary: A DAV protocol implementation with KJobs

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}

BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5XmlPatterns)

BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kio-devel  >= %{majmin}

BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)

%if 0%{?tests}
BuildRequires: cmake(Qt5Test)
BuildRequires: dbus-x11
BuildRequires: xorg-x11-server-Xvfb
%endif

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       cmake(KF5CoreAddons)
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

%find_lang %{name} --all-name --with-html

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 300" -C %{_target_platform} ||:
%endif

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README*
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKF5DAV.so.5*

%files devel
%{_kf5_includedir}/KDAV/
%{_kf5_includedir}/KDAV/kdav_version.h
%{_kf5_libdir}/libKF5DAV.so
%{_kf5_libdir}/cmake/KF5DAV/
%{_kf5_archdatadir}/mkspecs/modules/qt_KDAV.pri

%changelog
%autochangelog
