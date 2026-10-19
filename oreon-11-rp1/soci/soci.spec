%global source0_hash 144f017cccc2e2d806badb3313d6ab3c67a1925bccaa747a46fb3907108a615d
%bcond empty 1
%bcond sqlite3 1
%bcond mysql 1
%bcond postgresql 1
%bcond odbc 1
%bcond oracle 0
%bcond tests 1
%global _default_oracle_dir /opt/oracle/app/oracle/product/11.1.0/db_1
%{!?_with_oracle_incdir: %define _with_oracle_incdir --with-oracle-include=%{_default_oracle_dir}/rdbms/public}
%{!?_with_oracle_libdir: %define _with_oracle_libdir --with-oracle-lib=%{_default_oracle_dir}/lib}
Name:           soci
Version:        4.1.4
%global ups_ver 4.1.4
Release:        1%{?dist}
Summary:        The database access library for C++ programmers
License:        BSL-1.0
URL:            https://github.com/SOCI/%{name}
Source0:        https://github.com/SOCI/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libpq-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  sqlite-devel
BuildRequires:  unixODBC-devel
# /oreon:deps
%description
%{name} is a C++ database access library that provides the
illusion of embedding SQL in regular C++ code, staying entirely within
the C++ standard.

%{?with_empty:%package        empty
Summary:        Empty back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    empty
This package contains the Empty back-end for %{name}, i.e.,
dynamic library specific to the Empty database. If you would like to
use %{name} in your programs with an empty database, you will need to
install %{name}-empty.}

%{?with_sqlite3:%package        sqlite3
Summary:        SQLite3 back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  sqlite-devel

%description    sqlite3
This package contains the SQLite3 back-end for %{name}, i.e.,
dynamic library specific to the SQLite3 database. If you would like to
use %{name} in your programs with SQLite3, you will need to
install %{name}-sqlite3.}

%{?with_mysql:%package        mysql
Summary:        MySQL back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  mariadb-connector-c-devel

%description    mysql
This package contains the MySQL back-end for %{name}, i.e.,
dynamic library specific to the MySQL database. If you would like to
use %{name} in your programs with MySQL, you will need to
install %{name}-mysql.}

%{?with_postgresql:%package        postgresql
Summary:        PostGreSQL back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  libpq-devel

%description    postgresql
This package contains the PostGreSQL back-end for %{name}, i.e.,
dynamic library specific to the PostGreSQL database. If you would like
to use %{name} in your programs with PostGreSQL, you will need to
install %{name}-postgresql.}

%{?with_odbc:%package        odbc
Summary:        ODBC back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  unixODBC-devel

%description    odbc
This package contains the ODBC back-end for %{name}, i.e.,
dynamic library specific to the ODBC connectors. If you would like to
use %{name} in your programs with ODBC, you will need to
install %{name}-odbc.}

%{?with_oracle:%package        oracle
Summary:        Oracle back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    oracle
This package contains the Oracle back-end for %{name}, i.e.,
dynamic library specific to the Oracle database. If you would like to
use %{name} in your programs with Oracle, you will need to install
%{name}-oracle.}

%package        devel
Summary:        Header files, libraries and development documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
This package contains the header files, dynamic libraries and
development documentation for %{name}. If you would like to develop
programs using %{name}, you will need to install %{name}-devel.

%{?with_empty:%package        empty-devel
Summary:        Empty back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-empty = %{version}-%{release}

%description    empty-devel
This package contains the Empty back-end for %{name}, i.e., header
files and dynamic libraries specific to an empty database. If you
would like to develop programs using %{name} and an empty database,
you will need to install %{name}-empty.}

%{?with_sqlite3:%package        sqlite3-devel
Summary:        SQLite3 back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-sqlite3 = %{version}-%{release}
Requires:       sqlite-devel

%description    sqlite3-devel
This package contains the SQLite3 back-end for %{name}, i.e., header
files and dynamic libraries specific to the SQLite3 database. If you
would like to develop programs using %{name} and SQLite3, you will need
to install %{name}-sqlite3.}

%{?with_mysql:%package        mysql-devel
Summary:        MySQL back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-mysql = %{version}-%{release}
Requires:       mariadb-connector-c-devel

%description    mysql-devel
This package contains the MySQL back-end for %{name}, i.e., header
files and dynamic libraries specific to the MySQL database. If you
would like to develop programs using %{name} and MySQL, you will need
to install %{name}-mysql.}

%{?with_postgresql:%package        postgresql-devel
Summary:        PostGreSQL back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-postgresql = %{version}-%{release}
Requires:       libpq-devel

%description    postgresql-devel
This package contains the PostGreSQL back-end for %{name}, i.e., header
files and dynamic libraries specific to the PostGreSQL database. If
you would like to develop programs using %{name} and PostGreSQL, you
will need to install %{name}-postgresql.}

%{?with_odbc:%package        odbc-devel
Summary:        ODBC back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-odbc = %{version}-%{release}
Requires:       unixODBC-devel

%description    odbc-devel
This package contains the Odbc back-end for %{name}, i.e., header
files and dynamic libraries specific to the Odbc database. If you
would like to develop programs using %{name} and Odbc, you will need
to install %{name}-odbc.}

%{?with_oracle:%package        oracle-devel
Summary:        Oracle back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-oracle = %{version}-%{release}

%description    oracle-devel
This package contains the Oracle back-end for %{name}, i.e., header
files and dynamic libraries specific to the Oracle database. If you
would like to develop programs using %{name} and Oracle, you will need
to install %{name}-oracle.}

%package        doc
Summary:        HTML documentation for the %{name} library
BuildArch:      noarch
%description    doc
This package contains the documentation in the HTML format of the %{name}
library. The documentation is the same as at the %{name} web page.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{ups_ver}

# Rename change-log and license file, so that they comply with
# packaging standard
mv README.md README
mv CHANGES ChangeLog
mv LICENSE_1_0.txt COPYING
echo "2025-03-30:" > NEWS
echo "- Version 4.1.0" >> NEWS
echo "- See the ChangeLog file for more details." >> NEWS
# Remove the spurious executable permission
chmod a-x AUTHORS README ChangeLog COPYING NEWS
# Unix ends of line
dos2unix AUTHORS README ChangeLog COPYING NEWS

%build

%define soci_testflags -DBUILD_TESTS="NONE"
%if %{with tests}
%define soci_testflags -DSOCI_TEST=ON -DSOCI_EMPTY_TEST_CONNSTR="dummy" -DSOCI_SQLITE3_TEST_CONNSTR="test.db" -DSOCI_POSTGRESQL_TEST_CONNSTR:STRING="dbname=soci_test" -DSOCI_MYSQL_TEST_CONNSTR:STRING="db=soci_test user=mloskot password=pantera"
%endif
%cmake \
 -DSOCI_STATIC=OFF \
 -DSOCI_EMPTY=%{?with_empty:ON}%{!?with_empty:OFF} \
 -DSOCI_SQLITE3=%{?with_sqlite3:ON}%{!?with_sqlite3:OFF} \
 -DSOCI_POSTGRESQL=%{?with_postgresql:ON}%{!?with_postgresql:OFF} \
 -DSOCI_MYSQL=%{?with_mysql:ON}%{!?with_mysql:OFF} \
 -DSOCI_ODBC=%{?with_odbc:ON}%{!?with_odbc:OFF} \
 -DSOCI_ORACLE=%{?with_oracle:ON %{?_with_oracle_incdir} %{?_with_oracle_libdir}}%{!?with_oracle:OFF} \
 %{soci_testflags}
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

%{ctest --exclude-regex 'soci_(odbc|mysql|postgresql)_test'}
%endif
%files -f %{oreon_filedir}/main.list
%files -n soci-empty -f %{oreon_filedir}/soci-empty.list
%files -n soci-sqlite3 -f %{oreon_filedir}/soci-sqlite3.list
%files -n soci-mysql -f %{oreon_filedir}/soci-mysql.list
%files -n soci-postgresql -f %{oreon_filedir}/soci-postgresql.list
%files -n soci-odbc -f %{oreon_filedir}/soci-odbc.list
%files -n soci-devel -f %{oreon_filedir}/soci-devel.list
%files -n soci-empty-devel -f %{oreon_filedir}/soci-empty-devel.list
%files -n soci-sqlite3-devel -f %{oreon_filedir}/soci-sqlite3-devel.list
%files -n soci-mysql-devel -f %{oreon_filedir}/soci-mysql-devel.list
%files -n soci-postgresql-devel -f %{oreon_filedir}/soci-postgresql-devel.list
%files -n soci-odbc-devel -f %{oreon_filedir}/soci-odbc-devel.list
%files -n soci-doc -f %{oreon_filedir}/soci-doc.list

%changelog

%autochangelog
