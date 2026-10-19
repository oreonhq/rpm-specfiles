%global source0_hash cf8da9409412ed3348ee4a8ab9e2df8ecf844070f84c8cdbf0b6f4c8269339ca
%global base_name akonadi-calendar
%if !0%{?bootstrap}
%global tests 1
%endif
Name:    kf5-%{base_name}
Version: 23.08.5
Release:        1%{?dist}
Summary:        The Akonadi Calendar Library
License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{base_name}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{base_name}-%{version}.tar.xz
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}
%global kf5_ver 5.87.0
%global majmin_ver %{version}
%if 0%{?tests}
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake(KF5TextEditTextToSpeech)
BuildRequires:  cmake(KPim5Libkdepim)
BuildRequires:  cmake(KPim5MailTransport)
BuildRequires:  cmake(KPim5MessageCore)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cyrus-sasl-devel
BuildRequires:  dbus-x11
BuildRequires:  extra-cmake-modules
BuildRequires:  grantlee-qt5-devel
BuildRequires:  kf5-akonadi-contacts-devel
BuildRequires:  kf5-akonadi-server
BuildRequires:  kf5-akonadi-server-devel
BuildRequires:  kf5-akonadi-server-mysql
BuildRequires:  kf5-grantleetheme-devel
BuildRequires:  kf5-kcalendarcore-devel
BuildRequires:  kf5-kcalendarutils-devel
BuildRequires:  kf5-kcodecs-devel
BuildRequires:  kf5-kcontacts-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kidentitymanagement-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
%{summary}.

%package        libs
Summary:        Only the linkable libraries for %{name}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kf5-akonadi-contacts-devel
Requires:       kf5-akonadi-server-devel
Requires:       kf5-kcalendarcore-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{base_name}-%{version} -p1

%build

%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
%cmake_build
%install
%cmake_install
%find_lang libakonadi-calendar5
%find_lang libakonadi-calendar5-serializer
cat libakonadi-calendar5-serializer.lang >> libakonadi-calendar5.lang
%find_lang kalendarac
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n kf5-akonadi-calendar-libs -f %{oreon_filedir}/kf5-akonadi-calendar-libs.list
%files -n kf5-akonadi-calendar-devel -f %{oreon_filedir}/kf5-akonadi-calendar-devel.list

%changelog

%autochangelog
