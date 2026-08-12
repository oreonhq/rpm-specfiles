%global source0_hash 74d78593d40ac89221fe195076f1b6a06fa2f70d2227032c8e21b0620b4d5c0d

%global framework syndication

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Epoch:   1
Version: 5.116.0
Release: 7%{?dist}
Summary: The Syndication Library

License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

BuildRequires: make
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kio-devel >= %{version}
BuildRequires:  kf5-kcodecs-devel >= %{version}

BuildRequires:  qt5-qtbase-devel

%if 0%{?tests}
#BuildRequires: dbus-x11
BuildRequires:  time
#BuildRequires: xorg-x11-server-Xvfb
%endif

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build
%{cmake_kf5} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
%cmake_build

%install
%cmake_install

%check
%if 0%{?tests}
DBUS_SESSION_BUS_ADDRESS=
DISPLAY=
export CTEST_OUTPUT_ON_FAILURE=1
%ctest ||:
%endif

%ldconfig_scriptlets

%files
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5Syndication.so.*

%files devel

%{_kf5_includedir}/Syndication/
%{_kf5_libdir}/libKF5Syndication.so
%{_kf5_libdir}/cmake/KF5Syndication/
%{_kf5_archdatadir}/mkspecs/modules/qt_Syndication.pri

%changelog
%autochangelog
