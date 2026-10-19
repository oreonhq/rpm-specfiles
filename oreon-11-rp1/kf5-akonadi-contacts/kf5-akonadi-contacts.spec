%global source0_hash e7a4b37c6bb4dbdb074398a48050b3ea63b1ffd8b576f3efa9cef56759cf4251
%global framework akonadi-contacts
%if !0%{?bootstrap}
%global tests 0
%endif
Name:    kf5-%{framework}
Version: 23.08.5
Release:        1%{?dist}
Summary:        The Akonadi Contacts Library
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz
%global kf5_ver 5.83
%global majmin_ver %{version}
%if 0%{?tests}
%endif
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes: kf5-akonadi < 16.07
Obsoletes: kf5-akonadi-contact < 16.07
Provides:  kf5-akonadi-contact = %{version}-%{release}
Obsoletes: kdepim-apps-libs < 20.11.90
# oreon:deps
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-akonadi-mime-devel
BuildRequires:  kf5-akonadi-server-devel
BuildRequires:  kf5-grantleetheme-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcontacts-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kmime-devel
BuildRequires:  kf5-prison-devel
BuildRequires:  kf5-rpm-macros
# /oreon:deps
%description
%{summary}.

%package   libs
Summary:   Only the linkable libraries for %{name}
%description    libs
%{summary}.

%package   devel
Summary:   Development files for %{name}
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes: kf5-akonadi-devel < 16.07
Obsoletes: kf5-akonadi-contact-devel < 16.07
Provides:  kf5-akonadi-contact-devel = %{version}-%{release}
Obsoletes: kdepim-apps-libs-devel < 20.11.90
Requires:  cmake(KF5Akonadi)
Requires:  cmake(KF5Contacts)
Requires:  cmake(KPim5GrantleeTheme)
Recommends:  cmake(KF5CalendarCore)
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
DBUS_SESSION_BUS_ADDRESS=
xvfb-run -a \
%make_build test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n kf5-akonadi-contacts-libs -f %{oreon_filedir}/kf5-akonadi-contacts-libs.list
%files -n kf5-akonadi-contacts-devel -f %{oreon_filedir}/kf5-akonadi-contacts-devel.list

%changelog

%autochangelog
