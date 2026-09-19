%global source0_hash 898fa19e4dbd089a4b00693b8226982f5cbb1751cf4fa21565eb93141b15fdc0

%undefine __cmake_in_source_build
%global framework kholidays

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Epoch:   1
Version: 5.116.0
Release: 7%{?dist}
Summary: The KHolidays Library

License: BSD-2-Clause AND CC0-1.0 AND GPL-3.0-or-later AND LGPL-2.0-or-later AND (GPL-3.0-or-later WITH Bison-exception-2.2)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros

# qt5-qtbase-devel
BuildRequires:  pkgconfig(Qt5Core)
# qt5-qtdeclarative-devel
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  qt5-qttools-static
BuildRequires: make
#BuildRequires:  cmake(Qt5LinguistTools)

# translations moved here
Conflicts: kde-l10n < 17.03

%description
The KHolidays library provides a C++ API that determines holiday
and other special events for a geographical region.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
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

%find_lang_kf5 libkholidays5_qt

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
time \
make test ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif

%ldconfig_scriptlets

%files -f libkholidays5_qt.lang
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/*categories
%{_kf5_libdir}/libKF5Holidays.so.*
%{_kf5_qmldir}/org/kde/kholidays/

%files devel

%{_kf5_includedir}/KHolidays/
%{_kf5_libdir}/libKF5Holidays.so
%{_kf5_libdir}/cmake/KF5Holidays/
%{_kf5_archdatadir}/mkspecs/modules/qt_KHolidays.pri

%changelog
%autochangelog
