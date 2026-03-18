%undefine __cmake_in_source_build
%global framework akonadi-notes

# uncomment to enable bootstrap mode
%global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: The Akonadi Notes Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

BuildRequires: make
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
%global kf5_ver 5.23
BuildRequires:  kf5-ki18n-devel >= %{kf5_ver}

BuildRequires:  cmake(Qt5Xml)

#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-akonadi-server-devel >= %{majmin_ver}
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}

%if 0%{?tests}
BuildRequires: kf5-akonadi-server >= %{majmin_ver}
BuildRequires: kf5-akonadi-server-mysql
BuildRequires: xorg-x11-server-Xvfb
%endif

# split from kf5-akonadi/kdepimlibs in 16.07
Obsoletes: kf5-akonadi < 16.07

%description
%{summary}.

%package   devel
Summary:   Development files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
# split from kf5-akonadi/kdepimlibs in 16.07
Obsoletes: kf5-akonadi-devel < 16.07
Requires:  cmake(KPim5Mime)
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

%find_lang %{name} --all-name


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
DBUS_SESSION_BUS_ADDRESS=
xvfb-run -a \
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_libdir}/libKPim5AkonadiNotes.so.*

%files devel
%{_kf5_libdir}/cmake/KF5AkonadiNotes/
%{_kf5_libdir}/cmake/KPim5AkonadiNotes/
%{_kf5_libdir}/libKPim5AkonadiNotes.so
%{_kf5_archdatadir}/mkspecs/modules/qt_AkonadiNotes.pri
%{_includedir}/KPim5/AkonadiNotes


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-5
- Prepare for Oreon 11 (RP1)
