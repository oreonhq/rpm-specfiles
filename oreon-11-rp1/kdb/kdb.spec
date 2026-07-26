%global source0_hash 8f8983bc8d143832dc14bc2003ba6af1af27688e477c0c791fd61445464f2069

%undefine __cmake_in_source_build
# koffice version to Obsolete
%global koffice_ver 3:2.3.70

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
# some known failures, ping upstream
%global tests 1
%endif

Name:    kdb
Summary: Database Connectivity and Creation Framework
Version: 3.2.0
Release: 25%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+

Url:     https://community.kde.org/KDb
Source0: http://download.kde.org/stable/%{name}/src/%{name}-%{version}.tar.xz

## upstream patches
Patch1: 0001-cmake-find-PostgreSQL-12.patch
Patch2: 0002-PgSQL-driver-fix-build-with-PostgreSQL-12.patch
Patch3: 0003-Autotests-Fix-QCOMPARE-for-QString-const-char-and-QB.patch
Patch4: 0004-TRIVIAL-Move-Q_REQUIRED_RESULT-to-correct-place.patch
Patch7: 0007-Take-all-args-to-kdbfeaturestest-before-the-driver.patch
Patch8: 0008-Expand-feature-test-for-buffered-cursors.patch
Patch9: 0009-Escape-table-name-in-when-building-a-select-statemen.patch
Patch10: 0010-Improve-a-bit-parse-error-diagnosis.patch
Patch12: 0012-Update-README.md-add-github-note-and-donation.patch
Patch13: 0013-cmake-find-PostgreSQL-13.patch
Patch17: 0017-Find-also-Python3-with-find_package-PythonInterp.patch
Patch20: 0020-Fix-build-with-newer-Qt.patch
Patch22: 0022-cmake-find-PostgreSQL-14.patch
Patch30: 0030-Fix-build-with-GCC-12-standard-attributes-in-middle-.patch

## upstreamable patches
# fix/santitize KDb3.pc dependencies
Patch100: kdb-3.2.0-pkgconfig.patch
# https://invent.kde.org/libraries/kdb/-/merge_requests/11
Patch1001: 1001-gcc-12-inline.patch
# Fix build with CMake 4.0
Patch1002: 1002-cmake4.patch

BuildRequires: gcc-c++

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5CoreAddons)

BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)

BuildRequires: libicu-devel
BuildRequires: python3

# drivers
BuildRequires: mariadb-connector-c-devel
# postgresql-private-devel introduced in f35+ with pgsql-13.4 and Conflicts: libpq-devel
%if 0%{?fedora} > 34 || 0%{?rhel} > 8
BuildRequires: postgresql-private-devel >= 13.4
%else
BuildRequires: libpq-devel
%endif
# this shouldn't be needed, but the build system configuration seems to
# mistakenly detect server-related headers
BuildRequires: postgresql-server-devel
BuildRequires: pkgconfig(sqlite3)

# autodeps
BuildRequires: cmake
BuildRequires: pkgconfig

%if 0%{?tests}
BuildRequires: cmake(Qt5Test)
%endif

Obsoletes: calligra-kexi-driver-sybase < 3.0.0
Obsoletes: calligra-kexi-driver-xbase < 3.0.0

%description
A database connectivity and creation framework for various database vendors.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(KF5CoreAddons)
%description devel
%{summary}.

%package  driver-mysql
Summary:  Mysql driver for %{name}
Obsoletes: koffice-kexi-driver-mysql < %{koffice_ver}
Obsoletes: calligra-kexi-driver-mysql < 3.0.0
Provides:  calligra-kexi-driver-mysql = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Supplements: (%{name} and mariadb-server)
%description driver-mysql
%{summary}.

%package  driver-postgresql
Summary:  Postgresql driver for %{name}
Obsoletes: koffice-kexi-driver-pgsql < %{koffice_ver}
Obsoletes: calligra-kexi-driver-pgsql < 2.3.86-2
Provides:  calligra-kexi-driver-pgsql = %{version}-%{release}
Obsoletes: calligra-kexi-driver-postgresql < 3.0.0
Provides:  calligra-kexi-driver-postgresql = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Supplements: (%{name} and postgresql-server)
%description driver-postgresql
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf5 \
  -Wno-dev \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{?!tests:OFF} \
  -DCMAKE_CXX_STANDARD=17 \
  -DPYTHON_EXECUTABLE:PATH="%{__python3}"

%cmake_build

%install
%cmake_install

%find_lang_kf5 kdb_qt
%find_lang_kf5 kdb_mysqldriver_qt
%find_lang_kf5 kdb_postgresqldriver_qt
%find_lang_kf5 kdb_sqlitedriver_qt
cat kdb_sqlitedriver_qt.lang >> kdb_qt.lang

%check
## tests have known failures, TODO: consult upstream
## assumes cmake files are installed on system (not buildroot)
#The following tests FAILED:
#         11 - HeadersTest (Failed)
%if 0%{?tests}
%ctest ||:
%endif

%ldconfig_scriptlets

%files -f kdb_qt.lang
%license COPYING.LIB
%{_libdir}/libKDb3.so.4*
%{_bindir}/kdb3_sqlite3_dump
%dir %{_qt5_plugindir}/kdb3/
# sqlite driver included in base (for now)
%{_qt5_plugindir}/kdb3/kdb_sqlitedriver.so
%{_qt5_plugindir}/kdb3/sqlite3/

%files driver-mysql -f kdb_mysqldriver_qt.lang
%{_qt5_plugindir}/kdb3/kdb_mysqldriver.so

%files driver-postgresql -f kdb_postgresqldriver_qt.lang
%{_qt5_plugindir}/kdb3/kdb_postgresqldriver.so

%files devel
%{_includedir}/KDb3/
%{_libdir}/libKDb3.so
%{_libdir}/cmake/KDb3/
%{_libdir}/pkgconfig/KDb3.pc
%{_kf5_archdatadir}/mkspecs/modules/qt_KDb3.pri

%changelog
%autochangelog
