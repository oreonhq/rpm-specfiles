%global source1_hash e52d4e0c7bdd6f48d8a6a5ec721a3be042729d3152fe63bc15f91d4f3e634fbe
%global source0_hash 07c00fb824df0a0c295f249f44691b86e3266753b380c96f633c3311e10bd005
%{?mingw_package_header}
Name:           mingw-postgresql
Version:        16.9
Release:        1%{?dist}
Summary:        MinGW Windows PostgreSQL library
License:        PostgreSQL
URL:            http://www.postgresql.org/
Source0:        https://ftp.postgresql.org/pub/source/v%{version}/postgresql-%{version}.tar.bz2
Source1:        https://ftp.postgresql.org/pub/source/v%{version}/postgresql-%{version}.tar.bz2.sha256
Patch0:         postgresql-10.0-mingw.patch
Patch1:         postgresql-11.2-import-name.patch
Patch2:         postgresql-11.2-static-libraries.patch
Patch4:         postgresql_libs.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw32-libxslt
BuildRequires:  mingw32-openssl
BuildRequires:  mingw32-readline
BuildRequires:  mingw32-tcl
BuildRequires:  mingw32-winpthreads
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw64-libxslt
BuildRequires:  mingw64-openssl
BuildRequires:  mingw64-readline
BuildRequires:  mingw64-tcl
BuildRequires:  mingw64-winpthreads
BuildRequires:  mingw64-zlib
BuildRequires:  pkgconfig
BuildRequires:  tcl
# /oreon:deps
%description
MinGW Windows copy of PostgreSQL. PostgreSQL is an advanced Object-Relational
database management system (DBMS).

# Win32
%package -n mingw32-postgresql
Summary:        MinGW Windows PostgreSQL library
%description -n mingw32-postgresql
MinGW Windows copy of PostgreSQL. PostgreSQL is an advanced Object-Relational
database management system (DBMS).

%package -n mingw32-postgresql-static
Summary:        Static libraries for MinGW PostgreSQL
Requires:       mingw32-postgresql = %{version}-%{release}
%description -n mingw32-postgresql-static
%{summary}

# Win64
%package -n mingw64-postgresql
Summary:        MinGW Windows PostgreSQL library
%description -n mingw64-postgresql
MinGW Windows copy of PostgreSQL. PostgreSQL is an advanced Object-Relational
database management system (DBMS).

%package -n mingw64-postgresql-static
Summary:        Static libraries for MinGW PostgreSQL
Requires:       mingw64-postgresql = %{version}-%{release}
%description -n mingw64-postgresql-static
%{summary}

%{?mingw_debug_package}

%prep
%global oreon_srcdir postgresql-%{version}
%oreon_prep
%build

MINGW32_CONFIGURE_ARGS=--with-tclconfig=%{mingw32_libdir} \
MINGW64_CONFIGURE_ARGS=--with-tclconfig=%{mingw64_libdir} \
%mingw_configure \
    --with-openssl \
    --enable-thread-safety \
    --enable-integer-datetimes \
    --enable-nls \
    --without-icu \
    --with-ldap \
    --with-libxml \
    --with-libxslt \
    --with-tcl
ln -s %{_builddir}/%{buildsubdir}/src/interfaces/libpq/libpqdll.def ./build_win32/src/interfaces/libpq/
ln -s %{_builddir}/%{buildsubdir}/src/interfaces/libpq/libpqdll.def ./build_win64/src/interfaces/libpq/
ln -s %{_builddir}/%{buildsubdir}/src/interfaces/ecpg/ecpglib/libecpgdll.def ./build_win32/src/interfaces/ecpg/ecpglib/
ln -s %{_builddir}/%{buildsubdir}/src/interfaces/ecpg/ecpglib/libecpgdll.def ./build_win64/src/interfaces/ecpg/ecpglib/
ln -s %{_builddir}/%{buildsubdir}/src/interfaces/ecpg/pgtypeslib/libpgtypesdll.def ./build_win32/src/interfaces/ecpg/pgtypeslib/
ln -s %{_builddir}/%{buildsubdir}/src/interfaces/ecpg/pgtypeslib/libpgtypesdll.def ./build_win64/src/interfaces/ecpg/pgtypeslib/
ln -s %{_builddir}/%{buildsubdir}/src/interfaces/ecpg/compatlib/libecpg_compatdll.def ./build_win32/src/interfaces/ecpg/compatlib/
ln -s %{_builddir}/%{buildsubdir}/src/interfaces/ecpg/compatlib/libecpg_compatdll.def ./build_win64/src/interfaces/ecpg/compatlib/
%mingw_make_build
%install
%mingw_make_install
mv %{buildroot}%{mingw32_libdir}/*.dll %{buildroot}%{mingw32_bindir}
mv %{buildroot}%{mingw64_libdir}/*.dll %{buildroot}%{mingw64_bindir}
rm %{buildroot}%{mingw32_bindir}/*.exe
rm %{buildroot}%{mingw64_bindir}/*.exe
rm -rf %{buildroot}%{mingw32_libdir}/postgresql/
rm -rf %{buildroot}%{mingw64_libdir}/postgresql/
rm -f %{buildroot}%{mingw32_libdir}/libpostgres.{a,dll.a}
rm -f %{buildroot}%{mingw64_libdir}/libpostgres.{a,dll.a}
rm -rf %{buildroot}%{mingw32_bindir}/pltcl*
rm -rf %{buildroot}%{mingw64_bindir}/pltcl*
rm -rf %{buildroot}%{mingw32_datadir}
rm -rf %{buildroot}%{mingw64_datadir}
%oreon_autofiles mingw32-postgresql usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-postgresql-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-postgresql usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-postgresql-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-postgresql -f %{oreon_filedir}/mingw32-postgresql.list
%files -n mingw32-postgresql-static -f %{oreon_filedir}/mingw32-postgresql-static.list
%files -n mingw64-postgresql -f %{oreon_filedir}/mingw64-postgresql.list
%files -n mingw64-postgresql-static -f %{oreon_filedir}/mingw64-postgresql-static.list

%changelog

%autochangelog
