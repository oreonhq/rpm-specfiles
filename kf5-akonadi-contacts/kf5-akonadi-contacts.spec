%global framework akonadi-contacts

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 0
%endif

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: The Akonadi Contacts Library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
%global kf5_ver 5.83
BuildRequires:  kf5-kio-devel >= %{kf5_ver}
BuildRequires:  kf5-kconfig-devel >= %{kf5_ver}
BuildRequires:  kf5-ki18n-devel >= %{kf5_ver}
BuildRequires:  kf5-prison-devel >= %{kf5_ver}

BuildRequires:  cmake(Grantlee5) >= 5.1
BuildRequires:  cmake(Qt5Widgets) >= 5.8

#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-akonadi-mime-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-server-devel >= %{majmin_ver}
BuildRequires:  kf5-grantleetheme-devel >= %{majmin_ver}
%if !(0%{?rhel} == 8 && ( "%{_arch}" == "aarch64" || "%{_arch}" == "s390x" ))
BuildRequires:  kf5-kcalendarcore-devel >= %{majmin_ver}
%endif
BuildRequires:  kf5-kcontacts-devel >= %{majmin_ver}
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}
#BuildRequires:  kf5-libkleo-devel >= %{majmin_ver}

%if 0%{?tests}
BuildRequires: kf5-akonadi-server >= %{majmin_ver}
BuildRequires: kf5-akonadi-server-mysql
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires:  %{name}-libs%{?_isa} = %{version}-%{release}

# split from kf5-akonadi/kdepimlibs in 16.07
Obsoletes: kf5-akonadi < 16.07
Obsoletes: kf5-akonadi-contact < 16.07
Provides:  kf5-akonadi-contact = %{version}-%{release}

# kdepim-apps-libs deprecated, some content moved here
Obsoletes: kdepim-apps-libs < 20.11.90

%description
%{summary}.

%package   libs
Summary:   Only the linkable libraries for %{name}
%description    libs
%{summary}.

%package   devel
Summary:   Development files for %{name}
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}
# split from kf5-akonadi/kdepimlibs in 16.07
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
DBUS_SESSION_BUS_ADDRESS=
xvfb-run -a \
%make_build test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files
%dir %{_kf5_datadir}/kf5/akonadi/
%{_kf5_datadir}/akonadi/plugins/serializer/
%{_kf5_datadir}/kf5/akonadi/contact/
%{_kf5_qtplugindir}/akonadi_serializer_*.so

%files libs -f %{name}.lang
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5AkonadiContact.so.*
%{_kf5_libdir}/libKPim5ContactEditor.so.*

%files devel
%{_kf5_archdatadir}/mkspecs/modules/qt_AkonadiContact.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_ContactEditor.pri
%{_includedir}/KPim5/AkonadiContact/
%{_includedir}/KPim5/AkonadiContactEditor/
%{_kf5_libdir}/cmake/KPim5AkonadiContact/
%{_kf5_libdir}/cmake/KF5AkonadiContactEditor/
%{_kf5_libdir}/cmake/KPim5ContactEditor/
%{_kf5_libdir}/libKPim5AkonadiContact.so
%{_kf5_libdir}/libKPim5ContactEditor.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-5
- Prepare for Oreon 11 (RP1)
