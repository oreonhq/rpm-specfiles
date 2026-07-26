%global source0_hash 2246a03812c7d90f10194ad01c2213a7646e383000a800277c6fb8d2bf81497c

# building multi-threaded causes intermittent build failures
%global _smp_mflags -j1

Name:           opendbx
Version:        1.4.6
Release:        43%{?dist}
Summary:        Lightweight but extensible database access library written in C

License:        GPL-2.0-or-later AND LGPL-2.0-or-later
# (util/argmap.{cpp,hpp}) and lib/opendbx/api are LGPL-2.0-or-later
URL:            http://www.linuxnetworks.de/doc/index.php/OpenDBX
Source0:        http://linuxnetworks.de/opendbx/download/%{name}-%{version}.tar.gz
Patch0:         opendbx-1.4.6-freetds-fix.patch
# Remove obsolete options from Doxyfile.in, fix INPUT file name to generate docs for C++ API.
Patch1:         opendbx-1.4.6-doxygen-1.9.1.patch
# Remove obsolete throws( std::exception ) from C++ API that fail to build with C++17.
Patch2:         opendbx-1.4.6-dynamic-exceptions.patch
Patch3:         opendbx-c99.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gcc
%if 0%{?fedora}
BuildRequires:  sqlite2-devel
%endif
BuildRequires:  mariadb-connector-c-devel, libpq-devel, sqlite-devel, readline-devel
%if 0%{?fedora} || 0%{?rhel} < 10
BuildRequires:  firebird-devel
%endif
BuildRequires:  freetds-devel, ncurses-devel
BuildRequires:  doxygen, docbook2X, gettext
BuildRequires:  automake, gettext-devel, libtool

%{?filter_setup:
%filter_provides_in %{_libdir}/opendbx/lib.*backend\.so.*$
%filter_requires_in %{_libdir}/opendbx/lib.*backend\.so.*$
%filter_setup
}

%description
Provides an abstraction layer to all supported databases with a single, clean
and simple interface that leads to an elegant code design automatically.
If you want your application to support different databases with little effort,
this is definitively the right thing for you!

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        mysql
Summary:        MySQL backend - provides mysql support in %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    mysql
Allows odbx_init with "mysql" as the backend parameter.

%package        postgresql
Summary:        PostgreSQL backend - provides postgresql support in %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    postgresql
Allows odbx_init with "pgsql" as the backend parameter.

%if 0%{?fedora} ||  0%{?rhel} <= 7
%package        sqlite2
Summary:        SQLite 2 backend - provides sqlite2 support in %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    sqlite2
Allows odbx_init with "sqlite" as the backend parameter.
%endif

%package        sqlite
Summary:        SQLite 3 backend - provides sqlite3 support in %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    sqlite
Allows odbx_init with "sqlite3" as the backend parameter.

%if 0%{?fedora} || 0%{?rhel} < 10
%package        firebird
Summary:        Firebird backend - provides firebird support in %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    firebird
Allows odbx_init with "firebird" as the backend parameter.
%endif

%package        mssql
Summary:        MSSQL backend - provides mssql support in %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    mssql
Allows odbx_init with "mssql" as the backend parameter.

%package        sybase
Summary:        Sybase backend - provides sybase support in %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    sybase
Allows odbx_init with "sybase" as the backend parameter.

%package        utils
Summary:        Utility binaries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
The %{name}-utils package provides the odbx-sql tool.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# To fix Doxygen parsing issue
ln -s api lib/%{name}/api.dox
# C++ API file must have extension .hpp to be parsed correctly by doxygen
cp lib/%{name}/api lib/%{name}/api.hpp

%build
autoreconf -iv
export CXXFLAGS="-std=c++14 -Wno-error=incompatible-pointer-types -Wno-error=int-conversion %optflags"
export CFLAGS="-Wno-error=incompatible-pointer-types -Wno-error=int-conversion %optflags"
%if 0%{?fedora}
%configure --with-backends="mysql pgsql sqlite sqlite3 \
%if 0%{?fedora} || 0%{?rhel} < 10
firebird \
%endif
mssql sybase" CPPFLAGS="-I%{_includedir}/mysql -I%{_includedir}/firebird" --disable-test --disable-static LDFLAGS="-L%{_libdir}/mysql"
%else
%configure --with-backends="mysql pgsql sqlite3 \
%if 0%{?fedora} || 0%{?rhel} < 10
firebird \
%endif
mssql sybase" CPPFLAGS="-I%{_includedir}/mysql -I%{_includedir}/firebird" --disable-test --disable-static LDFLAGS="-L%{_libdir}/mysql"
%endif
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# fix multithreaded builds by precreating the doc/{html,xml,man} directories
mkdir -p doc/{html,xml.man}
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}
%find_lang %{name}-utils

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%dir %{_libdir}/opendbx
%{_libdir}/*.so.*
%{_datadir}/opendbx/keywords

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.gz

%files mysql
%{_libdir}/opendbx/*mysql*.so
%{_libdir}/opendbx/*mysql*.so.*

%files postgresql
%{_libdir}/opendbx/*pgsql*.so
%{_libdir}/opendbx/*pgsql*.so.*

%if 0%{?fedora}
%files sqlite2
%{_libdir}/opendbx/*sqlitebackend.so
%{_libdir}/opendbx/*sqlitebackend.so.*
%endif

%files sqlite
%{_libdir}/opendbx/*sqlite3backend.so
%{_libdir}/opendbx/*sqlite3backend.so.*

%if 0%{?fedora} || 0%{?rhel} < 10
%files firebird
%{_libdir}/opendbx/*firebird*.so
%{_libdir}/opendbx/*firebird*.so.*
%endif

%files mssql
%{_libdir}/opendbx/*mssql*.so
%{_libdir}/opendbx/*mssql*.so.*

%files sybase
%{_libdir}/opendbx/*sybase*.so
%{_libdir}/opendbx/*sybase*.so.*

%files utils -f %{name}-utils.lang
%{_bindir}/odbx-sql
%{_mandir}/man1/odbx-sql.1.gz

%changelog
%autochangelog
