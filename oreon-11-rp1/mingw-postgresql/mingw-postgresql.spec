%global source0_hash none

%{?mingw_package_header}

Name:           mingw-postgresql
Version:        16.9
Release:        2%{?dist}
Summary:        MinGW Windows PostgreSQL library

License:        PostgreSQL
URL:            http://www.postgresql.org/
Source0:        https://ftp.postgresql.org/pub/source/v%{version}/postgresql-%{version}.tar.bz2
Source1:        https://ftp.postgresql.org/pub/source/v%{version}/postgresql-%{version}.tar.bz2.sha256

# Allow linking to MinGW TCL DLL
Patch0:         postgresql-10.0-mingw.patch
# https://www.postgresql.org/message-id/2a6c418e-373b-8466-fcb8-ce729aab255f@gmail.com
Patch1:         postgresql-11.2-import-name.patch
# https://www.postgresql.org/message-id/2a6c418e-373b-8466-fcb8-ce729aab255f@gmail.com
Patch2:         postgresql-11.2-static-libraries.patch
# Use winpthreads directly instead of internal reimplementation
# It causes multiple definition errors if linked together with something that pulls in winpthreads
#Patch3:         postgresql_pthread.patch
# Keep/add some libraries in SHLIB_LINK as eventually passed to the pkgconfig Libs.private:
# - libz, libpathcch, required by libcrypto
# - libiconv, required by libintl
Patch4:         postgresql_libs.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gettext
#BuildRequires:  mingw32-icu
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw32-libxslt
BuildRequires:  mingw32-openssl
BuildRequires:  mingw32-tcl
BuildRequires:  mingw32-readline
BuildRequires:  mingw32-winpthreads
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gettext
#BuildRequires:  mingw64-icu
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw64-libxslt
BuildRequires:  mingw64-openssl
BuildRequires:  mingw64-readline
BuildRequires:  mingw64-tcl
BuildRequires:  mingw64-winpthreads
BuildRequires:  mingw64-zlib

BuildRequires:  bison flex gettext make pkgconfig tcl

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
%autosetup -p1 -n postgresql-%{version}

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
# Make DLL definition file visible during each arch build
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

# move DLLs to bin
mv %{buildroot}%{mingw32_libdir}/*.dll %{buildroot}%{mingw32_bindir}
mv %{buildroot}%{mingw64_libdir}/*.dll %{buildroot}%{mingw64_bindir}

# due to Fedora packaging policy, delete executables
rm %{buildroot}%{mingw32_bindir}/*.exe
rm %{buildroot}%{mingw64_bindir}/*.exe
rm -rf %{buildroot}%{mingw32_libdir}/postgresql/
rm -rf %{buildroot}%{mingw64_libdir}/postgresql/

# libpostgres.dll.a is just the import library for postgres.exe, delete it
rm -f %{buildroot}%{mingw32_libdir}/libpostgres.{a,dll.a}
rm -f %{buildroot}%{mingw64_libdir}/libpostgres.{a,dll.a}

# remove server support files
rm -rf %{buildroot}%{mingw32_bindir}/pltcl*
rm -rf %{buildroot}%{mingw64_bindir}/pltcl*
rm -rf %{buildroot}%{mingw32_datadir}
rm -rf %{buildroot}%{mingw64_datadir}

# Win32
%files -n mingw32-postgresql
%license COPYRIGHT
%{mingw32_bindir}/libecpg.dll
%{mingw32_bindir}/libecpg_compat.dll
%{mingw32_bindir}/libpgtypes.dll
%{mingw32_bindir}/libpq.dll
%{mingw32_includedir}/libpq/
%{mingw32_includedir}/postgresql/
%{mingw32_includedir}/ecpg*.h
%{mingw32_includedir}/libpq-events.h
%{mingw32_includedir}/libpq-fe.h
%{mingw32_includedir}/pg*.h
%{mingw32_includedir}/postgres_ext.h
%{mingw32_includedir}/sql*.h
%{mingw32_libdir}/libecpg.dll.a
%{mingw32_libdir}/libecpg_compat.dll.a
%{mingw32_libdir}/libpgtypes.dll.a
%{mingw32_libdir}/libpq.dll.a
%{mingw32_libdir}/pkgconfig/*.pc

%files -n mingw32-postgresql-static
%{mingw32_libdir}/libecpg.a
%{mingw32_libdir}/libecpg_compat.a
%{mingw32_libdir}/libpq.a
%{mingw32_libdir}/libpgcommon.a
%{mingw32_libdir}/libpgcommon_shlib.a
%{mingw32_libdir}/libpgfeutils.a
%{mingw32_libdir}/libpgport.a
%{mingw32_libdir}/libpgport_shlib.a
%{mingw32_libdir}/libpgtypes.a

# Win64
%files -n mingw64-postgresql
%license COPYRIGHT
%{mingw64_bindir}/libecpg.dll
%{mingw64_bindir}/libecpg_compat.dll
%{mingw64_bindir}/libpgtypes.dll
%{mingw64_bindir}/libpq.dll
%{mingw64_includedir}/libpq/
%{mingw64_includedir}/postgresql/
%{mingw64_includedir}/ecpg*.h
%{mingw64_includedir}/libpq-events.h
%{mingw64_includedir}/libpq-fe.h
%{mingw64_includedir}/pg*.h
%{mingw64_includedir}/postgres_ext.h
%{mingw64_includedir}/sql*.h
%{mingw64_libdir}/libecpg.dll.a
%{mingw64_libdir}/libecpg_compat.dll.a
%{mingw64_libdir}/libpgtypes.dll.a
%{mingw64_libdir}/libpq.dll.a
%{mingw64_libdir}/pkgconfig/*.pc

%files -n mingw64-postgresql-static
%{mingw64_libdir}/libecpg.a
%{mingw64_libdir}/libecpg_compat.a
%{mingw64_libdir}/libpq.a
%{mingw64_libdir}/libpgcommon.a
%{mingw64_libdir}/libpgcommon_shlib.a
%{mingw64_libdir}/libpgfeutils.a
%{mingw64_libdir}/libpgport.a
%{mingw64_libdir}/libpgport_shlib.a
%{mingw64_libdir}/libpgtypes.a

%changelog
%autochangelog
