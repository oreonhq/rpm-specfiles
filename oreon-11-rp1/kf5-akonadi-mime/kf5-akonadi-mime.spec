%global source0_hash fd40e599ea73fe8107d195673ae721461edfedf1bf56b2bef13fab940de5c833

%undefine __cmake_in_source_build
%global framework akonadi-mime

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 0
%endif

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: The Akonadi Mime Library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

BuildRequires: make
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
%global kf5_ver 5.23
BuildRequires:  kf5-kio-devel >= %{kf5_ver}
BuildRequires:  kf5-kcompletion-devel >= %{kf5_ver}
BuildRequires:  kf5-kcodecs-devel >= %{kf5_ver}
BuildRequires:  kf5-kcontacts-devel >= %{kf5_ver}

BuildRequires:  cmake(Qt5Gui)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(shared-mime-info)

#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-akonadi-server-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-server-devel >= %{majmin_ver}
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}

%if 0%{?tests}
BuildRequires: kf5-akonadi-server >= %{majmin_ver}
BuildRequires: kf5-akonadi-server-mysql
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires:  %{name}-libs%{?_isa} = %{version}-%{release}

# when conflicts with kdepimlibs was fixed
# https://bugzilla.redhat.com/show_bug.cgi?id=2088779
Conflicts: kdepimlibs < 4.14.10-40

# split from kf5-akonadi/kdepimlibs in 16.07
Obsoletes: kf5-akonadi < 16.07

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
Requires: cmake(KF5Akonadi)
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

%find_lang %{name} --all-name

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
DBUS_SESSION_BUS_ADDRESS=
xvfb-run -a \
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf5_datadir}/akonadi/plugins/serializer/
%{_kf5_datadir}/config.kcfg/specialmailcollections.kcfg
%{_kf5_datadir}/mime/packages/x-vnd.kde.contactgroup.xml
%{_kf5_qtplugindir}/akonadi_serializer_mail.so

%files libs -f %{name}.lang
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5AkonadiMime.so.*

%files devel 
%{_kf5_bindir}/akonadi_benchmarker
%{_kf5_archdatadir}/mkspecs/modules/qt_AkonadiMime.pri
%{_includedir}/KPim5/AkonadiMime/
%{_kf5_libdir}/cmake/KF5AkonadiMime/
%{_kf5_libdir}/cmake/KPim5AkonadiMime/
%{_kf5_libdir}/libKPim5AkonadiMime.so

%changelog
%autochangelog
