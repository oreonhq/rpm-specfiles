%global source0_hash 2246a03812c7d90f10194ad01c2213a7646e383000a800277c6fb8d2bf81497c
%global _smp_mflags -j1
Name:           opendbx
Version:        1.4.6
Release:        1%{?dist}
Summary:        Lightweight but extensible database access library written in C
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            http://www.linuxnetworks.de/doc/index.php/OpenDBX
Source0:        https://src.fedoraproject.org/repo/pkgs/opendbx/%{name}-%{version}.tar.gz/3e89d7812ce4a28046bd60d5f969263d/%{name}-%{version}.tar.gz
Patch0:         opendbx-1.4.6-freetds-fix.patch
Patch1:         opendbx-1.4.6-doxygen-1.9.1.patch
Patch2:         opendbx-1.4.6-dynamic-exceptions.patch
Patch3:         opendbx-c99.patch
%{?filter_setup:
%filter_provides_in %{_libdir}/opendbx/lib.*backend\.so.*$
%filter_requires_in %{_libdir}/opendbx/lib.*backend\.so.*$
%filter_setup
}
# oreon:deps
BuildRequires:  automake
BuildRequires:  docbook2X
BuildRequires:  doxygen
BuildRequires:  freetds-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  libpq-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  sqlite-devel
# /oreon:deps
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

%package        sqlite
Summary:        SQLite 3 backend - provides sqlite3 support in %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    sqlite
Allows odbx_init with "sqlite3" as the backend parameter.

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
%configure --with-backends="mysql pgsql sqlite3 \
mssql sybase" CPPFLAGS="-I%{_includedir}/mysql -I%{_includedir}/firebird" --disable-test --disable-static LDFLAGS="-L%{_libdir}/mysql"
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
mkdir -p doc/{html,xml.man}
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang %{name}
%find_lang %{name}-utils
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n opendbx-devel -f %{oreon_filedir}/opendbx-devel.list
%files -n opendbx-mysql -f %{oreon_filedir}/opendbx-mysql.list
%files -n opendbx-postgresql -f %{oreon_filedir}/opendbx-postgresql.list
%files -n opendbx-sqlite -f %{oreon_filedir}/opendbx-sqlite.list
%files -n opendbx-mssql -f %{oreon_filedir}/opendbx-mssql.list
%files -n opendbx-sybase -f %{oreon_filedir}/opendbx-sybase.list
%files -n opendbx-utils -f %{oreon_filedir}/opendbx-utils.list

%changelog

%autochangelog
