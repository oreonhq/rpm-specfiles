%global framework syndication

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Epoch:   1
Version: 5.116.0
Release: 5%{?dist}
Summary: The Syndication Library

License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
